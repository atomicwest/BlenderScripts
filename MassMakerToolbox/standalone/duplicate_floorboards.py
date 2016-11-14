#select object first then run in script editor
#this script mainly randomly distributes the
#location of each copy relative to it's original
#object, i.e. radiating away from this center

import bpy
import random
import math
from random import randint

obj = bpy.context.object
orig = bpy.context.object.data
dupTemp = orig.copy()

# user input textboxes
copies = 10
newName = ""

'''
random factor Location, Rotation, and Scale
e.g. user determines how large of a range for
random location placement for each duplicate
'''
rfL = 0
rfR = 0
rfS = 1

#booleans
integersOnly = True

#for randomizing signed floats
def signed():
    return random.uniform(-1,1)

def genLoc(i):
    l = obj.location
    # newX = math.ceil(2.451 * i)
    newY = l[2]+2.451 * (i+1)
    # newZ = math.ceil(2.451 * i)

    return (l[0],newY,l[2])


for i in range(copies):
    num = "%04d"%i

    if (len(newName)==0):
        newName = "%s%s" %(obj.name,num)

    dup = bpy.data.objects.new(newName, dupTemp)

    dup.location = genLoc(i)
    # dup.rotation_euler = genRot()
    dup.rotation_euler = obj.rotation_euler
    # dup.scale = genScale()
    dup.scale = obj.scale

    scene = bpy.context.scene
    scene.objects.link(dup)
    scene.update()
