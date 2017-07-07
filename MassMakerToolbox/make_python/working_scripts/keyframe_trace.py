'''
given hundreds or thousands of objects with the same name scheme,
make one object visible for each frame
keyframe both render and 3d view so that the animation can be previewed

right click on the camera/render restrict icon in the outline
click add to keying set 
'''

import bpy

scn = bpy.context.scene
scn.frame_start = 1

allobj = bpy.data.objects

target = "scale_crystal"

#make all invisible first and keyframe
bpy.context.scene.frame_set(1)
match_count = 1
for ob in allobj:
    print(ob.name)
    if target in ob.name:
        ob.hide = True
        ob.hide_render = True
        # bpy.ops.anim.keyframe_insert_button(all=True)
        # bpy.ops.anim.keyframe_insert_menu(confirm_success=True)
        ob.keyframe_insert(data_path="hide")
        ob.keyframe_insert(data_path="hide_render")
        match_count+=1

scn.frame_end = match_count

match_count = 1     #reuse match_count

#make each visible again but increment the frame
for ob in allobj:
    if target in ob.name:
        bpy.context.scene.frame_set(match_count)
        ob.hide = False
        ob.hide_render = False
        
        # bpy.ops.anim.keyframe_insert_button(all=True)
        # bpy.ops.anim.keyframe_insert_menu(confirm_success=True)
        
        ob.keyframe_insert(data_path="hide")
        ob.keyframe_insert(data_path="hide_render")
        
        match_count+=1
