import bpy

allobjs = bpy.data.objects

for obj in allobjs:
    if ("armor" in obj.name):
        print(obj.name)
        bpy.ops.object.modifier_add(type='COLLISION')