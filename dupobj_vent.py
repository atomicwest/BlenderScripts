import bpy
import random
import math

obj = bpy.context.object
orig = bpy.context.object.data
dupTemp = orig.copy()

pos = obj.location
# sca = obj.scale
#print(pos[1])
for i in range(5):
    num = "%04d"%i
    newName = "%s%s" %(obj.name,num)
    dup = bpy.data.objects.new(newName, dupTemp)

    newZ = pos[2] - i*(0.1)

    dup.location = (pos[0],pos[1],newZ)
    # dup.rotation_euler = (newX, newY, newZ)
    dup.scale = obj.scale

    scene = bpy.context.scene
    scene.objects.link(dup)
    scene.update()
