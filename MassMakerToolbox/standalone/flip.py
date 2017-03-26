import bpy

allobj = bpy.data.objects

for obj in allobj:
    if obj.select == True:
        #if Z is the axis you want to flip on
        obj.scale[2] = -1 * obj.scale[2]