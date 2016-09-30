import bpy
import random
import math

orig = bpy.context.object.data
dupTemp = orig.copy()

for i in range(15):
    num = "%04d"%i
    newName = "Asteroid%s" %num
    dup = bpy.data.objects.new(newName, dupTemp)
    
    newX = math.ceil(random.uniform(-1,1)*20)
    newY = math.ceil(random.uniform(-1,1)*20)
    newZ = math.ceil(random.uniform(-1,1)*20)
    
    dup.location = (newX,newY,newZ)
    dup.rotation_euler = (newX, newY, newZ)
    dup.scale = (newX+1, newY+1, newZ+1)
    
    scene = bpy.context.scene
    scene.objects.link(dup)
    scene.update()