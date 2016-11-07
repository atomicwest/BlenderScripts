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
copies = 0
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
    newX = math.ceil(signed()*rfL + signed()*i)
    newY = math.ceil(signed()*rfL + signed()*i)
    newZ = math.ceil(signed()*rfL + signed()*i)

    return (newX,newY,newZ)

def genRot():

    rotX = rfR*(random.uniform(-360,360)/360)
    rotY = rfR*(random.uniform(-360,360)/360)
    rotZ = rfR*(random.uniform(-360,360)/360)

    return (rotX, rotY, rotZ)

def genScale():
    vals = []
    scale3d = ()
    if integersOnly:
        for j in range(3):
            #omit 0s
            a = 0
            while(a==0):
                a = randint(-rfS,rfS)
            vals+=[a]
        scale3d = (vals[0],vals[1],vals[2])
        #scale3d = (randint(-rfS,rfS),randint(-rfS,rfS),randint(-rfS,rfS))
    else:
        for j in range(3):
            #omit 0s
            a = 0
            while(a==0):
                a = random.uniform(-rfS,rfS)
            vals+=[a]
        scale3d = (vals[0],vals[1],vals[2])
        #scale3d = (random.uniform(-rfS,rfS), random.uniform(-rfS,rfS), random.uniform(-rfS,rfS))

    return scale3d

for i in range(copies):
    num = "%04d"%i

    if (len(newName)==0):
        newName = "%s%s" %(obj.name,num)

    dup = bpy.data.objects.new(newName, dupTemp)

    dup.location = genLoc(i)
    dup.rotation_euler = genRot()
    dup.scale = genScale()

    scene = bpy.context.scene
    scene.objects.link(dup)
    scene.update()
