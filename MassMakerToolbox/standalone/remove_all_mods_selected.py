#remove all object modifiers if object is selected
#very useful for reducing poly count if  many subsurf mods
#are present in the scene

import bpy

allobj = bpy.data.objects

for obj in allobj:
    if obj.select == True:
        print(obj.name)
        bpy.context.scene.objects.active = bpy.data.objects[obj.name]
        #bpy.ops.object.modifier_remove()
        obj.modifiers.clear()
        obj.select = False