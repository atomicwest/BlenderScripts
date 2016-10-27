'''
More generalized LocRotScale script

The setloc function will keyframe the location of each
matching object

The setsize function scale all of the stars uniformly
across however many frames when setframe is called

Setrot will keyframe rotations on each axis with a 
range of magnitudes based on the third argument passed
'''

import bpy
import math
import random

# prepare a scene
scn = bpy.context.scene
scn.frame_start = 1
scn.frame_end = 1200

#all = bpy.context.scene.objects
all = bpy.data.objects

target = "Asteroid"

def setsize(frame, obj, grow):
    scal = obj.scale
    print(scal[0])
    bpy.context.scene.frame_set(frame)
    
    obj.scale[1] = obj.scale[1]*grow
    
    bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')
    
def setloc(frame, obj, dist):
    #hardcoded for y-axis
    loc = obj.location
    print(loc[1])
    bpy.context.scene.frame_set(frame)
    obj.location[1] = obj.location[1] + dist
    bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')

def setrot(frame, obj, magnitude):
    rot = obj.rotation_euler
    print(rot)
    bpy.context.scene.frame_set(frame)
    
    rotX = obj.rotation_euler[0] + random.uniform(-1,1)*random.uniform(0,magnitude)
    rotY = obj.rotation_euler[1] + random.uniform(-1,1)*random.uniform(0,magnitude)
    rotZ = obj.rotation_euler[2] + random.uniform(-1,1)*random.uniform(0,magnitude)
    
    obj.rotation_euler = (rotX, rotY, rotZ)
    bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')


for obj in all:

    if (target in obj.name):
        bpy.data.objects[obj.name].select=True
    else:
        bpy.data.objects[obj.name].select=False
        continue

    print(obj.name)
    #setloc(150,obj, 10000)
    setloc(200, obj, 0)
    setloc(1200, obj, 5)
    setrot(0,obj, 0)
    setrot(1200, obj, 2)
