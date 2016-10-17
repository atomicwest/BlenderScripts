import bpy
import math

# prepare a scene
scn = bpy.context.scene
scn.frame_start = 1
scn.frame_end = 1200

#all = bpy.context.scene.objects
all = bpy.data.objects


def setframe(frame, obj, grow):
    scal = obj.scale
    print(scal[0])
    bpy.context.scene.frame_set(frame)
    #bpy.ops.transform.resize(value=(scal[0],scal[1]*grow, scal[2]))
    #bpy.ops.transform.translate(value=obj.location)
    #bpy.ops.transform.rotate(value=obj.orientation)
    # create keyframe
    
    obj.scale[1] = obj.scale[1]*grow
    
    bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')
    

for obj in all:

    if ("star" in obj.name):
        bpy.data.objects[obj.name].select=True
    else:
        bpy.data.objects[obj.name].select=False
        continue

    print(obj.name)
    setframe(30,obj, 1)
    setframe(90,obj, 200)
