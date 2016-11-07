bl_info = {
    "name": "Mass Animator Locator",
    "author": "Jesson Go",
    "version": (1, 0),
    "blender": (2, 77, 0),
    "location": "View3D > Tool Shelf > RandMass",
    "description": "Animates many duplicates of the target object (location only)",
    "warning": "",
    "wiki_url": "",
    "category": "RandMass",
    }

import bpy
import random
import math
from random import randint
from bpy.props import IntProperty, StringProperty, FloatProperty, BoolProperty

#-------------Mass Animation Location Operator-------------

class ManyAnimLoc(bpy.types.Operator):
    bl_idname = "myops.massanimLoc"
    bl_label = "Set Location of Many Objects"
    bl_options = {'REGISTER', 'UNDO'}

    target = StringProperty(
            name="Target Name",
            default=""
            )

    startframe = IntProperty(
            name="Set Start Frame At",
            default=1
            )

    endframe = IntProperty(
            name="Set End Frame At",
            default=2
            )

    distX = FloatProperty(
            name="Distance Change X",
            default=0.0
            )

    distY = FloatProperty(
            name="Distance Change Y",
            default=0.0
            )

    distZ = FloatProperty(
            name="Distance Change Z",
            default=0.0
            )

    def locating(classobj, target, startframe, endframe, distX, distY, distZ):

        allobj = bpy.data.objects
        frames = (startframe, endframe)
        delta = (distX, distY, distZ)

        def setloc(frames, obj, delta):
            loc = obj.location
            print(loc)

            bpy.context.scene.frame_set(frames[0])
            bpy.ops.anim.keyframe_insert_menu(type='Location')

            bpy.context.scene.frame_set(frames[1])
            loc[0] = loc[0] + delta[0]
            loc[1] = loc[1] + delta[1]
            loc[2] = loc[2] + delta[2]
            # bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')
            bpy.ops.anim.keyframe_insert_menu(type='Location')

        for obj in allobj:

            if (target in obj.name):
                bpy.data.objects[obj.name].select=True
            else:
                bpy.data.objects[obj.name].select=False
                continue

            print(obj.name)
            setloc(frames, obj, delta)

    #-------------------------------------------------
    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        # main(context)
        self.locating(
            self.target,
            self.startframe,
            self.endframe,
            self.distX,
            self.distY,
            self.distZ
            )
        return {'FINISHED'}

#---------Mass Animation Panel----------------

class MassAnimLocPanel(bpy.types.Panel):
    bl_label="Animate Many Objects"
    bl_idname = "OBJECT_PT_massanimLoc"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "RandMass"

    def draw(self, context):
        layout=self.layout

        row = layout.row()
        row.prop()

        row = layout.row()
        row.prop(self, 'target')
        row = layout.row()
        row.prop(self, 'startframe')
        row = layout.row()
        row.prop(self, 'endframe')
        row = layout.row()
        row.prop(self, 'distX')
        row = layout.row()
        row.prop(self, 'distY')
        row = layout.row()
        row.prop(self, 'distZ')

        row = layout.row()
        row.operator("myops.massanimLoc")


#---------------------------------------------

def register():
    bpy.utils.register_class(MassAnimLocPanel)
    bpy.utils.register_class(ManyAnimLoc)


def unregister():
    bpy.utils.unregister_class(MassAnimLocPanel)
    bpy.utils.unregister_class(ManyAnimLoc)


if __name__ == "__main__":
    register()
