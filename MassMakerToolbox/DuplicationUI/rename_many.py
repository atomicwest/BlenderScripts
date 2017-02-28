bl_info = {
    "name": "Rename Many",
    "author": "Jesson Go",
    "version": (0, 2, 1),
    "blender": (2, 78, 0),
    "location": "View3D > Tool Shelf > RandMass",
    "description": "Renames many objects under a new name pattern",
    "warning": "",
    "wiki_url": "",
    "category": "MassMaker",
    }


import bpy
from bpy.props import StringProperty

class RenameMany(bpy.types.Operator):
    bl_idname = "myops.renamemany"
    bl_label = "Rename Many"
    bl_options = {'REGISTER', 'UNDO'}

    newName = StringProperty(
            name="New Name Pattern (ENTER FIRST)",
            default="None"
            )

    targetName = StringProperty(
            name="Target Name Pattern",
            default="None"
            )

    def renameobjs(self, tName, nName):
        #all = bpy.context.scene.objects
        allobj = bpy.data.objects

        for obj in allobj:
            if (tName in obj.name):
                obj.name = nName
                print(obj.name + " successfully renamed")

    @classmethod
    def poll(self, context):
        return context.active_object is not None

    def execute(self, context):
        # main(context)
        self.renameobjs(
            self.targetName,
            self.newName
            )
        return {'FINISHED'}


class RenameManyPanel(bpy.types.Panel):
    """Toolbox"""
    bl_label = "Rename Many Objects"
    bl_idname = "OBJECT_PT_RenameMany"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "MassMaker"

    #objects of type.Panel have sub objects of type layout

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.prop(self, "targetName")

        row = layout.row()
        row.prop(self, "newName")

        row = layout.row()
        row.operator("myops.renamemany")


def register():
    bpy.utils.register_class(RenameManyPanel)
    bpy.utils.register_class(RenameMany)

def unregister():
    bpy.utils.unregister_class(RenameManyPanel)
    bpy.utils.unregister_class(RenameMany)

if __name__ == "__main__":
    register()