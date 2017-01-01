#select

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

class ApplyAllMods(bpy.types.Operator):
    bl_idname = "myops.applymods"
    bl_label = "Apply all mods on each mesh object"
    bl_options = {'REGISTER', 'UNDO'}

    def applymods(self):
        #all = bpy.context.scene.objects
        objects = bpy.data.objects

        for obj in objects:
            bpy.ops.object.modifier_apply(apply_as='DATA')
            print(obj.name)

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        self.applymods()
        return {'FINISHED'}


class ApplyAllModsPanel(bpy.types.Panel):
    """Toolbox"""
    bl_label = "All Origin to Center of Mass"
    bl_idname = "OBJECT_PT_applymods"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "MassMaker"

    #objects of type.Panel have sub objects of type layout

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.operator("myops.applymods")


def register():
    bpy.utils.register_class(ApplyAllModsPanel)
    bpy.utils.register_class(ApplyAllMods)


def unregister():
    bpy.utils.unregister_class(ApplyAllModsPanel)
    bpy.utils.unregister_class(ApplyAllMods)


if __name__ == "__main__":
    register()
