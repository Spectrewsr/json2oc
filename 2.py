# fusion_circle_extrude.py
# 需要 pythonocc-core ≥ 7.7.0
from OCC.Core.gp import gp_Pnt, gp_Dir, gp_Ax2, gp_Vec, gp_Circ
from OCC.Core.BRepBuilderAPI import (
    BRepBuilderAPI_MakeEdge,
    BRepBuilderAPI_MakeWire,
    BRepBuilderAPI_MakeFace,
)
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakePrism
from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs
from OCC.Core.IFSelect import IFSelect_RetDone
from OCC.Display.SimpleGui import init_display
from math import pi, cos, sin
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeCylinder, BRepPrimAPI_MakePrism
from OCC.Core.BRepBuilderAPI import (
    BRepBuilderAPI_MakeWire,
    BRepBuilderAPI_MakeEdge,
    BRepBuilderAPI_MakeFace,
    BRepBuilderAPI_Transform
)
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse
from OCC.Core.BRepOffsetAPI import BRepOffsetAPI_MakePipeShell
from OCC.Core.TopoDS import TopoDS_Shape, TopoDS_Compound, topods
from OCC.Core.gp import gp_Pnt, gp_Vec, gp_Trsf, gp_Ax2, gp_Dir, gp_Ax3
from OCC.Core.Geom import Geom_Circle
from OCC.Core.GeomAPI import GeomAPI_PointsToBSpline
from OCC.Core.TColgp import TColgp_Array1OfPnt
from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs
from OCC.Core.Interface import Interface_Static_SetCVal
from OCC.Core.BRep import BRep_Builder
from OCC.Core.TopExp import TopExp_Explorer
from OCC.Core.TopAbs import TopAbs_EDGE
from OCC.Core.ShapeFix import ShapeFix_Shape



# ── 参数（米） ────────────────────────────────────────────────────────────────
RADIUS = 91     # 圆半径 ≈ 91 mm
HEIGHT = 25         # 拉伸高度 25.4 mm（1 inch）


# ── 草图 → 面 ─────────────────────────────────────────────────────────────────
circle_geom = gp_Circ(gp_Ax2(gp_Pnt(0, 0, 0), gp_Dir(0, 0, 1)), RADIUS)

edge = BRepBuilderAPI_MakeEdge(circle_geom).Edge()
wire = BRepBuilderAPI_MakeWire(edge).Wire()
face = BRepBuilderAPI_MakeFace(wire).Face()        # “Profile”


# ── 拉伸 ─────────────────────────────────────────────────────────────────────
vec = gp_Vec(0, 0, HEIGHT)
solid = BRepPrimAPI_MakePrism(face, vec).Shape()


import os
from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs
from OCC.Core.IFSelect import IFSelect_RetDone
from OCC.Core.Interface import Interface_Static_SetCVal, Interface_Static_SetRVal

def export_step(shape: TopoDS_Shape, filename="circle_extrude.step"):
    # 确保文件名有 .step 后缀
    if not filename.lower().endswith(".step"):
        filename += ".step"

    writer = STEPControl_Writer()

    # 设置制造友好的导出参数
    Interface_Static_SetCVal("write.step.schema", "AP203")  # 可选: 用 AP203 标准
    Interface_Static_SetCVal("write.step.unit", "MM")
    Interface_Static_SetCVal("write.step.precision.mode", "User")
    Interface_Static_SetRVal("write.step.precision.val", 0.001)

    # 传递形状
    transfer_status = writer.Transfer(shape, STEPControl_AsIs)
    if transfer_status != 1:
        print("❌ STEP Transfer 失败")
        return

    # 写入文件
    write_status = writer.Write(filename)
    if write_status == IFSelect_RetDone:
        abs_path = os.path.abspath(filename)
        print(f"✅ STEP 文件已保存: {abs_path}")
    else:
        print("❌ STEP 写入失败")
from OCC.Core.BRepMesh import BRepMesh_IncrementalMesh

# 0.0005 = 0.5 mm 线性偏差
BRepMesh_IncrementalMesh(solid, 0.0005, True, 0.5, True)
export_step(solid)      # 再导出



# ── (可选) 显示窗口 ──────────────────────────────────────────────────────────
if __name__ == "__main__":
    display, start_display, *_ = init_display()
    display.DisplayShape(solid, update=True)
    display.FitAll()
    start_display()


