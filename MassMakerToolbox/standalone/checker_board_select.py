# select the faces first

import bpy
import bmesh
import mathutils

bpy.ops.object.mode_set(mode='EDIT')

# Get the active mesh
obj = bpy.context.edit_object
me = obj.data


# Get a BMesh representation
bm = bmesh.from_edit_mesh(me)

#bm.faces.active = None

#print(bm.faces[412].select)

count = 0

for f in bm.faces:
    if count%2==0:
        f.select == True
    count+=1

# Show the updates in the viewport
# and recalculate n-gon tessellation.
bmesh.update_edit_mesh(me, True)
