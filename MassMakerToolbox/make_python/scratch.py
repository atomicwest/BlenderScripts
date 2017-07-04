import bpy
import mathutils
import inspect

print('-----------------------------')

selected = bpy.context.scene.objects.active
#print(inspect.getmembers(selected))

#create a plane object, leave at origin and name "Plane_base"
base = bpy.data.objects["Plane_base"]

#edge object that will provide vector info
#should change to each direction of each face during iter
vec = bpy.data.objects["python_trial_vector"]

#get the duplicate object that will be rotated
target = bpy.data.objects["scale.001"]

#print(selected.location)
#print(selected.rotation_euler)
#print(base.rotation_euler)

#print(selected.rotation_euler - base.rotation_euler)
#print(selected.matrix_local)

print(vec.data.vertices[0].co.magnitude)
print(vec.data.vertices[1].co.magnitude)

#print(inspect.getmembers(selected.data.vertices[0]))
print(vec.data.vertices[0].co)
print(vec.data.vertices[1].co)
a = vec.data.vertices[0].co
b = vec.data.vertices[1].co
print(b-a)

direction = b-a

print(direction.magnitude)

bpy.context.object.rotation_mode = 'QUATERNION'
#bpy.context.object.rotation_quaternion = direction.to_track_quat(['X','Y'],'Z')

