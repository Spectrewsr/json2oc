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
p1 = gp_Pnt(0.0, 6.802559999999999, 0.0)
p2 = gp_Pnt(0.203132, 6.358504, 0.0)
p3 = gp_Pnt(0.420436, 5.919172, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(0.420436, 5.919172, 0.0)
p2 = gp_Pnt(4.780688, 8.43234, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(4.780688, 8.43234, 0.0)
p2 = gp_Pnt(5.33812, 8.323688, 0.0)
p3 = gp_Pnt(5.2058480000000005, 7.77098, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(5.2058480000000005, 7.77098, 0.0)
p2 = gp_Pnt(0.812528, 5.238916, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(0.812528, 5.238916, 0.0)
p2 = gp_Pnt(1.081796, 4.827928, 0.0)
p3 = gp_Pnt(1.36996, 4.431112, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(1.36996, 4.431112, 0.0)
p2 = gp_Pnt(6.372675999999999, 4.388596, 0.0)
p3 = gp_Pnt(8.909463999999998, 0.075584, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(8.909463999999998, 0.075584, 0.0)
p2 = gp_Pnt(9.40076, 0.028343999999999998, 0.0)
p3 = gp_Pnt(9.887332, 0.0, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(9.887332, 0.0, 0.0)
p2 = gp_Pnt(9.887332, 5.03106, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(9.887332, 5.03106, 0.0)
p2 = gp_Pnt(10.260527999999999, 5.460944, 0.0)
p3 = gp_Pnt(10.67624, 5.068852, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(10.67624, 5.068852, 0.0)
p2 = gp_Pnt(10.67624, 0.0, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(10.67624, 0.0, 0.0)
p2 = gp_Pnt(11.162811999999999, 0.028343999999999998, 0.0)
p3 = gp_Pnt(11.649384, 0.075584, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(11.649384, 0.075584, 0.0)
p2 = gp_Pnt(14.186172, 4.388596, 0.0)
p3 = gp_Pnt(19.193611999999998, 4.431112, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(19.193611999999998, 4.431112, 0.0)
p2 = gp_Pnt(19.198335999999998, 4.435836, 0.0)
p3 = gp_Pnt(19.203059999999997, 4.445284, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(19.203059999999997, 4.445284, 0.0)
p2 = gp_Pnt(17.686656, 5.612112, 0.0)
p3 = gp_Pnt(16.500932, 7.114344, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(16.500932, 7.114344, 0.0)
p2 = gp_Pnt(15.390791999999998, 7.7568079999999995, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(15.390791999999998, 7.7568079999999995, 0.0)
p2 = gp_Pnt(15.206556, 8.295344, 0.0)
p3 = gp_Pnt(15.749815999999997, 8.45596, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(15.749815999999997, 8.45596, 0.0)
p2 = gp_Pnt(15.882088, 8.375652, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(15.882088, 8.375652, 0.0)
p2 = gp_Pnt(15.371896000000001, 11.158088, 0.0)
p3 = gp_Pnt(15.882088, 13.940523999999998, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(15.882088, 13.940523999999998, 0.0)
p2 = gp_Pnt(15.782884, 13.879112, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(15.782884, 13.879112, 0.0)
p2 = gp_Pnt(15.225451999999997, 13.992488, 0.0)
p3 = gp_Pnt(15.357724000000001, 14.545195999999999, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(15.357724000000001, 14.545195999999999, 0.0)
p2 = gp_Pnt(16.500932, 15.206556, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(16.500932, 15.206556, 0.0)
p2 = gp_Pnt(17.686656, 16.704064000000002, 0.0)
p3 = gp_Pnt(19.203059999999997, 17.870891999999998, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(19.203059999999997, 17.870891999999998, 0.0)
p2 = gp_Pnt(19.198335999999998, 17.88034, 0.0)
p3 = gp_Pnt(19.193611999999998, 17.885063999999996, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(19.193611999999998, 17.885063999999996, 0.0)
p2 = gp_Pnt(14.186172, 17.92758, 0.0)
p3 = gp_Pnt(11.649384, 22.240592, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(11.649384, 22.240592, 0.0)
p2 = gp_Pnt(11.162811999999999, 22.287831999999998, 0.0)
p3 = gp_Pnt(10.671515999999999, 22.316176, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(10.671515999999999, 22.316176, 0.0)
p2 = gp_Pnt(10.671515999999999, 17.285116000000002, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(10.671515999999999, 17.285116000000002, 0.0)
p2 = gp_Pnt(10.29832, 16.855232, 0.0)
p3 = gp_Pnt(9.887332, 17.247324, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(9.887332, 17.247324, 0.0)
p2 = gp_Pnt(9.887332, 22.316176, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(9.887332, 22.316176, 0.0)
p2 = gp_Pnt(9.396035999999999, 22.287831999999998, 0.0)
p3 = gp_Pnt(8.909463999999998, 22.240592, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(8.909463999999998, 22.240592, 0.0)
p2 = gp_Pnt(6.372675999999999, 17.92758, 0.0)
p3 = gp_Pnt(1.36996, 17.885063999999996, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(1.36996, 17.885063999999996, 0.0)
p2 = gp_Pnt(1.081796, 17.488248, 0.0)
p3 = gp_Pnt(0.812528, 17.07726, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(0.812528, 17.07726, 0.0)
p2 = gp_Pnt(5.1727799999999995, 14.559367999999997, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(5.1727799999999995, 14.559367999999997, 0.0)
p2 = gp_Pnt(5.357016, 14.020832, 0.0)
p3 = gp_Pnt(4.809032, 13.860216, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(4.809032, 13.860216, 0.0)
p2 = gp_Pnt(0.420436, 16.397004000000003, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(0.420436, 16.397004000000003, 0.0)
p2 = gp_Pnt(0.19840799999999997, 15.957671999999997, 0.0)
p3 = gp_Pnt(0.0, 15.513615999999999, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(0.0, 15.513615999999999, 0.0)
p2 = gp_Pnt(2.4659280000000003, 11.158088, 0.0)
p3 = gp_Pnt(0.0, 6.802559999999999, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
edges = []
circ = gp_Circ(gp_Ax2(gp_Pnt(10.279424, 11.158088, 0.0), gp_Dir(0,0,1)), 4.331908)
edge = BRepBuilderAPI_MakeEdge(circ).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
outer = wires[0]
face_mkr = BRepBuilderAPI_MakeFace(outer)
for hole_w in wires[1:]: face_mkr.Add(hole_w)
face = face_mkr.Face()
extruded = BRepPrimAPI_MakePrism(face, gp_Vec(0,0,1)*13.11).Shape()
trsf = gp_Trsf(); trsf.SetTranslation(gp_Vec(2.29,2.59,15.73))
rot  = gp_Trsf(); rot.SetRotation(gp_Ax1(gp_Pnt(0,0,0), gp_Dir(0,0,1)), 0.0)
rot.Multiply(trsf)
extruded = BRepBuilderAPI_Transform(extruded, rot, True).Shape()
all_shapes.append(extruded)
wires = []
edges = []
p1 = gp_Pnt(0.0, 6.802559999999999, 0.0)
p2 = gp_Pnt(0.203132, 6.358504, 0.0)
p3 = gp_Pnt(0.420436, 5.919172, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(0.420436, 5.919172, 0.0)
p2 = gp_Pnt(4.780688, 8.43234, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(4.780688, 8.43234, 0.0)
p2 = gp_Pnt(5.33812, 8.323688, 0.0)
p3 = gp_Pnt(5.2058480000000005, 7.77098, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(5.2058480000000005, 7.77098, 0.0)
p2 = gp_Pnt(0.812528, 5.238916, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(0.812528, 5.238916, 0.0)
p2 = gp_Pnt(1.081796, 4.827928, 0.0)
p3 = gp_Pnt(1.36996, 4.431112, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(1.36996, 4.431112, 0.0)
p2 = gp_Pnt(6.372675999999999, 4.388596, 0.0)
p3 = gp_Pnt(8.909463999999998, 0.075584, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(8.909463999999998, 0.075584, 0.0)
p2 = gp_Pnt(9.40076, 0.028343999999999998, 0.0)
p3 = gp_Pnt(9.887332, 0.0, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(9.887332, 0.0, 0.0)
p2 = gp_Pnt(9.887332, 5.03106, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(9.887332, 5.03106, 0.0)
p2 = gp_Pnt(10.260527999999999, 5.460944, 0.0)
p3 = gp_Pnt(10.67624, 5.068852, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(10.67624, 5.068852, 0.0)
p2 = gp_Pnt(10.67624, 0.0, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(10.67624, 0.0, 0.0)
p2 = gp_Pnt(11.162811999999999, 0.028343999999999998, 0.0)
p3 = gp_Pnt(11.649384, 0.075584, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(11.649384, 0.075584, 0.0)
p2 = gp_Pnt(14.186172, 4.388596, 0.0)
p3 = gp_Pnt(19.193611999999998, 4.431112, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(19.193611999999998, 4.431112, 0.0)
p2 = gp_Pnt(19.198335999999998, 4.435836, 0.0)
p3 = gp_Pnt(19.203059999999997, 4.445284, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(19.203059999999997, 4.445284, 0.0)
p2 = gp_Pnt(17.686656, 5.612112, 0.0)
p3 = gp_Pnt(16.500932, 7.114344, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(16.500932, 7.114344, 0.0)
p2 = gp_Pnt(15.390791999999998, 7.7568079999999995, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(15.390791999999998, 7.7568079999999995, 0.0)
p2 = gp_Pnt(15.206556, 8.295344, 0.0)
p3 = gp_Pnt(15.749815999999997, 8.45596, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(15.749815999999997, 8.45596, 0.0)
p2 = gp_Pnt(15.882088, 8.375652, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(15.882088, 8.375652, 0.0)
p2 = gp_Pnt(15.371896000000001, 11.158088, 0.0)
p3 = gp_Pnt(15.882088, 13.940523999999998, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(15.882088, 13.940523999999998, 0.0)
p2 = gp_Pnt(15.782884, 13.879112, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(15.782884, 13.879112, 0.0)
p2 = gp_Pnt(15.225451999999997, 13.992488, 0.0)
p3 = gp_Pnt(15.357724000000001, 14.545195999999999, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(15.357724000000001, 14.545195999999999, 0.0)
p2 = gp_Pnt(16.500932, 15.206556, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(16.500932, 15.206556, 0.0)
p2 = gp_Pnt(17.686656, 16.704064000000002, 0.0)
p3 = gp_Pnt(19.203059999999997, 17.870891999999998, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(19.203059999999997, 17.870891999999998, 0.0)
p2 = gp_Pnt(19.198335999999998, 17.88034, 0.0)
p3 = gp_Pnt(19.193611999999998, 17.885063999999996, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(19.193611999999998, 17.885063999999996, 0.0)
p2 = gp_Pnt(14.186172, 17.92758, 0.0)
p3 = gp_Pnt(11.649384, 22.240592, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(11.649384, 22.240592, 0.0)
p2 = gp_Pnt(11.162811999999999, 22.287831999999998, 0.0)
p3 = gp_Pnt(10.671515999999999, 22.316176, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(10.671515999999999, 22.316176, 0.0)
p2 = gp_Pnt(10.671515999999999, 17.285116000000002, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(10.671515999999999, 17.285116000000002, 0.0)
p2 = gp_Pnt(10.29832, 16.855232, 0.0)
p3 = gp_Pnt(9.887332, 17.247324, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(9.887332, 17.247324, 0.0)
p2 = gp_Pnt(9.887332, 22.316176, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(9.887332, 22.316176, 0.0)
p2 = gp_Pnt(9.396035999999999, 22.287831999999998, 0.0)
p3 = gp_Pnt(8.909463999999998, 22.240592, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(8.909463999999998, 22.240592, 0.0)
p2 = gp_Pnt(6.372675999999999, 17.92758, 0.0)
p3 = gp_Pnt(1.36996, 17.885063999999996, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(1.36996, 17.885063999999996, 0.0)
p2 = gp_Pnt(1.081796, 17.488248, 0.0)
p3 = gp_Pnt(0.812528, 17.07726, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(0.812528, 17.07726, 0.0)
p2 = gp_Pnt(5.1727799999999995, 14.559367999999997, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(5.1727799999999995, 14.559367999999997, 0.0)
p2 = gp_Pnt(5.357016, 14.020832, 0.0)
p3 = gp_Pnt(4.809032, 13.860216, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(4.809032, 13.860216, 0.0)
p2 = gp_Pnt(0.420436, 16.397004000000003, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(0.420436, 16.397004000000003, 0.0)
p2 = gp_Pnt(0.19840799999999997, 15.957671999999997, 0.0)
p3 = gp_Pnt(0.0, 15.513615999999999, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(0.0, 15.513615999999999, 0.0)
p2 = gp_Pnt(2.4659280000000003, 11.158088, 0.0)
p3 = gp_Pnt(0.0, 6.802559999999999, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
edges = []
circ = gp_Circ(gp_Ax2(gp_Pnt(10.279424, 11.158088, 0.0), gp_Dir(0,0,1)), 4.331908)
edge = BRepBuilderAPI_MakeEdge(circ).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
outer = wires[0]
face_mkr = BRepBuilderAPI_MakeFace(outer)
for hole_w in wires[1:]: face_mkr.Add(hole_w)
face = face_mkr.Face()
extruded = BRepPrimAPI_MakePrism(face, gp_Vec(0,0,1)*13.11).Shape()
trsf = gp_Trsf(); trsf.SetTranslation(gp_Vec(2.29,2.59,15.73))
rot  = gp_Trsf(); rot.SetRotation(gp_Ax1(gp_Pnt(0,0,0), gp_Dir(0,0,1)), 0.0)
rot.Multiply(trsf)
extruded = BRepBuilderAPI_Transform(extruded, rot, True).Shape()
all_shapes.append(extruded)
wires = []
edges = []
circ = gp_Circ(gp_Ax2(gp_Pnt(10.279424, 11.158088, 0.0), gp_Dir(0,0,1)), 4.331908)
edge = BRepBuilderAPI_MakeEdge(circ).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
edges = []
circ = gp_Circ(gp_Ax2(gp_Pnt(10.279424, 11.158088, 0.0), gp_Dir(0,0,1)), 1.2376880000000001)
edge = BRepBuilderAPI_MakeEdge(circ).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
outer = wires[0]
face_mkr = BRepBuilderAPI_MakeFace(outer)
for hole_w in wires[1:]: face_mkr.Add(hole_w)
face = face_mkr.Face()
extruded = BRepPrimAPI_MakePrism(face, gp_Vec(0,0,1)*13.11).Shape()
trsf = gp_Trsf(); trsf.SetTranslation(gp_Vec(2.29,2.59,15.73))
rot  = gp_Trsf(); rot.SetRotation(gp_Ax1(gp_Pnt(0,0,0), gp_Dir(0,0,1)), 0.0)
rot.Multiply(trsf)
extruded = BRepBuilderAPI_Transform(extruded, rot, True).Shape()
all_shapes.append(extruded)
wires = []
edges = []
p1 = gp_Pnt(15.882088, 8.375652, 0.0)
p2 = gp_Pnt(20.138412, 5.919172, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(20.138412, 5.919172, 0.0)
p2 = gp_Pnt(20.36044, 6.358504, 0.0)
p3 = gp_Pnt(20.563572, 6.802559999999999, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(20.563572, 6.802559999999999, 0.0)
p2 = gp_Pnt(18.097644, 11.158088, 0.0)
p3 = gp_Pnt(20.563572, 15.513615999999999, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(20.563572, 15.513615999999999, 0.0)
p2 = gp_Pnt(20.36044, 15.957671999999997, 0.0)
p3 = gp_Pnt(20.138412, 16.397004000000003, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(20.138412, 16.397004000000003, 0.0)
p2 = gp_Pnt(15.882088, 13.940523999999998, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(15.882088, 13.940523999999998, 0.0)
p2 = gp_Pnt(15.371896000000001, 11.158088, 0.0)
p3 = gp_Pnt(15.882088, 8.375652, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
outer = wires[0]
face_mkr = BRepBuilderAPI_MakeFace(outer)
for hole_w in wires[1:]: face_mkr.Add(hole_w)
face = face_mkr.Face()
extruded = BRepPrimAPI_MakePrism(face, gp_Vec(0,0,1)*13.11).Shape()
trsf = gp_Trsf(); trsf.SetTranslation(gp_Vec(2.29,2.59,15.73))
rot  = gp_Trsf(); rot.SetRotation(gp_Ax1(gp_Pnt(0,0,0), gp_Dir(0,0,1)), 0.0)
rot.Multiply(trsf)
extruded = BRepBuilderAPI_Transform(extruded, rot, True).Shape()
all_shapes.append(extruded)
wires = []
edges = []
p1 = gp_Pnt(16.500932, 7.114344, 0.0)
p2 = gp_Pnt(17.686656, 5.612112, 0.0)
p3 = gp_Pnt(19.203059999999997, 4.445284, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(19.203059999999997, 4.445284, 0.0)
p2 = gp_Pnt(19.481775999999996, 4.837376, 0.0)
p3 = gp_Pnt(19.746319999999997, 5.238916, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(19.746319999999997, 5.238916, 0.0)
p2 = gp_Pnt(16.500932, 7.114344, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
outer = wires[0]
face_mkr = BRepBuilderAPI_MakeFace(outer)
for hole_w in wires[1:]: face_mkr.Add(hole_w)
face = face_mkr.Face()
extruded = BRepPrimAPI_MakePrism(face, gp_Vec(0,0,1)*13.11).Shape()
trsf = gp_Trsf(); trsf.SetTranslation(gp_Vec(2.29,2.59,15.73))
rot  = gp_Trsf(); rot.SetRotation(gp_Ax1(gp_Pnt(0,0,0), gp_Dir(0,0,1)), 0.0)
rot.Multiply(trsf)
extruded = BRepBuilderAPI_Transform(extruded, rot, True).Shape()
all_shapes.append(extruded)
wires = []
edges = []
p1 = gp_Pnt(16.500932, 15.206556, 0.0)
p2 = gp_Pnt(19.746319999999997, 17.07726, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(19.746319999999997, 17.07726, 0.0)
p2 = gp_Pnt(19.481775999999996, 17.4788, 0.0)
p3 = gp_Pnt(19.203059999999997, 17.870891999999998, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(19.203059999999997, 17.870891999999998, 0.0)
p2 = gp_Pnt(17.686656, 16.704064000000002, 0.0)
p3 = gp_Pnt(16.500932, 15.206556, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
outer = wires[0]
face_mkr = BRepBuilderAPI_MakeFace(outer)
for hole_w in wires[1:]: face_mkr.Add(hole_w)
face = face_mkr.Face()
extruded = BRepPrimAPI_MakePrism(face, gp_Vec(0,0,1)*13.11).Shape()
trsf = gp_Trsf(); trsf.SetTranslation(gp_Vec(2.29,2.59,15.73))
rot  = gp_Trsf(); rot.SetRotation(gp_Ax1(gp_Pnt(0,0,0), gp_Dir(0,0,1)), 0.0)
rot.Multiply(trsf)
extruded = BRepBuilderAPI_Transform(extruded, rot, True).Shape()
all_shapes.append(extruded)
wires = []
edges = []
p1 = gp_Pnt(0.0, 1.921374, 0.0)
p2 = gp_Pnt(0.28917, 0.818244, 0.0)
p3 = gp_Pnt(1.0838519999999998, 0.0, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(1.0838519999999998, 0.0, 0.0)
p2 = gp_Pnt(1.3923, 1.0817100000000002, 0.0)
p3 = gp_Pnt(1.454418, 2.2041180000000002, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(1.454418, 2.2041180000000002, 0.0)
p2 = gp_Pnt(0.741132, 1.994202, 0.0)
p3 = gp_Pnt(0.0, 1.921374, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
outer = wires[0]
face_mkr = BRepBuilderAPI_MakeFace(outer)
for hole_w in wires[1:]: face_mkr.Add(hole_w)
face = face_mkr.Face()
extruded = BRepPrimAPI_MakePrism(face, gp_Vec(0,0,1)*13.11).Shape()
trsf = gp_Trsf(); trsf.SetTranslation(gp_Vec(40.86,17.24,15.73))
rot  = gp_Trsf(); rot.SetRotation(gp_Ax1(gp_Pnt(0,0,0), gp_Dir(0,0,1)), 0.0)
rot.Multiply(trsf)
extruded = BRepBuilderAPI_Transform(extruded, rot, True).Shape()
all_shapes.append(extruded)
wires = []
edges = []
p1 = gp_Pnt(0.649026, 4.373964, 0.0)
p2 = gp_Pnt(0.783972, 4.453218, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(0.783972, 4.453218, 0.0)
p2 = gp_Pnt(0.745416, 4.521762, 0.0)
p3 = gp_Pnt(0.704718, 4.588164, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(0.704718, 4.588164, 0.0)
p2 = gp_Pnt(0.63189, 4.4917739999999995, 0.0)
p3 = gp_Pnt(0.649026, 4.373964, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
outer = wires[0]
face_mkr = BRepBuilderAPI_MakeFace(outer)
for hole_w in wires[1:]: face_mkr.Add(hole_w)
face = face_mkr.Face()
extruded = BRepPrimAPI_MakePrism(face, gp_Vec(0,0,1)*13.11).Shape()
trsf = gp_Trsf(); trsf.SetTranslation(gp_Vec(40.86,17.24,15.73))
rot  = gp_Trsf(); rot.SetRotation(gp_Ax1(gp_Pnt(0,0,0), gp_Dir(0,0,1)), 0.0)
rot.Multiply(trsf)
extruded = BRepBuilderAPI_Transform(extruded, rot, True).Shape()
all_shapes.append(extruded)
wires = []
edges = []
p1 = gp_Pnt(0.649026, 4.373964, 0.0)
p2 = gp_Pnt(0.743274, 4.301136, 0.0)
p3 = gp_Pnt(0.861084, 4.31613, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(0.861084, 4.31613, 0.0)
p2 = gp_Pnt(0.8225279999999999, 4.384674, 0.0)
p3 = gp_Pnt(0.783972, 4.453218, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(0.783972, 4.453218, 0.0)
p2 = gp_Pnt(0.649026, 4.373964, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
outer = wires[0]
face_mkr = BRepBuilderAPI_MakeFace(outer)
for hole_w in wires[1:]: face_mkr.Add(hole_w)
face = face_mkr.Face()
extruded = BRepPrimAPI_MakePrism(face, gp_Vec(0,0,1)*13.11).Shape()
trsf = gp_Trsf(); trsf.SetTranslation(gp_Vec(40.86,17.24,15.73))
rot  = gp_Trsf(); rot.SetRotation(gp_Ax1(gp_Pnt(0,0,0), gp_Dir(0,0,1)), 0.0)
rot.Multiply(trsf)
extruded = BRepBuilderAPI_Transform(extruded, rot, True).Shape()
all_shapes.append(extruded)
wires = []
edges = []
p1 = gp_Pnt(0.704718, 4.588164, 0.0)
p2 = gp_Pnt(0.783972, 4.453218, 0.0)
p3 = gp_Pnt(0.861084, 4.31613, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(0.861084, 4.31613, 0.0)
p2 = gp_Pnt(0.92106, 4.532472, 0.0)
p3 = gp_Pnt(0.704718, 4.588164, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
outer = wires[0]
face_mkr = BRepBuilderAPI_MakeFace(outer)
for hole_w in wires[1:]: face_mkr.Add(hole_w)
face = face_mkr.Face()
extruded = BRepPrimAPI_MakePrism(face, gp_Vec(0,0,1)*13.11).Shape()
trsf = gp_Trsf(); trsf.SetTranslation(gp_Vec(40.86,17.24,15.73))
rot  = gp_Trsf(); rot.SetRotation(gp_Ax1(gp_Pnt(0,0,0), gp_Dir(0,0,1)), 0.0)
rot.Multiply(trsf)
extruded = BRepBuilderAPI_Transform(extruded, rot, True).Shape()
all_shapes.append(extruded)
wires = []
edges = []
p1 = gp_Pnt(1.0838519999999998, 0.0, 0.0)
p2 = gp_Pnt(4.179042, 0.779688, 0.0)
p3 = gp_Pnt(3.369366, 3.86631, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(3.369366, 3.86631, 0.0)
p2 = gp_Pnt(2.5511220000000003, 2.8745640000000003, 0.0)
p3 = gp_Pnt(1.454418, 2.2041180000000002, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(1.454418, 2.2041180000000002, 0.0)
p2 = gp_Pnt(1.3923, 1.0817100000000002, 0.0)
p3 = gp_Pnt(1.0838519999999998, 0.0, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
edges = []
circ = gp_Circ(gp_Ax2(gp_Pnt(2.2469580000000002, 1.9213740000000001, 0.0), gp_Dir(0,0,1)), 0.561204)
edge = BRepBuilderAPI_MakeEdge(circ).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
outer = wires[0]
face_mkr = BRepBuilderAPI_MakeFace(outer)
for hole_w in wires[1:]: face_mkr.Add(hole_w)
face = face_mkr.Face()
extruded = BRepPrimAPI_MakePrism(face, gp_Vec(0,0,1)*13.11).Shape()
trsf = gp_Trsf(); trsf.SetTranslation(gp_Vec(40.86,17.24,15.73))
rot  = gp_Trsf(); rot.SetRotation(gp_Ax1(gp_Pnt(0,0,0), gp_Dir(0,0,1)), 0.0)
rot.Multiply(trsf)
extruded = BRepBuilderAPI_Transform(extruded, rot, True).Shape()
all_shapes.append(extruded)
wires = []
edges = []
p1 = gp_Pnt(0.35672400000000004, 2.7513989999999997, 0.0)
p2 = gp_Pnt(3.33603, 1.033839, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(3.33603, 1.033839, 0.0)
p2 = gp_Pnt(3.4879679999999995, 1.337715, 0.0)
p3 = gp_Pnt(3.6299969999999995, 1.6514999999999997, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(3.6299969999999995, 1.6514999999999997, 0.0)
p2 = gp_Pnt(1.9058309999999998, 4.693563, 0.0)
p3 = gp_Pnt(3.6299969999999995, 7.738929, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(3.6299969999999995, 7.738929, 0.0)
p2 = gp_Pnt(3.4879679999999995, 8.052714, 0.0)
p3 = gp_Pnt(3.3327269999999998, 8.359893, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(3.3327269999999998, 8.359893, 0.0)
p2 = gp_Pnt(0.360027, 6.63903, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(0.360027, 6.63903, 0.0)
p2 = gp_Pnt(0.0, 4.696866, 0.0)
p3 = gp_Pnt(0.35672400000000004, 2.7513989999999997, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
outer = wires[0]
face_mkr = BRepBuilderAPI_MakeFace(outer)
for hole_w in wires[1:]: face_mkr.Add(hole_w)
face = face_mkr.Face()
extruded = BRepPrimAPI_MakePrism(face, gp_Vec(0,0,-1)*7.86).Shape()
trsf = gp_Trsf(); trsf.SetTranslation(gp_Vec(34.83,12.0,15.73))
rot  = gp_Trsf(); rot.SetRotation(gp_Ax1(gp_Pnt(0,0,0), gp_Dir(0,0,1)), 0.0)
rot.Multiply(trsf)
extruded = BRepBuilderAPI_Transform(extruded, rot, True).Shape()
all_shapes.append(extruded)
wires = []
edges = []
p1 = gp_Pnt(0.35672400000000004, 2.7513989999999997, 0.0)
p2 = gp_Pnt(0.554904, 2.298888, 0.0)
p3 = gp_Pnt(0.789417, 1.866195, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(0.789417, 1.866195, 0.0)
p2 = gp_Pnt(3.058578, 0.5582069999999999, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(3.058578, 0.5582069999999999, 0.0)
p2 = gp_Pnt(3.2006069999999998, 0.7927200000000001, 0.0)
p3 = gp_Pnt(3.33603, 1.033839, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(3.33603, 1.033839, 0.0)
p2 = gp_Pnt(0.35672400000000004, 2.7513989999999997, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
outer = wires[0]
face_mkr = BRepBuilderAPI_MakeFace(outer)
for hole_w in wires[1:]: face_mkr.Add(hole_w)
face = face_mkr.Face()
extruded = BRepPrimAPI_MakePrism(face, gp_Vec(0,0,-1)*7.86).Shape()
trsf = gp_Trsf(); trsf.SetTranslation(gp_Vec(34.83,12.0,15.73))
rot  = gp_Trsf(); rot.SetRotation(gp_Ax1(gp_Pnt(0,0,0), gp_Dir(0,0,1)), 0.0)
rot.Multiply(trsf)
extruded = BRepBuilderAPI_Transform(extruded, rot, True).Shape()
all_shapes.append(extruded)
wires = []
edges = []
p1 = gp_Pnt(0.360027, 6.63903, 0.0)
p2 = gp_Pnt(3.3327269999999998, 8.359893, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(3.3327269999999998, 8.359893, 0.0)
p2 = gp_Pnt(3.326121, 8.373105, 0.0)
p3 = gp_Pnt(3.319515, 8.386317, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(3.319515, 8.386317, 0.0)
p2 = gp_Pnt(3.13785, 8.363195999999999, 0.0)
p3 = gp_Pnt(2.992518, 8.475498, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(2.992518, 8.475498, 0.0)
p2 = gp_Pnt(0.5416920000000001, 7.061814, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(0.5416920000000001, 7.061814, 0.0)
p2 = gp_Pnt(0.445905, 6.853724999999999, 0.0)
p3 = gp_Pnt(0.360027, 6.63903, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
outer = wires[0]
face_mkr = BRepBuilderAPI_MakeFace(outer)
for hole_w in wires[1:]: face_mkr.Add(hole_w)
face = face_mkr.Face()
extruded = BRepPrimAPI_MakePrism(face, gp_Vec(0,0,-1)*7.86).Shape()
trsf = gp_Trsf(); trsf.SetTranslation(gp_Vec(34.83,12.0,15.73))
rot  = gp_Trsf(); rot.SetRotation(gp_Ax1(gp_Pnt(0,0,0), gp_Dir(0,0,1)), 0.0)
rot.Multiply(trsf)
extruded = BRepBuilderAPI_Transform(extruded, rot, True).Shape()
all_shapes.append(extruded)
wires = []
edges = []
p1 = gp_Pnt(0.5416920000000001, 7.061814, 0.0)
p2 = gp_Pnt(2.992518, 8.475498, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(2.992518, 8.475498, 0.0)
p2 = gp_Pnt(2.966094, 8.660465999999998, 0.0)
p3 = gp_Pnt(3.0783959999999997, 8.805798, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(3.0783959999999997, 8.805798, 0.0)
p2 = gp_Pnt(3.0684869999999997, 8.819009999999999, 0.0)
p3 = gp_Pnt(3.058578, 8.835525, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(3.058578, 8.835525, 0.0)
p2 = gp_Pnt(0.7927200000000001, 7.524233999999999, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(0.7927200000000001, 7.524233999999999, 0.0)
p2 = gp_Pnt(0.6606, 7.296327, 0.0)
p3 = gp_Pnt(0.5416920000000001, 7.061814, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
outer = wires[0]
face_mkr = BRepBuilderAPI_MakeFace(outer)
for hole_w in wires[1:]: face_mkr.Add(hole_w)
face = face_mkr.Face()
extruded = BRepPrimAPI_MakePrism(face, gp_Vec(0,0,-1)*7.86).Shape()
trsf = gp_Trsf(); trsf.SetTranslation(gp_Vec(34.83,12.0,15.73))
rot  = gp_Trsf(); rot.SetRotation(gp_Ax1(gp_Pnt(0,0,0), gp_Dir(0,0,1)), 0.0)
rot.Multiply(trsf)
extruded = BRepBuilderAPI_Transform(extruded, rot, True).Shape()
all_shapes.append(extruded)
wires = []
edges = []
p1 = gp_Pnt(0.789417, 1.866195, 0.0)
p2 = gp_Pnt(1.61847, 0.8158409999999999, 0.0)
p3 = gp_Pnt(2.6787330000000003, 0.0, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(2.6787330000000003, 0.0, 0.0)
p2 = gp_Pnt(2.8736099999999998, 0.27414900000000003, 0.0)
p3 = gp_Pnt(3.058578, 0.5582069999999999, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(3.058578, 0.5582069999999999, 0.0)
p2 = gp_Pnt(0.789417, 1.866195, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
outer = wires[0]
face_mkr = BRepBuilderAPI_MakeFace(outer)
for hole_w in wires[1:]: face_mkr.Add(hole_w)
face = face_mkr.Face()
extruded = BRepPrimAPI_MakePrism(face, gp_Vec(0,0,-1)*7.86).Shape()
trsf = gp_Trsf(); trsf.SetTranslation(gp_Vec(34.83,12.0,15.73))
rot  = gp_Trsf(); rot.SetRotation(gp_Ax1(gp_Pnt(0,0,0), gp_Dir(0,0,1)), 0.0)
rot.Multiply(trsf)
extruded = BRepBuilderAPI_Transform(extruded, rot, True).Shape()
all_shapes.append(extruded)
wires = []
edges = []
p1 = gp_Pnt(0.7927200000000001, 7.524233999999999, 0.0)
p2 = gp_Pnt(3.058578, 8.835525, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(3.058578, 8.835525, 0.0)
p2 = gp_Pnt(2.8736099999999998, 9.11628, 0.0)
p3 = gp_Pnt(2.6787330000000003, 9.390429, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(2.6787330000000003, 9.390429, 0.0)
p2 = gp_Pnt(1.61847, 8.574588, 0.0)
p3 = gp_Pnt(0.7927200000000001, 7.524233999999999, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
outer = wires[0]
face_mkr = BRepBuilderAPI_MakeFace(outer)
for hole_w in wires[1:]: face_mkr.Add(hole_w)
face = face_mkr.Face()
extruded = BRepPrimAPI_MakePrism(face, gp_Vec(0,0,-1)*7.86).Shape()
trsf = gp_Trsf(); trsf.SetTranslation(gp_Vec(34.83,12.0,15.73))
rot  = gp_Trsf(); rot.SetRotation(gp_Ax1(gp_Pnt(0,0,0), gp_Dir(0,0,1)), 0.0)
rot.Multiply(trsf)
extruded = BRepBuilderAPI_Transform(extruded, rot, True).Shape()
all_shapes.append(extruded)
wires = []
edges = []
p1 = gp_Pnt(1.9058309999999998, 4.696866, 0.0)
p2 = gp_Pnt(2.3649479999999996, 2.9462759999999997, 0.0)
p3 = gp_Pnt(3.6299969999999995, 1.6514999999999997, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(3.6299969999999995, 1.6514999999999997, 0.0)
p2 = gp_Pnt(3.6465119999999995, 1.691136, 0.0)
p3 = gp_Pnt(3.663027, 1.730772, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(3.663027, 1.730772, 0.0)
p2 = gp_Pnt(2.437614, 2.992518, 0.0)
p3 = gp_Pnt(1.9917089999999997, 4.693563, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(1.9917089999999997, 4.693563, 0.0)
p2 = gp_Pnt(1.9487699999999997, 4.693563, 0.0)
p3 = gp_Pnt(1.9058309999999998, 4.696866, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
outer = wires[0]
face_mkr = BRepBuilderAPI_MakeFace(outer)
for hole_w in wires[1:]: face_mkr.Add(hole_w)
face = face_mkr.Face()
extruded = BRepPrimAPI_MakePrism(face, gp_Vec(0,0,-1)*7.86).Shape()
trsf = gp_Trsf(); trsf.SetTranslation(gp_Vec(34.83,12.0,15.73))
rot  = gp_Trsf(); rot.SetRotation(gp_Ax1(gp_Pnt(0,0,0), gp_Dir(0,0,1)), 0.0)
rot.Multiply(trsf)
extruded = BRepBuilderAPI_Transform(extruded, rot, True).Shape()
all_shapes.append(extruded)
wires = []
edges = []
p1 = gp_Pnt(1.9058309999999998, 4.696866, 0.0)
p2 = gp_Pnt(1.9487699999999997, 4.693563, 0.0)
p3 = gp_Pnt(1.9917089999999997, 4.693563, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(1.9917089999999997, 4.693563, 0.0)
p2 = gp_Pnt(2.437614, 6.394607999999999, 0.0)
p3 = gp_Pnt(3.663027, 7.659656999999999, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(3.663027, 7.659656999999999, 0.0)
p2 = gp_Pnt(3.6465119999999995, 7.699293, 0.0)
p3 = gp_Pnt(3.6299969999999995, 7.738929, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(3.6299969999999995, 7.738929, 0.0)
p2 = gp_Pnt(2.3649479999999996, 6.444153, 0.0)
p3 = gp_Pnt(1.9058309999999998, 4.696866, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
outer = wires[0]
face_mkr = BRepBuilderAPI_MakeFace(outer)
for hole_w in wires[1:]: face_mkr.Add(hole_w)
face = face_mkr.Face()
extruded = BRepPrimAPI_MakePrism(face, gp_Vec(0,0,-1)*7.86).Shape()
trsf = gp_Trsf(); trsf.SetTranslation(gp_Vec(34.83,12.0,15.73))
rot  = gp_Trsf(); rot.SetRotation(gp_Ax1(gp_Pnt(0,0,0), gp_Dir(0,0,1)), 0.0)
rot.Multiply(trsf)
extruded = BRepBuilderAPI_Transform(extruded, rot, True).Shape()
all_shapes.append(extruded)
wires = []
edges = []
p1 = gp_Pnt(1.9917089999999997, 4.693563, 0.0)
p2 = gp_Pnt(2.437614, 2.992518, 0.0)
p3 = gp_Pnt(3.663027, 1.730772, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(3.663027, 1.730772, 0.0)
p2 = gp_Pnt(4.138659, 3.3987870000000004, 0.0)
p3 = gp_Pnt(4.234446, 5.1295589999999995, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(4.234446, 5.1295589999999995, 0.0)
p2 = gp_Pnt(3.134547, 4.805865, 0.0)
p3 = gp_Pnt(1.9917089999999997, 4.693563, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
outer = wires[0]
face_mkr = BRepBuilderAPI_MakeFace(outer)
for hole_w in wires[1:]: face_mkr.Add(hole_w)
face = face_mkr.Face()
extruded = BRepPrimAPI_MakePrism(face, gp_Vec(0,0,-1)*7.86).Shape()
trsf = gp_Trsf(); trsf.SetTranslation(gp_Vec(34.83,12.0,15.73))
rot  = gp_Trsf(); rot.SetRotation(gp_Ax1(gp_Pnt(0,0,0), gp_Dir(0,0,1)), 0.0)
rot.Multiply(trsf)
extruded = BRepBuilderAPI_Transform(extruded, rot, True).Shape()
all_shapes.append(extruded)
wires = []
edges = []
p1 = gp_Pnt(1.9917089999999997, 4.693563, 0.0)
p2 = gp_Pnt(3.134547, 4.805865, 0.0)
p3 = gp_Pnt(4.234446, 5.1295589999999995, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(4.234446, 5.1295589999999995, 0.0)
p2 = gp_Pnt(4.056084, 6.417729, 0.0)
p3 = gp_Pnt(3.663027, 7.659656999999999, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(3.663027, 7.659656999999999, 0.0)
p2 = gp_Pnt(2.437614, 6.394607999999999, 0.0)
p3 = gp_Pnt(1.9917089999999997, 4.693563, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
outer = wires[0]
face_mkr = BRepBuilderAPI_MakeFace(outer)
for hole_w in wires[1:]: face_mkr.Add(hole_w)
face = face_mkr.Face()
extruded = BRepPrimAPI_MakePrism(face, gp_Vec(0,0,-1)*7.86).Shape()
trsf = gp_Trsf(); trsf.SetTranslation(gp_Vec(34.83,12.0,15.73))
rot  = gp_Trsf(); rot.SetRotation(gp_Ax1(gp_Pnt(0,0,0), gp_Dir(0,0,1)), 0.0)
rot.Multiply(trsf)
extruded = BRepBuilderAPI_Transform(extruded, rot, True).Shape()
all_shapes.append(extruded)
wires = []
edges = []
p1 = gp_Pnt(3.663027, 7.659656999999999, 0.0)
p2 = gp_Pnt(8.918099999999999, 4.693563, 0.0)
p3 = gp_Pnt(3.663027, 1.730772, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(3.319515, 8.386317, 0.0)
p2 = gp_Pnt(3.5011799999999997, 8.02629, 0.0)
p3 = gp_Pnt(3.663027, 7.659656999999999, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(3.0783959999999997, 8.805798, 0.0)
p2 = gp_Pnt(3.411999, 8.71992, 0.0)
p3 = gp_Pnt(3.319515, 8.386317, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(2.6787330000000003, 9.390429, 0.0)
p2 = gp_Pnt(2.883519, 9.103068, 0.0)
p3 = gp_Pnt(3.0783959999999997, 8.805798, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(2.6787330000000003, 0.0, 0.0)
p2 = gp_Pnt(10.909809, 4.693563, 0.0)
p3 = gp_Pnt(2.6787330000000003, 9.390429, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(3.663027, 1.730772, 0.0)
p2 = gp_Pnt(3.2270309999999998, 0.8356589999999999, 0.0)
p3 = gp_Pnt(2.6787330000000003, 0.0, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
outer = wires[0]
face_mkr = BRepBuilderAPI_MakeFace(outer)
for hole_w in wires[1:]: face_mkr.Add(hole_w)
face = face_mkr.Face()
extruded = BRepPrimAPI_MakePrism(face, gp_Vec(0,0,-1)*7.86).Shape()
trsf = gp_Trsf(); trsf.SetTranslation(gp_Vec(34.83,12.0,15.73))
rot  = gp_Trsf(); rot.SetRotation(gp_Ax1(gp_Pnt(0,0,0), gp_Dir(0,0,1)), 0.0)
rot.Multiply(trsf)
extruded = BRepBuilderAPI_Transform(extruded, rot, True).Shape()
all_shapes.append(extruded)
wires = []
edges = []
p1 = gp_Pnt(3.663027, 1.730772, 0.0)
p2 = gp_Pnt(8.435862, 2.933064, 0.0)
p3 = gp_Pnt(7.187328, 7.692686999999999, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(7.187328, 7.692686999999999, 0.0)
p2 = gp_Pnt(5.925582, 6.166701, 0.0)
p3 = gp_Pnt(4.234446, 5.1295589999999995, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(4.234446, 5.1295589999999995, 0.0)
p2 = gp_Pnt(4.138659, 3.3987870000000004, 0.0)
p3 = gp_Pnt(3.663027, 1.730772, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
edges = []
circ = gp_Circ(gp_Ax2(gp_Pnt(5.453253, 4.693563, 0.0), gp_Dir(0,0,1)), 0.8653860000000001)
edge = BRepBuilderAPI_MakeEdge(circ).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
outer = wires[0]
face_mkr = BRepBuilderAPI_MakeFace(outer)
for hole_w in wires[1:]: face_mkr.Add(hole_w)
face = face_mkr.Face()
extruded = BRepPrimAPI_MakePrism(face, gp_Vec(0,0,-1)*7.86).Shape()
trsf = gp_Trsf(); trsf.SetTranslation(gp_Vec(34.83,12.0,15.73))
rot  = gp_Trsf(); rot.SetRotation(gp_Ax1(gp_Pnt(0,0,0), gp_Dir(0,0,1)), 0.0)
rot.Multiply(trsf)
extruded = BRepBuilderAPI_Transform(extruded, rot, True).Shape()
all_shapes.append(extruded)
wires = []
edges = []
p1 = gp_Pnt(3.663027, 7.659656999999999, 0.0)
p2 = gp_Pnt(4.056084, 6.417729, 0.0)
p3 = gp_Pnt(4.234446, 5.1295589999999995, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(4.234446, 5.1295589999999995, 0.0)
p2 = gp_Pnt(5.925582, 6.166701, 0.0)
p3 = gp_Pnt(7.187328, 7.692686999999999, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
p1 = gp_Pnt(7.187328, 7.692686999999999, 0.0)
p2 = gp_Pnt(5.420223, 8.15841, 0.0)
p3 = gp_Pnt(3.663027, 7.659656999999999, 0.0)
arc_builder = GC_MakeArcOfCircle(p1, p2, p3)
if arc_builder.IsDone():
    curve = arc_builder.Value()
    edge  = BRepBuilderAPI_MakeEdge(curve).Edge()
else:
    # 三点共线，退化为直线 p1-p3
    edge  = BRepBuilderAPI_MakeEdge(p1, p3).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
outer = wires[0]
face_mkr = BRepBuilderAPI_MakeFace(outer)
for hole_w in wires[1:]: face_mkr.Add(hole_w)
face = face_mkr.Face()
extruded = BRepPrimAPI_MakePrism(face, gp_Vec(0,0,-1)*7.86).Shape()
trsf = gp_Trsf(); trsf.SetTranslation(gp_Vec(34.83,12.0,15.73))
rot  = gp_Trsf(); rot.SetRotation(gp_Ax1(gp_Pnt(0,0,0), gp_Dir(0,0,1)), 0.0)
rot.Multiply(trsf)
extruded = BRepBuilderAPI_Transform(extruded, rot, True).Shape()
all_shapes.append(extruded)
wires = []
edges = []
circ = gp_Circ(gp_Ax2(gp_Pnt(1.6826950000000003, 1.6826950000000003, 0.0), gp_Dir(0,0,1)), 1.6826950000000003)
edge = BRepBuilderAPI_MakeEdge(circ).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
edges = []
circ = gp_Circ(gp_Ax2(gp_Pnt(1.6826950000000003, 1.6826950000000003, 0.0), gp_Dir(0,0,1)), 0.48077000000000003)
edge = BRepBuilderAPI_MakeEdge(circ).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
outer = wires[0]
face_mkr = BRepBuilderAPI_MakeFace(outer)
for hole_w in wires[1:]: face_mkr.Add(hole_w)
face = face_mkr.Face()
extruded = BRepPrimAPI_MakePrism(face, gp_Vec(0,0,-1)*7.86).Shape()
trsf = gp_Trsf(); trsf.SetTranslation(gp_Vec(14.879999999999999,17.04,15.73))
rot  = gp_Trsf(); rot.SetRotation(gp_Ax1(gp_Pnt(0,0,0), gp_Dir(0,0,1)), 0.0)
rot.Multiply(trsf)
extruded = BRepBuilderAPI_Transform(extruded, rot, True).Shape()
all_shapes.append(extruded)
wires = []
edges = []
p1 = gp_Pnt(0.0, 0.0, 0.0)
p2 = gp_Pnt(56.25, 0.0, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(56.25, 0.0, 0.0)
p2 = gp_Pnt(56.25, 39.3225, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(56.25, 39.3225, 0.0)
p2 = gp_Pnt(0.0, 39.3225, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
p1 = gp_Pnt(0.0, 39.3225, 0.0)
p2 = gp_Pnt(0.0, 0.0, 0.0)
edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
edges = []
circ = gp_Circ(gp_Ax2(gp_Pnt(38.512499999999996, 19.6575, 0.0), gp_Dir(0,0,1)), 12.3825)
edge = BRepBuilderAPI_MakeEdge(circ).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
outer = wires[0]
face_mkr = BRepBuilderAPI_MakeFace(outer)
for hole_w in wires[1:]: face_mkr.Add(hole_w)
face = face_mkr.Face()
extruded = BRepPrimAPI_MakePrism(face, gp_Vec(0,0,1)*7.86).Shape()
trsf = gp_Trsf(); trsf.SetTranslation(gp_Vec(0.0,52.43,7.86))
rot  = gp_Trsf(); rot.SetRotation(gp_Ax1(gp_Pnt(0,0,0), gp_Dir(0,0,1)), 180.0)
rot.Multiply(trsf)
extruded = BRepBuilderAPI_Transform(extruded, rot, True).Shape()
all_shapes.append(extruded)
wires = []
edges = []
circ = gp_Circ(gp_Ax2(gp_Pnt(38.512499999999996, 19.6575, 0.0), gp_Dir(0,0,1)), 12.3825)
edge = BRepBuilderAPI_MakeEdge(circ).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
edges = []
circ = gp_Circ(gp_Ax2(gp_Pnt(33.39, 10.799999999999999, 0.0), gp_Dir(0,0,1)), 0.5475)
edge = BRepBuilderAPI_MakeEdge(circ).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
edges = []
circ = gp_Circ(gp_Ax2(gp_Pnt(38.512499999999996, 19.6575, 0.0), gp_Dir(0,0,1)), 1.965)
edge = BRepBuilderAPI_MakeEdge(circ).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
outer = wires[0]
face_mkr = BRepBuilderAPI_MakeFace(outer)
for hole_w in wires[1:]: face_mkr.Add(hole_w)
face = face_mkr.Face()
extruded = BRepPrimAPI_MakePrism(face, gp_Vec(0,0,1)*7.86).Shape()
trsf = gp_Trsf(); trsf.SetTranslation(gp_Vec(0.0,52.43,7.86))
rot  = gp_Trsf(); rot.SetRotation(gp_Ax1(gp_Pnt(0,0,0), gp_Dir(0,0,1)), 180.0)
rot.Multiply(trsf)
extruded = BRepBuilderAPI_Transform(extruded, rot, True).Shape()
all_shapes.append(extruded)
wires = []
edges = []
circ = gp_Circ(gp_Ax2(gp_Pnt(33.39, 10.799999999999999, 0.0), gp_Dir(0,0,1)), 0.5475)
edge = BRepBuilderAPI_MakeEdge(circ).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
outer = wires[0]
face_mkr = BRepBuilderAPI_MakeFace(outer)
for hole_w in wires[1:]: face_mkr.Add(hole_w)
face = face_mkr.Face()
extruded = BRepPrimAPI_MakePrism(face, gp_Vec(0,0,1)*7.86).Shape()
trsf = gp_Trsf(); trsf.SetTranslation(gp_Vec(0.0,52.43,7.86))
rot  = gp_Trsf(); rot.SetRotation(gp_Ax1(gp_Pnt(0,0,0), gp_Dir(0,0,1)), 180.0)
rot.Multiply(trsf)
extruded = BRepBuilderAPI_Transform(extruded, rot, True).Shape()
all_shapes.append(extruded)
wires = []
edges = []
circ = gp_Circ(gp_Ax2(gp_Pnt(38.512499999999996, 19.6575, 0.0), gp_Dir(0,0,1)), 1.965)
edge = BRepBuilderAPI_MakeEdge(circ).Edge()
edges.append(edge)
wire_mkr = BRepBuilderAPI_MakeWire()
for _e in edges: wire_mkr.Add(_e)
wires.append(wire_mkr.Wire())
outer = wires[0]
face_mkr = BRepBuilderAPI_MakeFace(outer)
for hole_w in wires[1:]: face_mkr.Add(hole_w)
face = face_mkr.Face()
extruded = BRepPrimAPI_MakePrism(face, gp_Vec(0,0,1)*7.86).Shape()
trsf = gp_Trsf(); trsf.SetTranslation(gp_Vec(0.0,52.43,7.86))
rot  = gp_Trsf(); rot.SetRotation(gp_Ax1(gp_Pnt(0,0,0), gp_Dir(0,0,1)), 180.0)
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
