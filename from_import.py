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

