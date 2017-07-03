import bpy

allobjs = bpy.data.objects

for obj in allobjs:
    if ("grassdark_blade" in obj.name):
        print(obj.name)
        bpy.ops.object.modifier_add(type='SUBSURF')