# script to assign materials  to many objects duplicated  from the same
# original object and are automatically numbered by blender 
# naming convention of (something.00x)

import bpy
from random import random

allmat = bpy.data.materials

for a in allmat:
    print(a)
    print(a.name)

allobj = bpy.data.objects

bpy.ops.object.mode_set(mode='OBJECT')

for obj in allobj:
    bpy.context.scene.objects.active = obj
    active = bpy.context.object
    data = active.data
    if hasattr(data, 'materials'):
        if len(data.materials)==0:
            if "gear" in obj.name:
                print(obj.name)
                try:
                    int(obj.name[-1])%2==0
                except ValueError:
                    continue
                if (int(obj.name[-1])%2==0):
                    data.materials.append(allmat["gear_even"])
                else: 
                    data.materials.append(allmat["gear_odd"])
