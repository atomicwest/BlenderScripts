bl_info = {
    "name": "Mass Animator Rotator",
    "author": "Jesson Go",
    "version": (1, 0),
    "blender": (2, 77, 0),
    "location": "View3D > Tool Shelf > RandMass",
    "description": "Animates many duplicates of the target object (rotation only)",
    "warning": "",
    "wiki_url": "",
    "category": "RandMass",
    }

import bpy
import random
import math
from random import randint
from bpy.props import IntProperty, StringProperty, FloatProperty, BoolProperty

#-------------Mass Animation Rotation Operator-------------

class ManyAnimRot(bpy.types.Operator):
    bl_idname = "myops.massanimRot"
    bl_label = "Set Rotation of Many Objects"
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

    magnitude = IntProperty(
            name="Random Rotation Magnitude",
            default=0
            )

    def rotating(classobj, target, startframe, endframe, magnitude):

        allobj = bpy.data.objects
        frames = (startframe, endframe)

        def setrot(frames, obj, magnitude):
            rotA = obj.rotation_euler
            print(rotA)

            bpy.context.scene.frame_set(frames[0])
            bpy.ops.anim.keyframe_insert_menu(type='Rotation')

            bpy.context.scene.frame_set(frames[1])

            rotX = rotA[0] + random.uniform(-1,1)*random.uniform(0,magnitude)
            rotY = rotA[1] + random.uniform(-1,1)*random.uniform(0,magnitude)
            rotZ = rotA[2] + random.uniform(-1,1)*random.uniform(0,magnitude)

            obj.rotation_euler = (rotX, rotY, rotZ)
            bpy.ops.anim.keyframe_insert_menu(type='Rotation')

        for obj in allobj:

            if (target in obj.name):
                bpy.data.objects[obj.name].select=True
            else:
                bpy.data.objects[obj.name].select=False
                continue

            print(obj.name)
            setrot(frames, obj, magnitude)

    #-------------------------------------------------
    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        # main(context)
        self.rotating(
            self.target,
            self.startframe,
            self.endframe,
            self.magnitude
            )
        return {'FINISHED'}

#---------Mass Animation Rotation Panel----------------

class MassAnimRotPanel(bpy.types.Panel):
    bl_label="Mass Rotation"
    bl_idname = "OBJECT_PT_massanimRot"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "RandMass"

    def draw(self, context):
        layout=self.layout

        row = layout.row()
        row.label(text="Mass Rotation Settings")

        row = layout.row()
        row.prop(self, 'target')
        row = layout.row()
        row.prop(self, 'startframe')
        row = layout.row()
        row.prop(self, 'endframe')
        row = layout.row()
        row.prop(self, 'magnitude')

        row = layout.row()
        row.operator("myops.massanimRot")
#---------------------------------------------

def register():
    bpy.utils.register_class(MassAnimRotPanel)
    bpy.utils.register_class(ManyAnimRot)


def unregister():
    bpy.utils.unregister_class(MassAnimRotPanel)
    bpy.utils.unregister_class(ManyAnimRot)


if __name__ == "__main__":
    register()
