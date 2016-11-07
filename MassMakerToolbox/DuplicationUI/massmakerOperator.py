import bpy
import random
import math
from random import randint
from bpy.props import IntProperty, StringProperty, FloatProperty, BoolProperty

# def main(context):
    #actual duplication code goes here



class MassMake(bpy.types.Operator):
    """Tooltip"""
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

    def signed():
        return random.uniform(-1,1)

    def genLoc(i):
        newX = math.ceil(signed()*rfL + signed()*i)
        newY = math.ceil(signed()*rfL + signed()*i)
        newZ = math.ceil(signed()*rfL + signed()*i)

        return (newX,newY,newZ)

    def genRot():

        rotX = rfR*(random.uniform(-360,360)/360)
        rotY = rfR*(random.uniform(-360,360)/360)
        rotZ = rfR*(random.uniform(-360,360)/360)

        return (rotX, rotY, rotZ)

    def genScale():
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

    def maker():
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


        for i in range(copies):
            num = "%04d"%i

            if (len(newName)==0):
                newName = "%s%s" %(obj.name,num)

            dup = bpy.data.objects.new(newName, dupTemp)

            dup.location = genLoc(i)
            dup.rotation_euler = genRot()
            dup.scale = genScale()

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
            )
        # return {'COMPLETED DUPLICATION'}
        #yields errors on run
        #RuntimeError: class MYOPS_OT_massmake, function execute: incompatible return value , str(: 'COMPLETED DUPLICATION' not found in ('RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH', 'INTERFACE'))
        return {'FINISHED'}




def menu_func(self, context):
    self.layout.operator(MassMake.b1_idname, icon='MESH_CUBE')

def register():
    bpy.utils.register_class(MassMake)
    bpy.types.INFO_MT_mesh_add.append(menu_func)

def unregister():
    bpy.utils.unregister_class(MassMake)
    bpy.types.INFO_MT_mesh_add.remove(menu_func)

if __name__ == "__main__":
    register()

    # test call
    # bpy.ops.myops.massmake()
