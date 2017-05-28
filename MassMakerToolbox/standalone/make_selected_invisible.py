#select all objects first

import bpy

allobj = bpy.data.objects

for obj in allobj:
    if obj.select==True:
        print(obj.name)
        obj.hide=True           #false when making objects visible again
        obj.hide_render=True    #false when making objects visible again