'''
run massmakerOperator.py first
'''

bl_info = {
    "name": "Mass Maker",
    "author": "Jesson Go",
    "version": (1, 0),
    "blender": (2, 75, 0),
    "location": "View3D > Tool Shelf > RandMass",
    "description": "Makes many duplicates of the selected object",
    "warning": "",
    "wiki_url": "",
    "category": "RandMass",
    }


import bpy
import random
import math
from random import randint
from bpy.props import IntProperty, StringProperty, FloatProperty, BoolProperty

class ManyDuplicate(bpy.types.Operator):
    """ Mass Produce the Current Object"""
    bl_idname = "myops.massmake"
    bl_label = "Make Many Copies"
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

    '''
    random factor Location, Rotation, and Scale
    user determines how large of a range for
    random location placement for each duplicate
    '''
    rfL = FloatProperty(
            name="Location Factor",
            default=0.0
            )
    rfR = FloatProperty(
            name="Rotation Factor",
            description="Scale",
            min=0.0,
            max=360.0,
            default=0.0
            )
    rfS = FloatProperty(
            name="Scale Factor",
            description="Scale",
            min=0.0,
            max=300,
            default=1.0
            )

    #booleans
    integersOnly = BoolProperty(
            name="Use Only Integer Scaling?",
            default=True
            )

    #---------Actual code-----------------

    def maker(classobj, copies, newName, rfL, rfR, rfS, integersOnly):
        obj = bpy.context.object
        orig = bpy.context.object.data
        dupTemp = orig.copy()

        # user input textboxes
        #copies = 0
        #newName = ""

        '''
        random factor Location, Rotation, and Scale
        user determines how large of a range for
        random location placement for each duplicate
        '''
        #rfL = 0
        #rfR = 0
        #rfS = 1

        #booleans
        #integersOnly = True

        #for randomizing signed floats

        def signed():
            return random.uniform(-1,1)

        def genLoc(rfL,i):
            newX = math.ceil(signed()*rfL + signed()*i)
            newY = math.ceil(signed()*rfL + signed()*i)
            newZ = math.ceil(signed()*rfL + signed()*i)

            return (newX,newY,newZ)

        def genRot(rfR):

            rotX = rfR*(random.uniform(-360,360)/360)
            rotY = rfR*(random.uniform(-360,360)/360)
            rotZ = rfR*(random.uniform(-360,360)/360)

            return (rotX, rotY, rotZ)

        def genScale(rfS, integersOnly):
            vals = []
            scale3d = ()
            if integersOnly:
                for j in range(3):
                    #omit 0s
                    a = 0
                    while(a==0):
                        a = randint(-rfS,rfS)
                    vals+=[a]
                scale3d = (vals[0],vals[1],vals[2])
                #scale3d = (randint(-rfS,rfS),randint(-rfS,rfS),randint(-rfS,rfS))
            else:
                for j in range(3):
                    #omit 0s
                    a = 0
                    while(a==0):
                        a = random.uniform(-rfS,rfS)
                    vals+=[a]
                scale3d = (vals[0],vals[1],vals[2])
                #scale3d = (random.uniform(-rfS,rfS), random.uniform(-rfS,rfS), random.uniform(-rfS,rfS))

            return scale3d



        for i in range(copies):
            num = "%04d"%i

            if (len(newName)==0):
                newName = "%s%s" %(obj.name,num)

            dup = bpy.data.objects.new(newName, dupTemp)

            dup.location = genLoc(rfL,i)
            dup.rotation_euler = genRot(rfR)
            dup.scale = genScale(rfS, integersOnly)

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
            self.rfS,
            self.integersOnly
            # copies,
            # newName,
            # rfL,
            # rfR,
            # rfS,
            # integersOnly
            )
        return {'FINISHED'}


    # def execute(self, context):
    #     main(context)
    #     return {'COMPLETED DUPLICATION'}

class MassMakePanel(bpy.types.Panel):
    """Toolbox"""
    bl_label = "Make Many Duplicates"
    bl_idname = "OBJECT_PT_massmake"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "RandMass"

    #objects of type.Panel have sub objects of type layout

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
        row.prop(self,'rfS')

        row = layout.row()
        row.prop(self,'integersOnly')

        row = layout.row()
        row.operator("myops.massmake")


def register():
    bpy.utils.register_class(MassMakePanel)
    bpy.utils.register_class(ManyDuplicate)


def unregister():
    bpy.utils.unregister_class(MassMakePanel)
    bpy.utils.unregister_class(ManyDuplicate)


if __name__ == "__main__":
    register()
