import bpy
import random
import math

obj = bpy.context.object
orig = bpy.context.object.data
dupTemp = orig.copy()

pos = obj.location
sca = obj.scale
# rot = obj.rotation_euler
#print(pos[1])
for i in range(8):
    num = "%04d"%(i+1)
    newName = "%s%s" %(obj.name,num)
    dup = bpy.data.objects.new(newName, dupTemp)

    newY = pos[1] + i*(0.06)
    newZ = pos[2] - i*(0.12)

    dup.location = (pos[0],newY,newZ)
    # dup.rotation_euler = (newX, newY, newZ)
    # dup.rotation_euler = rot
    dup.scale = (sca[0]+i*(0.025), sca[1], sca[2])

    scene = bpy.context.scene
    scene.objects.link(dup)
    scene.update()
