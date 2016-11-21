#select

bl_info = {
    "name": "Select Many",
    "author": "Jesson Go",
    "version": (0, 1, 2),
    "blender": (2, 77, 0),
    "location": "View3D > Tool Shelf > RandMass",
    "description": "Select many duplicates of the selected object",
    "warning": "",
    "wiki_url": "",
    "category": "MassMaker",
    }


import bpy
from bpy.props import StringProperty

class SelectMany(bpy.types.Operator):
    bl_idname = "myops.selectmany"
    bl_label = "Select Many"
    bl_options = {'REGISTER', 'UNDO'}

    findName = StringProperty(
            name="Duplicate Name",
            default=""
            )

    def selector(object, match):
        #all = bpy.context.scene.objects
        all = bpy.data.objects

        # match = "star"

        for obj in all:

            if (match in obj.name):
                bpy.data.objects[obj.name].select=True

            print(obj.name)

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        # main(context)
        self.selector(
            self.findName
            )
        return {'FINISHED'}


class SelectManyPanel(bpy.types.Panel):
    """Toolbox"""
    bl_label = "Select Many Duplicates"
    bl_idname = "OBJECT_PT_selectmany"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "MassMaker"

    #objects of type.Panel have sub objects of type layout

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.prop(self, "findName")

        row = layout.row()
        row.operator("myops.selectmany")


def register():
    bpy.utils.register_class(SelectManyPanel)
    bpy.utils.register_class(SelectMany)


def unregister():
    bpy.utils.unregister_class(SelectManyPanel)
    bpy.utils.unregister_class(SelectMany)


if __name__ == "__main__":
    register()
