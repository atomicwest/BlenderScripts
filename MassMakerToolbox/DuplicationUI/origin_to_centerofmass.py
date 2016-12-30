bl_info = {
    "name": "All Origin to Center of Mass",
    "author": "Jesson Go",
    "version": (0, 1, 1),
    "blender": (2, 78, 0),
    "location": "View3D > Tool Shelf > RandMass",
    "description": "Set origin of each object to its respective center of mass",
    "warning": "",
    "wiki_url": "",
    "category": "MassMaker",
    }


import bpy
from bpy.props import *

class CenterMany(bpy.types.Operator):
    bl_idname = "myops.allcenter"
    bl_label = "All Origin to Center of Mass"
    bl_options = {'REGISTER', 'UNDO'}

    def allcenter(self):
        objects = bpy.data.objects

        for obj in objects:
            obj.select=True
            bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')
            obj.select=False
            print(obj.name)

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        self.allcenter()
        return {'FINISHED'}


class CenterManyPanel(bpy.types.Panel):
    """Toolbox"""
    bl_label = "All Origin to Center of Mass"
    bl_idname = "OBJECT_PT_allcenter"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "MassMaker"

    #objects of type.Panel have sub objects of type layout

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.operator("myops.allcenter")


def register():
    bpy.utils.register_class(CenterManyPanel)
    bpy.utils.register_class(CenterMany)


def unregister():
    bpy.utils.unregister_class(CenterManyPanel)
    bpy.utils.unregister_class(CenterMany)


if __name__ == "__main__":
    register()
