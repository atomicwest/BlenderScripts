bl_info = {
    "name": "Simpler Copy",
    "author": "Jesson Go",
    "version": (0, 1, 5),
    "blender": (2, 78, 0),
    "location": "View3D > Tool Shelf > RandMass",
    "description": "duplicate an object in one direction",
    "warning": "",
    "wiki_url": "",
    "category": "MassMaker",
    }

import bpy
import random
import math
from random import randint
from bpy.props import IntProperty, StringProperty, FloatProperty, BoolProperty

class SCopy(bpy.types.Operator):
    """ Make many copies in one direction"""
    bl_idname = "myops.scopy"
    bl_label = "Make copies in one direction"
    bl_options = {'REGISTER', 'UNDO'}

    #---------Input fields----------------
    # user input textboxes
    copies = IntProperty(
            name="Copies",
            description="Number of Duplicates",
            default=1,
            min=1
            )

    newName = StringProperty(
            name="Duplicate Name",
            default=""
            )

    xLoc = BoolProperty(
            name="X",
            default=False
            )

    yLoc = BoolProperty(
            name="Y",
            default=False
            )

    zLoc = BoolProperty(
            name="Z",
            default=True
            )

    '''
    random factor Location and Rotation
    user determines how large of a range for
    random location placement for each duplicate
    '''
    rfL = FloatProperty(
            name="Distance Between Copies",
            default=0.0
            )
            
    rfR = FloatProperty(
            name="Rotation Factor",
            description="Scale",
            min=0.0,
            max=360.0,
            default=0.0
            )

    #---------Actual code-----------------

    def maker(self, copies, newName, rfL, rfR, xLoc, yLoc, zLoc):
        obj = bpy.context.object
        orig = bpy.context.object.data
        dupTemp = orig.copy()
        
        '''
        random factor Location, Rotation, and Scale
        user determines how large of a range for
        random location placement for each duplicate
        '''

        def signed():
            return random.uniform(-1,1)

        def genLoc(rfL,i, xLoc, yLoc, zLoc):
            newX, newY, newZ = 0,0,0

            if xLoc: newX = rfL * i + obj.location[0]
            if yLoc: newY = rfL * i + obj.location[1]
            if zLoc: newZ = rfL * i + obj.location[2]

            return (newX,newY,newZ)

        def genRot(rfR):
            startrot = obj.rotation_euler
            rotX = rfR*(random.uniform(-360,360)/360) + startrot[0]
            rotY = rfR*(random.uniform(-360,360)/360) + startrot[1]
            rotZ = rfR*(random.uniform(-360,360)/360) + startrot[2]

            return (rotX, rotY, rotZ)


        for i in range(copies):
            num = "%04d"%i

            if (len(newName)==0):
                newName = "%s%s" %(obj.name,num)

            dup = bpy.data.objects.new(newName, dupTemp)

            dup.location = genLoc(rfL,i, xLoc, yLoc, zLoc)
            dup.rotation_euler = genRot(rfR)
            dup.scale = obj.scale

            scene = bpy.context.scene
            scene.objects.link(dup)
            scene.update()


    #-------------------------------------
    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        # main(context)
        self.maker(
            self.copies,
            self.newName,
            self.rfL,
            self.rfR,
            self.xLoc,
            self.yLoc,
            self.zLoc
            )
        return {'FINISHED'}


class SCopyPanel(bpy.types.Panel):
    """Toolbox"""
    bl_label = "Copy object in one direction"
    bl_idname = "OBJECT_PT_scopy"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "MassMaker"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.label(text="Mass producing: " + obj.name)
        row = layout.row()
        row.prop(obj, "name")

        row = layout.row()
        row.prop(self,'copies')

        row = layout.row()
        row.prop(self,'newName')

        row = layout.row()
        row.prop(self,'rfL')

        row = layout.row()
        row.prop(self,'rfR')

        row = layout.row()
        row.prop(self,'xLoc')

        row = layout.row()
        row.prop(self,'yLoc')

        row = layout.row()
        row.prop(self,'zLoc')

        row = layout.row()
        row.operator("myops.scopy")


def register():
    bpy.utils.register_class(SCopyPanel)
    bpy.utils.register_class(SCopy)


def unregister():
    bpy.utils.unregister_class(SCopyPanel)
    bpy.utils.unregister_class(SCopy)


if __name__ == "__main__":
    register()
