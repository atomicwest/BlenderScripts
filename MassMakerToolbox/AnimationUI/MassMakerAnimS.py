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

#-------------Mass Animation Scaling Operator-------------

class ManyAnimScale(bpy.types.Operator):
    bl_idname = "myops.massanimScale"
    bl_label = "Set Scaling of Many Objects"
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

    scaleF = IntProperty(
            name="Random Scaling Magnitude",
            default=0
            )

    def scaling(classobj, target, startframe, endframe, scaleF):

        allobj = bpy.data.objects
        frames = (startframe, endframe)

        def setrot(frames, obj, scaleF):
            sca = obj.scale
            print(sca)

            bpy.context.scene.frame_set(frames[0])
            bpy.ops.anim.keyframe_insert_menu(type='Scale')

            scaX = sca[0] + random.uniform(0,scaleF)
            scaY = sca[1] + random.uniform(0,scaleF)
            scaZ = sca[2] + random.uniform(0,scaleF)
            obj.scale = (scaX, scaY, scaZ)

            bpy.context.scene.frame_set(frames[1])
            bpy.ops.anim.keyframe_insert_menu(type='Scale')

        for obj in allobj:

            if (target in obj.name):
                bpy.data.objects[obj.name].select=True
            else:
                bpy.data.objects[obj.name].select=False
                continue

            print(obj.name)
            setrot(frames, obj, scaleF)

    #-------------------------------------------------
    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        # main(context)
        self.scaling(
            self.target,
            self.startframe,
            self.endframe,
            self.magnitude
            )
        return {'FINISHED'}

#---------Mass Animation Scaling Panel----------------

class MassAnimScalePanel(bpy.types.Panel):
    bl_label="Mass Scaling"
    bl_idname = "OBJECT_PT_massanimScale"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "RandMass"

    def draw(self, context):
        layout=self.layout

        row = layout.row()
        row.label(text="Mass Scaling Settings")

        row = layout.row()
        row.prop(self, 'target')
        row = layout.row()
        row.prop(self, 'startframe')
        row = layout.row()
        row.prop(self, 'endframe')
        row = layout.row()
        row.prop(self, 'scaleF')

        row = layout.row()
        row.operator("myops.massanimScale")

#---------------------------------------------

def register():
    bpy.utils.register_class(MassAnimRotPanel)
    bpy.utils.register_class(ManyAnimRot)


def unregister():
    bpy.utils.unregister_class(MassAnimRotPanel)
    bpy.utils.unregister_class(ManyAnimRot)


if __name__ == "__main__":
    register()
