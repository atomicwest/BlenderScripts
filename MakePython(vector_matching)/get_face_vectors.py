import bpy
import bmesh
import mathutils

allobj = bpy.data.objects

matchstr = "python_main_body_coil"

for o in allobj:
    if(matchstr in o.name):
        bpy.ops.object.mode_set(mode = 'EDIT')
        
        