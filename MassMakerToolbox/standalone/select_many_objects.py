#select

import bpy

#all = bpy.context.scene.objects
all = bpy.data.objects

match = "star"

for obj in all:

    if (match in obj.name):
        bpy.data.objects[obj.name].select=True

    print(obj.name)
