import bpy
import bmesh

bpy.ops.object.mode_set(mode = 'EDIT')

original = bpy.data.objects["original_python"].data
# original = bpy.context.object.data

bm = bmesh.new()   # create an empty BMesh
bm.from_mesh(original)   # fill it in from a Mesh

# for f in bm.faces:
#     print(f)
#     f.select=True
#     bpy.ops.mesh.duplicate_move()
#     bpy.ops.mesh.separate(type='SELECTED')
#     #f.select=False

while len(bm.faces) > 0:
    # bpy.ops.object.mode_set(mode = 'EDIT')
    bm.faces.ensure_lookup_table()
    print(bm.faces[0])
    bm.faces[0].select = True
    
    # bpy.ops.mesh.duplicate_move()
    bm.faces[0].copy()
    bpy.ops.mesh.separate(type='SELECTED')
    
    
    