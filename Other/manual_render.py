#intended for use with PRMan/Renderman 
#adapted from http://blender.stackexchange.com/questions/17839/python-render-specific-frames

import bpy

# bpy.ops.render.render()
# bpy.context.scene.frame_set()

scene = bpy.context.scene
outpath = scene.render.filepath
scene.render.image_settings.file_format = 'PNG'


fstart = bpy.data.scenes["Scene"].frame_start
fend = bpy.data.scenes["Scene"].frame_end

for fnum in range(fstart,fend):
    
    scene.frame_set(fnum)

    # set output path so render won't get overwritten
    scene.render.filepath = outpath + str(fnum)
    
    #RenderMan in Blender might encounter RuntimeError: Error: PRMan: P03003 {Error}
    try:
        bpy.ops.render.render(write_still=True) # render still
    except RuntimeError:
        continue
    
# restore the filepath
scene.render.filepath = outpath