#select object first then run

import bpy
import random
import math

orig = bpy.context.object.data
dupTemp = orig.copy()

for i in range(15):
    num = "%04d"%i
    newName = "Asteroid%s" %num
    dup = bpy.data.objects.new("Asteroid_new", dupTemp)
    
    newX = math.ceil(random.random()*20)
    newY = math.ceil(random.random()*20)
    newZ = math.ceil(random.random()*20)
    
    dup.location = (newX,newY,newZ)

    scene = bpy.context.scene
    scene.objects.link(dup)
    scene.update()