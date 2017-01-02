bl_info = {
    "name": "Parent Many",
    "author": "Jesson Go",
    "version": (0, 4, 1),
    "blender": (2, 78, 0),
    "location": "View3D > Tool Shelf > RandMass",
    "description": "Parents objects of a specific naming pattern to the currently selected object",
    "warning": "",
    "wiki_url": "",
    "category": "MassMaker",
    }


import bpy
from bpy.props import StringProperty

class ParentMany(bpy.types.Operator):
    bl_idname = "myops.parentmany"
    bl_label = "Parent Many"
    bl_options = {'REGISTER', 'UNDO'}

    childrenName = StringProperty(
            name="Children Name Pattern",
            default="None"
            )

    def parentobjs(self, cName):
        #all = bpy.context.scene.objects
        allobj = bpy.data.objects

        parentObj = bpy.context.scene.objects.active

        for obj in allobj:
            if (cName in obj.name) & (parentObj.name != obj.name):
                allobj[obj.name].select=True
                bpy.ops.object.parent_set()

                print(obj.name + " successfully parented")

    @classmethod
    def poll(self, context):
        return context.active_object is not None

    def execute(self, context):
        # main(context)
        self.parentobjs(
            self.childrenName
            )
        return {'FINISHED'}

class UnparentAll(bpy.types.Operator):
    bl_idname="myops.unparent"
    bl_label="Unparent All"
    bl_options = {'REGISTER', 'UNDO'}

    def unparentall(self):
        allobj = bpy.data.objects

        for obj in allobj:
            allobj[obj.name].select=True
            bpy.ops.object.parent_clear(type='CLEAR')

    @classmethod
    def poll(self, context):
        return context.active_object is not None

    def execute(self, context):
        self.unparentall()
        return {'FINISHED'}

class ParentManyPanel(bpy.types.Panel):
    """Toolbox"""
    bl_label = "Parent Many Objects"
    bl_idname = "OBJECT_PT_parentmany"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "MassMaker"

    #objects of type.Panel have sub objects of type layout

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        layout.label(text="Select Parent First")

        row = layout.row()
        row.prop(self, "childrenName")

        row = layout.row()
        row.operator("myops.parentmany")

        row = layout.row()
        row.operator("myops.unparent")


def register():
    bpy.utils.register_class(ParentManyPanel)
    bpy.utils.register_class(ParentMany)
    bpy.utils.register_class(UnparentAll)


def unregister():
    bpy.utils.unregister_class(ParentManyPanel)
    bpy.utils.unregister_class(ParentMany)
    bpy.utils.unregister_class(UnparentAll)


if __name__ == "__main__":
    register()
