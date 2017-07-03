import bpy
import bmesh

active_obj = bpy.context.object.data

# Get a BMesh representation
bm = bmesh.new()   # create an empty BMesh
bm.from_mesh(active_obj)   # fill it in from a Mesh


# Get info on bmesh faces
for f in bm.faces:
    print(f.calc_center_meridian)
    # print(f.rotation_euler)


# Finish up, write the bmesh back to the mesh
bm.to_mesh(active_obj)