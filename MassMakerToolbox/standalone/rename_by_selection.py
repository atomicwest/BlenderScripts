#select objects to be renamed first

import bpy 

allobj = bpy.data.objects

'''
target = ""
newName = ""
for obj in allobj:
    if (target in obj.name):
        obj.name = newName
        print(obj.name + " successfully renamed")
'''

newName = ""
for obj in allobj:
    if allobj[obj.name].select==True:
        obj.name = newName
        print(obj.name + " successfully renamed")