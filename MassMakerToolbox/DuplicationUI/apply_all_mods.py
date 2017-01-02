bl_info = {
    "name": "Apply All Modifiers",
    "author": "Jesson Go",
    "version": (0, 1, 1),
    "blender": (2, 78, 0),
    "location": "View3D > Tool Shelf > RandMass",
    "description": "Apply mods from top of stack down",
    "warning": "",
    "wiki_url": "",
    "category": "MassMaker",
    }


import bpy
from bpy.props import *

class ApplyAllMods(bpy.types.Operator):
    bl_idname = "myops.applymods"
    bl_label = "Apply All Mods"
    bl_options = {'REGISTER', 'UNDO'}

    def applymods(self):
        #all = bpy.context.scene.objects
        objects = bpy.data.objects

        for obj in objects:

            bpy.context.scene.objects.active = obj
            mods = bpy.data.objects[obj.name].modifiers

            for i in range(len(mods)):
                mname = mods[i-1].name
                bpy.ops.object.modifier_apply(apply_as='DATA', modifier=mname)

            print(obj.name)

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        self.applymods()
        return {'FINISHED'}


class ApplySomeMods(bpy.types.Operator):
    bl_idname = "myops.applysomemods"
    bl_label = "Specify Mod"
    bl_options = {'REGISTER', 'UNDO'}

    modName = StringProperty(
        name="Modifier Name",
        default="None"
        )

    def applysomemods(self, modname):
        objects = bpy.data.objects

        for obj in objects:
            
            if modname == "None":
                return

            bpy.context.scene.objects.active = obj
            mods = bpy.data.objects[obj.name].modifiers
            modlist = []

            for i in range(len(mods)):
                modlist.append(mods[i-1].name)

            print(modlist)
            if modname in modlist:
                bpy.ops.object.modifier_apply(apply_as='DATA', modifier=modname)
            else:
                print("Modifier doesn't exist")

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        self.applysomemods(self.modName)
        return {'FINISHED'}

class ApplyModsPanel(bpy.types.Panel):
    """Toolbox"""
    bl_label = "Apply Mesh Mods"
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

        row = layout.row()
        row.prop(self, "modName")

        row = layout.row()
        row.operator("myops.applysomemods")

        row = layout.row()
        layout.label(text="Some default modifier names -> MODIFIER:")
        row = layout.row()
        layout.label(text="Mirror -> MIRROR")
        row = layout.row()
        layout.label(text="Subsurf -> SUBSURFACE")

def register():
    bpy.utils.register_class(ApplyModsPanel)
    bpy.utils.register_class(ApplyAllMods)
    bpy.utils.register_class(ApplySomeMods)


def unregister():
    bpy.utils.unregister_class(ApplyModsPanel)
    bpy.utils.unregister_class(ApplyAllMods)
    bpy.utils.unregister_class(ApplySomeMods)


if __name__ == "__main__":
    register()
