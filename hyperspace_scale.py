'''
nonparticle method for hyperspace entry effect
create an icosphere and name it "star" something
make n many duplicates of the star object.

The setloc function will keyframe the location of each
matching object

The setsize function scale all of the stars uniformly
across however many frames when setframe is called
'''

import bpy
import math

# prepare a scene
scn = bpy.context.scene
scn.frame_start = 1
scn.frame_end = 1200

#all = bpy.context.scene.objects
all = bpy.data.objects


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

for obj in all:

    if ("star" in obj.name):
        bpy.data.objects[obj.name].select=True
    else:
        bpy.data.objects[obj.name].select=False
        continue

    print(obj.name)
    
    #set move objects 10000 units away from current position
    #and key at frame 150
    setloc(150,obj, 10000) 
    
    #return objects to original position at frame 180
    setloc(180,obj, 0)

    #starting point at frame 30
    setsize(30,obj, 1)
    
    #stretch by 200 units at frame 90
    setsize(90,obj, 200)
