import bpy

base_mesh = bpy.context.object.data

bpy.ops.object.mode_set(mode = 'EDIT')
bpy.ops.mesh.select_all(action='TOGGLE')

bpy.ops.mesh.edge_split()

# bpy.ops.wm.call_menu(name="INFO_MT_window")
bpy.ops.mesh.select_all(action='TOGGLE')

bpy.ops.mesh.separate(type='LOOSE')