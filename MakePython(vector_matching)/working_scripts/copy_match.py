import bpy

copyobj = bpy.data.objects["scale"]
edge = bpy.data.objects["test.001"]

def copy_match(target, model, axis):
    #target=>blender object (an isolated face)
    #model=>blender object (an isolated edge)
    #axis=>string representing a directional axis
    #model is the edge whose location will be given to target
    #axis will determine how the vectors are subtracted/where the vector will point
    
    #determine vector direction and create direction vector
    a = model.data.vertices[0].co
    b = model.data.vertices[1].co
    
    axes = {'x':0, 'y':1, 'z':2}
    
    if a[axes[axis]] > b[axes[axis]]:
        direction = a-b
    else:
        direction = b-a
    
    bpy.context.scene.objects.active = target
    
    
    #align the copy
    bpy.context.object.rotation_mode = 'QUATERNION'
    bpy.context.object.rotation_quaternion = direction.to_track_quat('X','Y')
    bpy.ops.object.select_all(action='TOGGLE')



copy_match(copyobj, edge,'x')

