from OCC.Core.gp import gp_Pnt, gp_Dir, gp_Ax2, gp_Circ, gp_Vec
from OCC.Core.BRepBuilderAPI import (
    BRepBuilderAPI_MakeEdge,
    BRepBuilderAPI_MakeWire,
    BRepBuilderAPI_MakeFace,
)
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakePrism
from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs
from OCC.Core.Interface import Interface_Static_SetCVal, Interface_Static_SetRVal
from OCC.Core.TopoDS import TopoDS_Shape


def export_step(shape: TopoDS_Shape, filename: str):
    """Export shape to STEP file with manufacturing-friendly settings"""
    writer = STEPControl_Writer()
    Interface_Static_SetCVal("write.step.unit", "MM")
    Interface_Static_SetCVal("write.step.precision.mode", "User")
    Interface_Static_SetRVal("write.step.precision.val", 0.001)
    
    writer.Transfer(shape, STEPControl_AsIs)
    status = writer.Write(filename)
    if status == 1:
        print(f"✅ STEP file saved: {filename}")
    else:
        print(f"❌ Failed to write STEP file: {filename}")


# ── Parameters ──────────────────────────────────────────────────────────────
radius = 50  # mm
height = 100  # mm

# ── Sketch: circle ──────────────────────────────────────────────────────────
circle = gp_Circ(gp_Ax2(gp_Pnt(0, 0, 0), gp_Dir(0, 0, 1)), radius)
edge = BRepBuilderAPI_MakeEdge(circle).Edge()
wire = BRepBuilderAPI_MakeWire(edge).Wire()
face = BRepBuilderAPI_MakeFace(wire).Face()

# ── Extrude ────────────────────────────────────────────────────────────────
extrude_vector = gp_Vec(0, 0, height)
solid = BRepPrimAPI_MakePrism(face, extrude_vector).Shape()

# ── Export to STEP ─────────────────────────────────────────────────────────
export_step(solid, "cylinder_sketch_extrude.step")
