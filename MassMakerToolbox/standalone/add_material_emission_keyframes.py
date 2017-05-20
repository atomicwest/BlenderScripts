import bpy
import inspect

scn = bpy.context.scene

#print(bpy.data.objects["targeting_knob_light"])
print(bpy.data.materials["targeting_light.001"])

allmat = bpy.data.materials

matnames = ["targeting_light","targeting_light.001","targeting_light.002","targeting_light.003"]

#emitvalue = inspect.getmembers(allmat["targeting_light.001"].node_tree.nodes["Emission"].inputs[1].default_value)

def emitval(matval):
    m = matnames[matval]
    return allmat[m].node_tree.nodes["Emission"].inputs[1]

#print(inspect.getmembers(allmat["targeting_light.001"].node_tree.nodes["Emission"].inputs[1].default_value))

lights0 = emitval(0)
lights1 = emitval(1)
lights2 = emitval(2)
lights3 = emitval(3)

frames = [x for x in range(650) if x%40==0]
offframes = [x for x in frames if x%80==0]
onframes = sorted(list(set(frames) - set(offframes)))

for fr in offframes:
    #bpy.ops.anim.change_frame(frame = fr)
    scn.frame_set(fr)
    lights0.default_value = 0.5
    lights0.keyframe_insert('default_value')
    lights1.default_value = 0
    lights1.keyframe_insert('default_value')
    lights2.default_value = 0.45
    lights2.keyframe_insert('default_value')    
    lights3.default_value = 0
    lights3.keyframe_insert('default_value')
    #bpy.ops.anim.keyframe_insert_button(all=True)
    
for fr in onframes:
    #bpy.ops.anim.change_frame(frame = fr)
    scn.frame_set(fr)
    lights0.default_value = 0
    lights0.keyframe_insert('default_value')
    lights1.default_value = 0.8
    lights1.keyframe_insert('default_value')
    lights2.default_value = 0
    lights2.keyframe_insert('default_value')
    lights3.default_value = 0.75
    lights3.keyframe_insert('default_value')
    #bpy.ops.anim.keyframe_insert_button(all=True)s