import bpy
import math
import random

# prepare a scene
scn = bpy.context.scene
scn.frame_start = 1
scn.frame_end = 1200

#all = bpy.context.scene.objects
all = bpy.data.objects


def setframe(frame, rot, dist):
    sRot = random.choice([-1,1])*rot
    bpy.context.scene.frame_set(frame)
    # bpy.ops.transform.rotate(value=(sRot*math.pi ), axis=(random.choice([-1,1]), random.choice([-1,1]), random.choice([-1,1])))
    bpy.ops.transform.rotate(value=(sRot*math.pi ), axis=(0, 0, 0))
    # bpy.ops.transform.translate(value=(random.uniform(-dist,dist), random.uniform(-dist,dist),random.uniform(-dist,dist)))
    bpy.ops.transform.translate(value=(0, 0,0))

    # create keyframe
    bpy.ops.anim.keyframe_insert_menu(type='Rotation')
    bpy.ops.anim.keyframe_insert_menu(type='Location')

for obj in all:

    if ("Asteroid" in obj.name):
        bpy.data.objects[obj.name].select=True
    else:
        bpy.data.objects[obj.name].select=False
        continue

    setframe(1,0.005,1)
    setframe(1200,0.03,5)
