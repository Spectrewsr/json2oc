# 基础几何模块
from OCC.Core.gp import gp_Pnt, gp_Vec, gp_Dir, gp_Ax2, gp_Circ, gp_Cylinder, gp_Sphere, gp_Torus, gp_Pln

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


from OCC.Core.gp import gp_Pnt, gp_Dir, gp_Ax2, gp_Circ, gp_Vec
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire, BRepBuilderAPI_MakeFace
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakePrism
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse
from OCC.Core.TopoDS import TopoDS_Compound, TopoDS_Builder
all_shapes = []  # 存储所有生成的 shape
edges = []
circle = gp_Circ(gp_Ax2(gp_Pnt(0.0, 0.0, 0.0), gp_Dir(0.0, 0.0, 1.0)), 1.5875)
edge = BRepBuilderAPI_MakeEdge(circle).Edge()
edges.append(edge)
wire_maker = BRepBuilderAPI_MakeWire()
for e in edges:
    wire_maker.Add(e)
wire = wire_maker.Wire()
face = BRepBuilderAPI_MakeFace(wire).Face()
extruded_shape = BRepPrimAPI_MakePrism(face, gp_Vec(0.0, 0.0, 1.0) * 0.3175).Shape()
all_shapes.append(extruded_shape)
edges = []
circle = gp_Circ(gp_Ax2(gp_Pnt(0.0, 0.0, 0.0), gp_Dir(0.0, 0.0, 1.0)), 1.27)
edge = BRepBuilderAPI_MakeEdge(circle).Edge()
edges.append(edge)
wire_maker = BRepBuilderAPI_MakeWire()
for e in edges:
    wire_maker.Add(e)
wire = wire_maker.Wire()
face = BRepBuilderAPI_MakeFace(wire).Face()
extruded_shape = BRepPrimAPI_MakePrism(face, gp_Vec(0.0, 0.0, 1.0) * 2.2225).Shape()
all_shapes.append(extruded_shape)
edges = []
circle = gp_Circ(gp_Ax2(gp_Pnt(0.0, 0.0, 0.0), gp_Dir(0.0, 0.0, 1.0)), 0.9525)
edge = BRepBuilderAPI_MakeEdge(circle).Edge()
edges.append(edge)
wire_maker = BRepBuilderAPI_MakeWire()
for e in edges:
    wire_maker.Add(e)
wire = wire_maker.Wire()
face = BRepBuilderAPI_MakeFace(wire).Face()
if all_shapes:
    result_shape = all_shapes[0]
    for shape in all_shapes[1:]:
        result_shape = BRepAlgoAPI_Fuse(result_shape, shape).Shape()
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
