import math
import OCC.Core.gp as gp
import OCC.Core.BRepBuilderAPI as BRepBuilderAPI
import OCC.Core.BRepAlgoAPI as BRepAlgoAPI
from OCC.Core.AIS import AIS_Shape
from OCC.Display.SimpleGui import init_display
from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs  # 修正导入
from OCC.Core.IFSelect import IFSelect_RetError
from OCC.Core.TopoDS import TopoDS_Vertex  # 保留导入
from OCC.Core.TopTools import TopTools_HSequenceOfShape
from OCC.Core.TopAbs import TopAbs_VERTEX
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakePrism  # 使用正确的挤出类

# 创建一个简单的矩形面
def create_rect_face(x1, y1, x2, y2):
    # 创建3D点
    p1 = gp.gp_Pnt(x1, y1, 0)
    p2 = gp.gp_Pnt(x2, y1, 0)
    p3 = gp.gp_Pnt(x2, y2, 0)
    p4 = gp.gp_Pnt(x1, y2, 0)
    
    # 使用BRepBuilderAPI_MakeVertex创建顶点
    v1 = BRepBuilderAPI.BRepBuilderAPI_MakeVertex(p1).Vertex()
    v2 = BRepBuilderAPI.BRepBuilderAPI_MakeVertex(p2).Vertex()
    v3 = BRepBuilderAPI.BRepBuilderAPI_MakeVertex(p3).Vertex()
    v4 = BRepBuilderAPI.BRepBuilderAPI_MakeVertex(p4).Vertex()
    
    # 创建边
    edge1 = BRepBuilderAPI.BRepBuilderAPI_MakeEdge(v1, v2)
    edge2 = BRepBuilderAPI.BRepBuilderAPI_MakeEdge(v2, v3)
    edge3 = BRepBuilderAPI.BRepBuilderAPI_MakeEdge(v3, v4)
    edge4 = BRepBuilderAPI.BRepBuilderAPI_MakeEdge(v4, v1)
    
    # 正确的方式创建wire，每次传入一个边
    wire = BRepBuilderAPI.BRepBuilderAPI_MakeWire()
    wire.Add(edge1.Edge())
    wire.Add(edge2.Edge())
    wire.Add(edge3.Edge())
    wire.Add(edge4.Edge())

    return BRepBuilderAPI.BRepBuilderAPI_MakeFace(wire.Wire()).Face()

# 挤出草图
def extrude_face(face, depth):
    # 挤出操作，使用 BRepPrimAPI_MakePrism 来进行挤出
    normal = gp.gp_Vec(0, 0, depth)
    extruder = BRepPrimAPI_MakePrism(face, normal)
    return extruder.Shape()

# 创建草图并进行挤出
def create_extrusion():
    # 草图的参数
    length = 0.75
    width = 0.4023
    
    # 创建三个面
    face1 = create_rect_face(0.0, 0.0, 0.0187, 0.0437)  # 面1
    face2 = create_rect_face(0.0, 0.3087, 0.75, 0.4023)  # 面2
    face3 = create_rect_face(0.7313, 0.0, 0.75, 0.0437)  # 面3
    
    # 挤出面
    shape1 = extrude_face(face1, 0.3243)
    shape2 = extrude_face(face2, 0.3243)
    shape3 = extrude_face(face3, 0.3243)
    
    # 合并三个形状
    solid = BRepAlgoAPI.BRepAlgoAPI_Fuse(shape1, shape2).Shape()
    solid = BRepAlgoAPI.BRepAlgoAPI_Fuse(solid, shape3).Shape()
    
    return solid

# 设置并显示模型
def display_model():
    # 初始化显示器
    display, start_display, add_menu, add_function_to_menu = init_display()
    
    # 创建模型
    solid_model = create_extrusion()
    
    # 创建AIS对象并添加到显示
    ais_shape = AIS_Shape(solid_model)
    display.Context.Display(ais_shape, True)
    
    # 开始显示
    start_display()

# 导出为STEP文件
def export_to_step(shape, filename="output.step"):
    writer = STEPControl_Writer()
    # 使用 STEPControl_AsIs 来传递原始形状
    writer.Transfer(shape, STEPControl_AsIs)
    status = writer.Write(filename)
    
    if status == IFSelect_RetError:
        print("导出STEP文件时发生错误。")
    else:
        print(f"STEP文件已保存为 {filename}")

# 调用显示函数并导出为STEP
def main():
    solid_model = create_extrusion()
    display_model()  # 显示3D模型
    export_to_step(solid_model, "output.step")  # 导出STEP文件

# 运行主函数
main()
