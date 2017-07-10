# import bpy
# import bmesh
# import inspect 


# active_obj = bpy.context.object.data

# # Get a BMesh representation
# bm = bmesh.new()   # create an empty BMesh
# bm.from_mesh(active_obj)   # fill it in from a Mesh


# #print(inspect.getmembers(bm.faces.active))

# # Get info on bmesh faces
# for f in bm.faces:
#     #inspect.getmembers(f)
#     print(f)
#     #print(f.index)
#     #break

# # Finish up, write the bmesh back to the mesh
# bm.to_mesh(active_obj)
#=================================================
# import bpy
# import bmesh
# import inspect 

# active_obj = bpy.context.object.data

# # Get a BMesh representation
# bm = bmesh.new()   # create an empty BMesh
# bm.from_mesh(active_obj)   # fill it in from a Mesh

# # Get info on bmesh faces
# for f in bm.faces:
#     inspect.getmembers(f)
#     break

# # Finish up, write the bmesh back to the mesh
# bm.to_mesh(active_obj)

import bpy
import mathutils

selected = bpy.context.scene.objects.active

# duplicate face
bpy.ops.mesh.duplicate_move(MESH_OT_duplicate={"mode":1}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})

# convert face to separate object
bpy.ops.mesh.separate(TYPE='SELECTED')

# origin to center of mass

# get vector from face edge
    #construct vector from vertices
        #find difference between vertex position coordinates

# use to_track_quat to align object to vector

