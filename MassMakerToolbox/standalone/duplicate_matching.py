#select the star object first then run in script editor

import bpy
import random
import math

orig = bpy.context.object.data
dupTemp = orig.copy()

all = bpy.data.objects

target = "Dodecahedron"
i = 0
#this will look through all of the scene objects
#and create a duplicate emission object at the 
#center of any object whose name matches the conditional
for obj in all:
    if target in obj.name:
        newName = "Core%s" %(i)
        dup = bpy.data.objects.new(newName, dupTemp)

        dup.location = obj.location
        newscale = random.uniform(-1,1)
        dup.scale = (newscale, newscale, newscale)
        i+=1

        scene = bpy.context.scene
        scene.objects.link(dup)
        scene.update()
        