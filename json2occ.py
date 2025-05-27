import json
from OCC.Core.gp import gp_Pnt, gp_Dir, gp_Ax2, gp_Circ, gp_Vec
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire, BRepBuilderAPI_MakeFace
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakePrism
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse
from OCC.Core.STEPControl import STEPControl_Writer
from OCC.Core.TopoDS import TopoDS_Compound, TopoDS_Builder

def generate_occ_code_from_json(json_data):
    entities = json_data.get("entities", {})
    sequence = json_data.get("sequence", [])

    occ_code = []
    occ_code.append("from OCC.Core.gp import gp_Pnt, gp_Dir, gp_Ax2, gp_Circ, gp_Vec")
    occ_code.append("from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire, BRepBuilderAPI_MakeFace")
    occ_code.append("from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakePrism")
    occ_code.append("from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse")
    occ_code.append("from OCC.Core.TopoDS import TopoDS_Compound, TopoDS_Builder")

    occ_code.append("all_shapes = []  # 存储所有生成的 shape")

    for item in sequence:
        entity_type = item.get("type")
        entity_id = item.get("entity")

        if entity_type == "Sketch":
            sketch = entities.get(entity_id)
            if sketch:
                profiles = sketch.get("profiles", {})
                for profile_name, profile in profiles.items():
                    loops = profile.get("loops", [])
                    occ_code.append("edges = []")
                    for loop in loops:
                        if loop.get("is_outer"):
                            profile_curves = loop.get("profile_curves", [])
                            for curve in profile_curves:
                                if curve.get("type") == "Circle3D":
                                    center = curve.get("center_point", {})
                                    radius = curve.get("radius", 0.0) * 100
                                    occ_code.append(f"circle = gp_Circ(gp_Ax2(gp_Pnt({center.get('x', 0.0)*100}, {center.get('y', 0.0)*100}, {center.get('z', 0.0)*100}), gp_Dir(0.0, 0.0, 1.0)), {radius})")
                                    occ_code.append("edge = BRepBuilderAPI_MakeEdge(circle).Edge()")
                                    occ_code.append("edges.append(edge)")
                                elif curve.get("type") == "Line3D":
                                    start = curve.get("start_point", {})
                                    end = curve.get("end_point", {})
                                    start_x = start.get('x', 0.0) * 100
                                    start_y = start.get('y', 0.0) * 100
                                    start_z = start.get('z', 0.0) * 100
                                    end_x = end.get('x', 0.0) * 100
                                    end_y = end.get('y', 0.0) * 100
                                    end_z = end.get('z', 0.0) * 100
                                    occ_code.append(f"p1 = gp_Pnt({start_x}, {start_y}, {start_z})")
                                    occ_code.append(f"p2 = gp_Pnt({end_x}, {end_y}, {end_z})")
                                    occ_code.append("edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()")
                                    occ_code.append("edges.append(edge)")

                    occ_code.append("wire_maker = BRepBuilderAPI_MakeWire()")
                    occ_code.append("for e in edges:")
                    occ_code.append("    wire_maker.Add(e)")
                    occ_code.append("wire = wire_maker.Wire()")
                    occ_code.append("face = BRepBuilderAPI_MakeFace(wire).Face()")

        elif entity_type == "ExtrudeFeature":
            extrude_feature = entities.get(entity_id)
            if extrude_feature:
                extent_type = extrude_feature.get("extent_type", "OneSideFeatureExtentType")
                extent_one = extrude_feature.get("extent_one", {}).get("distance", {}).get("value", 0.0) * 100
                extent_two = extrude_feature.get("extent_two", {}).get("distance", {}).get("value", 0.0) * 100

                if extent_type == "OneSideFeatureExtentType":
                    occ_code.append(f"extruded_shape = BRepPrimAPI_MakePrism(face, gp_Vec(0.0, 0.0, 1.0) * {extent_one}).Shape()")
                elif extent_type == "TwoSideFeatureExtentType":
                    occ_code.append(f"extrude_one = BRepPrimAPI_MakePrism(face, gp_Vec(0.0, 0.0, 1.0) * {extent_one}).Shape()")
                    occ_code.append(f"extrude_two = BRepPrimAPI_MakePrism(face, gp_Vec(0.0, 0.0, -1.0) * {extent_two}).Shape()")
                    occ_code.append("extruded_shape = BRepAlgoAPI_Fuse(extrude_one, extrude_two).Shape()")

                occ_code.append("all_shapes.append(extruded_shape)")

    # 合并所有 shapes（如果有多个）
    occ_code.append("if all_shapes:")
    occ_code.append("    result_shape = all_shapes[0]")
    occ_code.append("    for shape in all_shapes[1:]:")
    occ_code.append("        result_shape = BRepAlgoAPI_Fuse(result_shape, shape).Shape()")
    occ_code.append("else:")
    occ_code.append("    result_shape = None")

    return occ_code

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
    with open('00000272.json', 'r') as file:
        json_data = json.load(file)

    occ_code = generate_occ_code_from_json(json_data)
    save_occ_code_to_file(occ_code)

if __name__ == '__main__':
    main()
