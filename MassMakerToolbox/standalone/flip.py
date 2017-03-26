import bpy

allobj = bpy.data.objects

for obj in allobj:
    if obj.select == True:
        #if Z is the axis you want to flip on
        flip = -1 * obj.scale[2]
        obj.scale = (0,0,flip)