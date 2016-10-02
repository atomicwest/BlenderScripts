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
    randScale = [-3,-2,-1,1,2,3]
    dup.scale = (random.choice(randScale), random.choice(randScale), random.choice(randScale))
    
    
    scene = bpy.context.scene
    scene.objects.link(dup)
    scene.update()