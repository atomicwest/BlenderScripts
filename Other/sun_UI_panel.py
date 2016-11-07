import bpy
import mathutils as util
import math

#====Sun Aligning Function===========================

def main(context):
    #get x,y,z angles of lamp in radians
    xTheta = bpy.data.objects['SunLamp'].rotation_euler[0]
    yTheta = bpy.data.objects['SunLamp'].rotation_euler[1]
    zTheta = bpy.data.objects['SunLamp'].rotation_euler[2]

    #create a vector that will know where the sun is
    #pointing relative to the sky texture
    vec = util.Vector((0.0, 0.0, 1.0))

    #rotational matrices to multiply by vec after rotation
    xMat = util.Matrix(((1.0, 0.0, 0.0), (0.0, math.cos(xTheta), -math.sin(xTheta)), (0.0, math.sin(xTheta), math.cos(xTheta)) ))
    yMat = util.Matrix(((math.cos(yTheta), 0.0, math.sin(yTheta)), (0.0, 0.1, 0.0), ( -math.sin(yTheta), 0.0,  math.cos(yTheta)) ))
    zMat = util.Matrix(((math.cos(zTheta), -math.sin(zTheta), 0.0), ( math.sin(zTheta), math.cos(zTheta), 0.0), (0.0, 0.0, 0.1) ))

    #vector multiplication
    vec = xMat * vec
    vec = yMat * vec
    vec = zMat * vec

    bpy.data.worlds['desert_sky'].node_tree.nodes['Sky Texture'].sun_direction = vec

#==================================================

class SunAlign(bpy.types.Operator):
    bl_idname = "myops.sun_align"     #name of your fxn, myops = myoperators
    bl_label = "Align the Sun Lamp"

#==================================================

class SunAlignPanel(bpy.types.Panel):
    bl_label = "Align the Sun Lamp"
    bl_idname = "OBJECT_PT_sunlamp"
    # bl_space_type = 'PROPERTIES'
    # bl_region_type = 'WINDOW'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    # bl_context = "object"
    bl_category = "¯\_(ツ)_/¯"

    def draw(self, context):
        layout = self.layout
        lamp = context.object

        row = layout.row()
        row.label(text="Align Sun with Sky", icon='WORLD_DATA')

        #if("lamp" in lamp.lower()):
        #    row = layout.row()
        #    row.label(text="Current Lamp: " + lamp)

        row = layout.row()
        row.operator("myops.sun_align")

#==================================================

def register():
    bpy.utils.register_class(SunAlign)
    bpy.utils.register_class(SunAlignPanel)

def unregister():
    bpy.utils.unregister_class(SunAlign)
    bpy.utils.unregister_class(SunAlignPanel)



if __name__ == "__main__":
    register()

#bpy.ops.myops.sun_align()
