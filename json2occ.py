import json
from OCC.Core.gp import gp_Pnt, gp_Dir, gp_Ax2, gp_Circ, gp_Vec
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire, BRepBuilderAPI_MakeFace
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakePrism
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse
from OCC.Core.STEPControl import STEPControl_Writer
from OCC.Core.TopoDS import TopoDS_Compound, TopoDS_Builder

def generate_occ_code_from_json_v2(json_data, unit_scale=100.0):
    """新版 JSON ➞ PythonOCC 代码字符串数组，支持 line/arc/circle、多环/孔洞"""
    parts = json_data.get("parts", {})

    occ = [
        # ---------- 基础 import ----------
        "from OCC.Core.gp import (gp_Pnt, gp_Dir, gp_Ax1, gp_Ax2, gp_Circ, gp_Vec, gp_Trsf)",
        "from OCC.Core.GC import GC_MakeArcOfCircle",
        "from OCC.Core.BRepBuilderAPI import (",
        "    BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire,",
        "    BRepBuilderAPI_MakeFace, BRepBuilderAPI_Transform",
        ")",
        "from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakePrism",
        "from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse",
        "from OCC.Core.STEPControl import STEPControl_AsIs",
        "",
        "all_shapes = []  # 存储每个 part 的体",
    ]

    # ---------- 遍历 parts ----------
    for part_name, part in parts.items():
        extrusion = part.get('extrusion', {})
        sketch    = part.get('sketch', {})
        coord_sys = part.get('coordinate_system', {})

        scale     = extrusion.get('sketch_scale', 1.0)
        depth_pos = extrusion.get('extrude_depth_towards_normal', 0.0) * unit_scale
        depth_neg = extrusion.get('extrude_depth_opposite_normal', 0.0) * unit_scale

        for face_key, face in sketch.items():          # face_1 …
            occ.append("wires = []")
            # ------ 每个 loop → wire ------
            for loop_key, loop in face.items():        # loop_1 …
                occ.append("edges = []")
                for elem_key, elem in loop.items():
                    # ---------- Line ----------
                    if elem_key.startswith('line_'):
                        sx, sy = elem['Start Point']; ex, ey = elem['End Point']
                        p1x = sx * scale * unit_scale
                        p1y = sy * scale * unit_scale
                        p2x = ex * scale * unit_scale
                        p2y = ey * scale * unit_scale
                        occ += [
                            f"p1 = gp_Pnt({p1x}, {p1y}, 0.0)",
                            f"p2 = gp_Pnt({p2x}, {p2y}, 0.0)",
                            "edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()",
                            "edges.append(edge)",
                        ]

                    # ---------- Arc (三点) ----------
                    elif elem_key.startswith('arc_'):
                        sx, sy = elem['Start Point']
                        mx, my = elem['Mid Point']
                        ex, ey = elem['End Point']
                        pts = [
                            (sx, sy, 'p1'),
                            (mx, my, 'p2'),
                            (ex, ey, 'p3'),
                        ]
                        for x, y, var in pts:
                            occ.append(f"{var} = gp_Pnt({x*scale*unit_scale}, {y*scale*unit_scale}, 0.0)")
                        occ += [
                            "curve = GC_MakeArcOfCircle(p1, p2, p3).Value()",
                            "edge  = BRepBuilderAPI_MakeEdge(curve).Edge()",
                            "edges.append(edge)",
                        ]

                    # ---------- Circle ----------
                    elif elem_key.startswith('circle_'):
                        cx, cy = elem['Center']; r = elem['Radius']
                        cx *= scale * unit_scale
                        cy *= scale * unit_scale
                        r  *= scale * unit_scale
                        occ += [
                            f"circ = gp_Circ(gp_Ax2(gp_Pnt({cx}, {cy}, 0.0), gp_Dir(0,0,1)), {r})",
                            "edge = BRepBuilderAPI_MakeEdge(circ).Edge()",
                            "edges.append(edge)",
                        ]

                    else:
                        occ.append(f'# 未识别元素 {elem_key}, 已跳过')

                # ------ edges → wire ------
                occ += [
                    "wire_mkr = BRepBuilderAPI_MakeWire()",
                    "for _e in edges: wire_mkr.Add(_e)",
                    "wires.append(wire_mkr.Wire())",
                ]

            # ------ wires → face (孔洞支持) ------
            occ += [
                "outer = wires[0]",
                "face_mkr = BRepBuilderAPI_MakeFace(outer)",
                "for hole_w in wires[1:]: face_mkr.Add(hole_w)",
                "face = face_mkr.Face()",
            ]

            # ------ 拉伸 ------
            # 拉伸部分的修改
            if depth_pos == 0 and depth_neg == 0:
                occ.append("# No extrusion, both depth_pos and depth_neg are 0")
            elif depth_pos != 0 and depth_neg == 0:
                occ.append(f"extruded = BRepPrimAPI_MakePrism(face, gp_Vec(0,0,1)*{depth_pos}).Shape()")
            elif depth_pos == 0 and depth_neg != 0:
                occ.append(f"extruded = BRepPrimAPI_MakePrism(face, gp_Vec(0,0,-1)*{depth_neg}).Shape()")
            else:
                # depth_pos != 0 and depth_neg != 0
                occ += [
                    f"pos = BRepPrimAPI_MakePrism(face, gp_Vec(0,0,1)*{depth_pos}).Shape()",
                    f"neg = BRepPrimAPI_MakePrism(face, gp_Vec(0,0,-1)*{depth_neg}).Shape()",
                    "extruded = BRepAlgoAPI_Fuse(pos, neg).Shape()",
                ]


            # ------ 变换 ------
            euler = coord_sys.get('Euler Angles', [0,0,0])
            trans = coord_sys.get('Translation Vector', [0,0,0])
            tx, ty, tz = [t*unit_scale for t in trans]

            occ += [
                "trsf = gp_Trsf(); trsf.SetTranslation(gp_Vec({},{},{}))".format(tx, ty, tz),
                "rot  = gp_Trsf(); rot.SetRotation(gp_Ax1(gp_Pnt(0,0,0), gp_Dir(0,0,1)), {})".format(euler[2]),
                "rot.Multiply(trsf)",
                "extruded = BRepBuilderAPI_Transform(extruded, rot, True).Shape()",
                "all_shapes.append(extruded)",
            ]

    # ---------- Fuse all parts ----------
    occ += [
        "if all_shapes:",
        "    result_shape = all_shapes[0]",
        "    for shp in all_shapes[1:]:",
        "        result_shape = BRepAlgoAPI_Fuse(result_shape, shp).Shape()",
        "else:",
        "    result_shape = None",
    ]
    return occ



