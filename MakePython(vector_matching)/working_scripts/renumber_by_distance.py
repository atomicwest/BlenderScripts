'''

1. pick a directional axis to order different objects
2. numerically rename and order a certain group of objects depending on 
    where they are located along the chosen axis

    e.g. a snake figure composed of thousands of smaller, separate objects
    facing the positive x direction;
    use this script to rename each object with the smaller numbers
    in the negative-most x direction, and the largest numbers in the 
    positive-most direction
    
this script is to be used in conjunction with keyframe_trace, so that
an iterative script can animate these objects in order

'''

import bpy
import math

allobj = bpy.data.objects

target = "scale_crystal"
axis = "x"

axes = {"x":0, "y":1, "z":2}

sort_objects = {} #keys correspond to integer distance  on one axis

for obj in allobj:
    if target in obj.name:
        coord = obj.location[axes[axis]]
        key = math.floor(coord) #this will determine the group of this object
        
        if key not in sort_objects.keys():
            sort_objects[key] = [obj]
        else:
            sort_objects[key].append(obj)

track = 0

#duplicate to key list to ensure sorting
ikeys = []

for s in sort_objects.keys():
    ikeys.append(s)

ikeys.sort()

for k in ikeys:
    for o in sort_objects[k]:
        o.name = target + ".%05d" % track
        track+=1


