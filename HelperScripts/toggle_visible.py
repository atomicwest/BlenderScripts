'''

change the properties of a group of objects by cross referencing
a list of strings that match the target objects

'''

import bpy

allobj = bpy.data.objects

targets = ["dragonzord", "button", "backlight"] 

def lookInList(l,string):
    for el in l:
        if el in string:
            return True
    return False

for obj in allobj:
    if lookInList(targets,obj.name):
        obj.hide = False
        obj.hide_render = False
    else:
        obj.hide = True
        obj.hide_render = True
    