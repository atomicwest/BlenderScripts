# select deformed body to freeze, go to frame, duplicate, press Alt+C to convert to mesh
# created to remove keyframes from many objects with baked dynamics for a bullettime render
# set frame on line 10
# set target name on line 12

import bpy

all = bpy.data.objects

bpy.context.scene.frame_set(39)

match = "insignia.0"

for item in all:
    if (match in item.name):
        print(item.name)
        bpy.context.scene.objects.active = bpy.data.objects[item.name]
        bpy.context.active_object.animation_data_clear()