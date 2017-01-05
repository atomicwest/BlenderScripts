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
            if "light" in obj.name:
                data.materials.append(allmat["Limb_light"])
            else:
                data.materials.append(allmat["Metal_main"])

