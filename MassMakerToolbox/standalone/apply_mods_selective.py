import bpy

obj = bpy.context.object
scene = bpy.context.scene

#sets active object only once
bpy.context.scene.objects.active = obj

allobjs = bpy.data.objects

#set a variable for mod name in case the name is repeated a lot
modname1 = "Subsurf"

#bpy.context.scene.objects.active = bpy.data.objects["Name of Object"]

#bpy.data.objects[obj.name].modifiers
print("------------------------------")

for obj in allobjs:
    if "neck" in obj.name:
        if "Curve" in bpy.data.objects[obj.name].modifiers:
            print(obj.name)
            bpy.context.scene.objects.active = obj      #needed to actually apply mod to each obj
            bpy.ops.object.modifier_apply(apply_as='DATA', modifier='Curve')
            #bpy.ops.object.modifier_apply(apply_as='DATA', modifier='Mirror')