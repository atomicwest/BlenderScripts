#assuming that all the faces of the object are already separated

import bpy
import bmesh
import inspect 

#---------change these variables--------------

match = "python_main_body"
copy_template = "scale_crystal"

#---------only rotate copies------------------

def copy_match(target, edge, axis):
    #target=>blender object (a copied object)
    #edge=>blender object (an isolated edge)
    #axis=>string representing a directional axis
    #edge is the edge whose location will be given to target
    #axis will determine how the vectors are subtracted/where the vector will point
    
    #determine vector direction and create direction vector
    a = edge.data.vertices[0].co
    b = edge.data.vertices[1].co
    
    axes = {'x':0, 'y':1, 'z':2}
    
    if a[axes[axis]] > b[axes[axis]]:
        direction = a-b
    else:
        direction = b-a
    
    target.location = edge.location
    target.scale *= direction.magnitude
    
    #align the copy
    bpy.context.object.rotation_mode = 'QUATERNION'
    bpy.context.object.rotation_quaternion = direction.to_track_quat('X','Y')
    bpy.ops.object.select_all(action='TOGGLE')

#--------------main---------------------------
allobj = bpy.data.objects

copyobj = bpy.data.objects[copy_template]

for f in allobj:
    
    f.select=True
    bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')
    f.select=False
    
    if match in f.name:
        # f should be an individual face object
        
        bpy.context.scene.objects.active = f
        
        active_obj = bpy.context.object.data    
        
        f.select = True
        # Get a BMesh representation
        bm = bmesh.new()
        bm.from_mesh(active_obj)
        
        # find the longest edge
        f.select = False
        
        bm.edges.ensure_lookup_table()  #run to enable indexing edges
        long_edge = bm.edges[0]
        long_edge.select = True
        
        bm.to_mesh(active_obj)      #this is important for updating the mesh
        
        for e in bm.edges:
            if e.calc_length() > long_edge.calc_length():
                bpy.ops.object.mode_set(mode = 'EDIT')
                long_edge.select = False
                long_edge = e
                long_edge.select = True
                bpy.ops.object.mode_set(mode = 'OBJECT')
                bm.to_mesh(active_obj)      #this is important for updating the mesh
        
        #---duplicate the edge--------
        bpy.ops.object.mode_set(mode = 'EDIT')
        bmesh.ops.duplicate(bm)
        bpy.ops.mesh.separate(type='SELECTED')
        # dup = bpy.ops.mesh.separate(type='SELECTED')
        bpy.ops.object.mode_set(mode = 'OBJECT')
        
        bpy.ops.object.select_all(action='TOGGLE') #deselect and move to next face
        
        f.select = True
        
        bpy.ops.object.delete() #delete the face to reduce memory load on scene
        bm.free()
        
        # get directional vector copy the object here
        # copy_match(copyobj,dup ,'x')

# rename all the edges
ecount = 0
for e in allobj:
    if match in  e.name:
        e.name = match + ".%05d" % ecount
        ecount+=1

#make enough copies of the target before orienting
bpy.context.scene.objects.active = copyobj
copyobj.select = True 

for i in range(ecount-1):
    bpy.ops.object.duplicate()

bpy.ops.object.select_all(action='TOGGLE')

#find all copies and orient
ecount = 0      #reuse variable
for cp in allobj:
    if copy_template in cp.name:
        bpy.context.scene.objects.active = cp
        cp.select = True
        edgename = match + ".%05d" % ecount
        try:
            nextedge = bpy.data.objects[edgename]
        except:
            break
        copy_match(cp,nextedge,'x')
        cp.select = False
        ecount+=1