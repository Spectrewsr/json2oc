# 基础几何模块
from OCC.Core.gp import gp_Pnt, gp_Vec, gp_Dir, gp_Ax2, gp_Circ, gp_Cylinder, gp_Sphere, gp_Torus, gp_Pln

# 修正版
from OCC.Core.gp import (
    gp_Pnt, gp_Dir, gp_Ax1, gp_Ax2,       # ← 加了 gp_Ax1
    gp_Circ, gp_Vec, gp_Trsf
)

# 几何对象构建
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire, BRepBuilderAPI_MakeFace, BRepBuilderAPI_MakeSolid

# 布尔运算
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse, BRepAlgoAPI_Cut, BRepAlgoAPI_Common

# 拉伸、旋转等操作
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakePrism, BRepPrimAPI_MakeCylinder, BRepPrimAPI_MakeSphere

# 拓扑和形状处理
from OCC.Core.TopAbs import TopAbs_SOLID, TopAbs_FACE, TopAbs_EDGE, TopAbs_VERTEX
from OCC.Core.TopoDS import TopoDS_Shape  # 仅导入 TopoDS_Shape，使用 topods_* 函数来转换形状

# 几何变换
from OCC.Core.gp import gp_Trsf, gp_GTrsf
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_Transform

# 文件操作（读写）
from OCC.Core.BRepTools import breptools_Read, breptools_Write

# 显示和调试（可视化）
from OCC.Display.SimpleGui import init_display

# 计算几何
from OCC.Core.BRepAdaptor import BRepAdaptor_Surface

# 网格（Mesh）操作
from OCC.Core.StlAPI import StlAPI_Writer, StlAPI_Reader

# 几何约束
from OCC.Core.Geom import Geom_Line, Geom_Circle, Geom_Ellipse

# 形状修改
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_ModifyShape

from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs


from OCC.Core.gp import (gp_Pnt, gp_Dir, gp_Ax1, gp_Ax2, gp_Circ, gp_Vec, gp_Trsf)
from OCC.Core.GC import GC_MakeArcOfCircle
from OCC.Core.BRepBuilderAPI import (
    BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire,
    BRepBuilderAPI_MakeFace, BRepBuilderAPI_Transform
)
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakePrism
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse
from OCC.Core.STEPControl import STEPControl_AsIs

all_shapes = []  # 存储每个 part 的体
wires = []
edges = []
p1 = gp_Pnt(0.0, 0.0, 0.0)
p2 = gp_Pnt(56.25, 0.0, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(56.25, 0.0, 0.0)
p2 = gp_Pnt(56.25, 11.7225, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(56.25, 11.7225, 0.0)
p2 = gp_Pnt(0.0, 11.7225, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(0.0, 11.7225, 0.0)
p2 = gp_Pnt(0.0, 0.0, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
edges = []
circ = gp_Circ(gp_Ax2(gp_Pnt(2.8125, 5.8575, 0.0), gp_Dir(0,0,1)), 1.0050000000000001)
edge = BRepBuilderAPI_MakeEdge(circ).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
edges = []
p1 = gp_Pnt(18.75, 2.3475, 0.0)
p2 = gp_Pnt(37.5, 2.3475, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(37.5, 2.3475, 0.0)
p2 = gp_Pnt(41.017500000000005, 5.8575, 0.0)
p3 = gp_Pnt(37.5, 9.375, 0.0)
curve = GC_MakeArcOfCircle(p1, p2, p3).Value()
edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
edges.append(edge)
p1 = gp_Pnt(37.5, 9.375, 0.0)
p2 = gp_Pnt(18.75, 9.375, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(18.75, 9.375, 0.0)
p2 = gp_Pnt(15.232499999999998, 5.8575, 0.0)
p3 = gp_Pnt(18.75, 2.3475, 0.0)
curve = GC_MakeArcOfCircle(p1, p2, p3).Value()
edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
edges = []
circ = gp_Circ(gp_Ax2(gp_Pnt(53.4375, 5.8875, 0.0), gp_Dir(0,0,1)), 1.0050000000000001)
edge = BRepBuilderAPI_MakeEdge(circ).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
outer = wires[0]
face_mkr = BRepBuilderAPI_MakeFace(outer)
for hole_w in wires[1:]: face_mkr.Add(hole_w)
face = face_mkr.Face()
extruded = BRepPrimAPI_MakePrism(face, gp_Vec(0,0,1)*1.5599999999999998).Shape()
trsf = gp_Trsf(); trsf.SetTranslation(gp_Vec(0.0,0.0,0.0))
rot  = gp_Trsf(); rot.SetRotation(gp_Ax1(gp_Pnt(0,0,0), gp_Dir(0,0,1)), 0.0)
rot.Multiply(trsf)
extruded = BRepBuilderAPI_Transform(extruded, rot, True).Shape()
all_shapes.append(extruded)
if all_shapes:
    result_shape = all_shapes[0]
    for shp in all_shapes[1:]:
        result_shape = BRepAlgoAPI_Fuse(result_shape, shp).Shape()
else:
    result_shape = None

# Saving the model to STEP file
if result_shape:
    step_writer = STEPControl_Writer()
    step_writer.Transfer(result_shape, STEPControl_AsIs)
    status = step_writer.Write('output.step')
    if status == 1:
        print('STEP file saved successfully as output.step')
    else:
        print('Error occurred while saving the STEP file')

# Display the shape in a window
if __name__ == '__main__':
    from OCC.Display.SimpleGui import init_display
    display, start_display, *_ = init_display()
    if result_shape:
        display.DisplayShape(result_shape, update=True, quality=0.001)
        display.FitAll()
    start_display()
