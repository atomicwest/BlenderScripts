#select

bl_info = {
    "name": "Many Dynamics",
    "author": "Jesson Go",
    "version": (0, 1, 1),
    "blender": (2, 77, 0),
    "location": "View3D > Tool Shelf > RandMass",
    "description": "Adds Dynamics Properties to Selected Objects, works in tandem with Select Many",
    "warning": "",
    "wiki_url": "",
    "category": "MassMaker",
    }


import bpy
from bpy.props import FloatProperty, BoolProperty

class ManyDynamics(bpy.types.Operator):
    bl_idname = "myops.manydynamics"
    bl_label = "Add Dynamics to Many"
    bl_options = {'REGISTER', 'UNDO'}

    active = BoolProperty(
            name="Active?",
            default="True"
            )

    # d20 project = 0.915
    newFriction = FloatProperty(
            name="Friction",
            default=0.0,
            min=0.0
            )

    # d20 project = 0.946
    newBounce = FloatProperty(
            name="Bounciness",
            default=0.0,
            min=0.0
            )

    # d20 project = True
    collisionMargin = BoolProperty(
            name="Collision Margin?",
            default=False
            )

    # d20 project = 0.039
    newMargin = FloatProperty(
            name="Margin",
            default=0.0,
            min=0.0
            )

    def dynamicAdder(object, active, newFriction, newBounce, collisionMargin, newMargin):
        #all = bpy.context.scene.objects
        all = bpy.data.objects

        actType = 'ACTIVE'
        actType = 'ACTIVE' if (active==True) else 'PASSIVE'

        for obj in all:

            # if (match in obj.name):
            #     bpy.data.objects[obj.name].select=True
            if (bpy.data.objects[obj.name].select==True):
                # bpy.ops.rigidbody.world_add()
                bpy.ops.rigidbody.objects_add(type=actType)
                print("-----------newFriction Debug------------")
                print(newFriction[1])
                print("----------------------------------")
                bpy.data.objects[obj.name].rigid_body.friction=newFriction
                bpy.data.objects[obj.name].rigid_body.restitution=newBounce
                bpy.data.objects[obj.name].rigid_body.use_margin=collisionMargin
                bpy.data.objects[obj.name].rigid_body.collision_margin=newMargin

            print(obj.name)

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        # main(context)
        self.dynamicAdder(
            self.active,
            self.newFriction,
            self.newBounce,
            self.collisionMargin,
            self.newMargin
            )
        return {'FINISHED'}


        bl_category = "MassMaker"


class ManyDynamicsPanel(bpy.types.Panel):
    """Toolbox"""
    bl_label = "Add Dynamics to Many"
    bl_idname = "OBJECT_PT_manydynamics"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'

    #objects of type.Panel have sub objects of type layout

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.prop(self, "active")

        row = layout.row()
        row.prop(self, "newFriction")

        row = layout.row()
        row.prop(self, "newBounce")

        row = layout.row()
        row.prop(self, "collisionMargin")

        row = layout.row()
        row.prop(self, "newMargin")

        row = layout.row()
        row.operator("myops.manydynamics")


def register():
    bpy.utils.register_class(ManyDynamicsPanel)
    bpy.utils.register_class(ManyDynamics)


def unregister():
    bpy.utils.unregister_class(ManyDynamicsPanel)
    bpy.utils.unregister_class(ManyDynamics)


if __name__ == "__main__":
    register()