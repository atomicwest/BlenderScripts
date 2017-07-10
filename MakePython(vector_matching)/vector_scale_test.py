import bpy

copyobj = bpy.data.objects["scale"]
model = bpy.data.objects["test.001"]
axis = 'x'

target = bpy.data.objects["Sphere"]

print(copyobj.location)
print(model.location)

a = model.data.vertices[0].co
b = model.data.vertices[1].co

axes = {'x':0, 'y':1, 'z':2}

if a[axes[axis]] > b[axes[axis]]:
    direction = a-b
else:
    direction = b-a

mult = direction.magnitude

print(mult)

print(target.scale)
print(mult*target.scale)

target.scale *= mult