def save_occ_code_to_file(occ_code, filename='1_occ.py', step_filename='output.step'):
    with open('from_import.py', 'r', encoding='utf-8') as file:
        import_code = file.read()

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(import_code + '\n')
        for line in occ_code:
            file.write(line + '\n')

        file.write(f"\n# Saving the model to STEP file\n")
        file.write(f"if result_shape:\n")
        file.write(f"    step_writer = STEPControl_Writer()\n")
        file.write(f"    step_writer.Transfer(result_shape, STEPControl_AsIs)\n")
        file.write(f"    status = step_writer.Write('{step_filename}')\n")
        file.write(f"    if status == 1:\n")
        file.write(f"        print('STEP file saved successfully as {step_filename}')\n")
        file.write(f"    else:\n")
        file.write(f"        print('Error occurred while saving the STEP file')\n")

        file.write(f"\n# Display the shape in a window\n")
        file.write(f"if __name__ == '__main__':\n")
        file.write(f"    from OCC.Display.SimpleGui import init_display\n")
        file.write(f"    display, start_display, *_ = init_display()\n")
        file.write(f"    if result_shape:\n")
        file.write(f"        display.DisplayShape(result_shape, update=True, quality=0.001)\n")
        file.write(f"        display.FitAll()\n")
        file.write(f"    start_display()\n")

    print(f"PythonOCC code has been saved to {filename} and STEP file saved as {step_filename}")

def main():
    with open('00000073.json', 'r') as file:
        json_data = json.load(file)

    occ_code = generate_occ_code_from_json_v2(json_data)
    save_occ_code_to_file(occ_code)

if __name__ == '__main__':
    main()
