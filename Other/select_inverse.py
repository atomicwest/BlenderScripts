bl_info = {
    "name": "Select Inverse Faces",
    "author": "Jesson Go",
    "version": (0, 1, 1),
    "blender": (2, 78, 0),
    "location": "View3D > Tool Shelf > AllSorts",
    "description": "Deselects currently selected faces while selecting negative space",
    "warning": "",
    "wiki_url": "",
    "category": "AllSorts"
    }

import bpy
import bmesh


class SelectInverseOperator(bpy.types.Operator):
    
    bl_idname = "asops.selectinverse"
    bl_label = "Select Inverse Faces"
    bl_options = {'REGISTER', 'UNDO'}
    
    def selectInverse(self):
        bpy.ops.object.mode_set(mode='EDIT')
        
        # Get the active mesh
        obj = bpy.context.edit_object
        me = obj.data
        
        # Get a BMesh representation
        bm = bmesh.from_edit_mesh(me)
        
        bm.faces.active = None
        
        for f in bm.faces:
            if f.select == True:
                f.select = False
            else:
                f.select = True
            
        # Show the updates in the viewport
        bmesh.update_edit_mesh(me, True)
    
    def execute(self,context):
        self.selectInverse()
        return {'FINISHED'}


class SelectInversePanel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_selectInverse"
    bl_label = "Select Inverse Faces"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "AllSorts"

    def draw(self, context):
        layout = self.layout
        obj = context.object
        
        row = layout.row()
        row.operator("asops.selectinverse")

def register():
    bpy.utils.register_class(SelectInverseOperator)
    bpy.utils.register_class(SelectInversePanel)
    
def unregister():
    bpy.utils.unregister_class(SelectInverseOperator)
    bpy.utils.unregister_class(SelectInversePanel)

if __name__ == "__main__":
    register()
    
    
    

