# select the faces first

import bpy
import bmesh
import mathutils
import math

bpy.ops.object.mode_set(mode='EDIT')

# Get the active mesh
obj = bpy.context.edit_object
me = obj.data


# Get a BMesh representation
bm = bmesh.from_edit_mesh(me)

rot = mathutils.Euler((math.radians(45), math.radians(45), math.radians(45) )).to_matrix()
scale = mathutils.Vector((0.9,0.9,0.9))

for f in bm.faces:
    if f.select == True:
        print(f)
        bmesh.ops.scale(
            bm,
            vec=scale,
            verts=f.verts
        )
        

# Show the updates in the viewport
# and recalculate n-gon tessellation.
bmesh.update_edit_mesh(me, True)
