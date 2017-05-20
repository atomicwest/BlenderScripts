import bpy

obj = bpy.context.object
scene = bpy.context.scene

allobjs = bpy.data.objects

#set a variable for mod name in case the name is repeated a lot
#mod to be applied must be in all caps
modname1 = 'WIREFRAME'

#bpy.data.objects[obj.name].modifiers
print("------------------------------")

for obj in allobjs:
    if "light" not in obj.name:
        # if "Curve" in bpy.data.objects[obj.name].modifiers:
        print(obj.name)
        # bpy.context.scene.objects.active = obj      #you should not make each object active to add the mod
        bpy.ops.object.modifier_add(type=modname1)
        