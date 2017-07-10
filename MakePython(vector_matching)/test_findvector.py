import bpy
import mathutils
import inspect

print('-----------------------------')


#edge object that will provide vector info
#should change to each direction of each face during iter
vec = bpy.data.objects["python_trial_vector"]

#get the duplicate object that will be rotated
target = bpy.data.objects["scale_crystal"]
target.location = vec.location


#---------------------------------------------
#snake progresses along x axis

#iterate through all faces
#for each face

# duplicate face
bpy.ops.mesh.duplicate_move(MESH_OT_duplicate={"mode":1}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})

# convert face to separate object
bpy.ops.mesh.separate(TYPE='SELECTED')

# center to mass
bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')

# get vector from face edge
    #figure out which edge is the longer edge by using magnitude
    #get the vertices of the edge


#construct vector from vertices
        #find difference between vertex position coordinates
print(vec.data.vertices[0].co)
print(vec.data.vertices[1].co)
a = vec.data.vertices[0].co
b = vec.data.vertices[1].co
print(b-a)

direction = b-a


# use to_track_quat to align object to vector
bpy.context.object.rotation_mode = 'QUATERNION'
bpy.context.object.rotation_quaternion = direction.to_track_quat('X','Z')
# bpy.context.object.rotation_quaternion = direction.to_track_quat('X','Y')
# bpy.context.object.rotation_quaternion = direction.to_track_quat('Z','Y')

#delete the face then move to the next face
#-------------------------------------------------------------

#iterate through all faces first in edit mode

#duplicate face
# bpy.ops.mesh.duplicate_move(MESH_OT_duplicate={"mode":1}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})

# separate each face as separate object
# bpy.ops.mesh.separate(TYPE='SELECTED')

#center each origin to center of mass

#now switch to object mode and iterate through each face object

#iterate through each edge
#figure out which edge is the longest by finding magnitudes


