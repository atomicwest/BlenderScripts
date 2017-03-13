'''
select an mesh object that has children, and swap the naming convention
to the opposite side; e.g. armor_leg_L swap to armor_leg_R
can be edited to cover multiple naming schemes besides "_L"
'''

import bpy

print(bpy.context.scene.objects.active.name)

allobjects = bpy.data.objects

print(bpy.context.scene.objects.active.children)

selected = bpy.context.scene.objects.active

kids = selected.children


def swap(meshobj):
    if ("_L." in meshobj.name) | ("_L_" in meshobj.name):
        try:
            start = meshobj.name.index("_L.")
        except:
            start = meshobj.name.index("_L_")
                
        new = meshobj.name[0:start+1]
        new+="R" 
    else:
        try:
            start = meshobj.name.index("_R.")
        except:
            start = meshobj.name.index("_R_")
                
        new = meshobj.name[0:start+1]
        new+="L" 
           
        meshobj.name=new


swap(selected)      #swap naming scheme of the parent object

#swap naming scheme of children objects
for child in kids:
    swap(child)
