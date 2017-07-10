'''

copy the location and direction of an object
vec is a mesh object that is an edge duplicated/separated
    from a face edge on a larger mesh model

target is the object that will copy the location and rotation of vec

originally built to create scales along a cylinder object to imitate
a snake

the problem is that the faces of a mesh are not always consistent; 
i.e. the index of each face can change, deleting or separating another
can result in the indices of each face changing.


'''

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


#construct vector from vertices
print(vec.data.vertices[0].co)
print(vec.data.vertices[1].co)
a = vec.data.vertices[0].co
b = vec.data.vertices[1].co
print(b-a)

direction = b-a


# use to_track_quat to align object to vector
bpy.context.object.rotation_mode = 'QUATERNION'
bpy.context.object.rotation_quaternion = direction.to_track_quat('X','Y')
# bpy.context.object.rotation_quaternion = direction.to_track_quat('X','Z')
# bpy.context.object.rotation_quaternion = direction.to_track_quat('Z','Y')
