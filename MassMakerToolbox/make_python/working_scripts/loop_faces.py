#assuming that all the faces of the object are already separated

import bpy
import bmesh
import inspect 

allobj = bpy.data.objects
match = "Cylinder"


for f in allobj:
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
        bpy.ops.object.mode_set(mode = 'OBJECT')
        
        bpy.ops.object.select_all(action='TOGGLE') #deselect and move to next face
        
        f.select = True
        
        bpy.ops.object.delete() #delete the face to reduce memory load on scene
        bm.free()
        
        
