#link sun lamp and sky environment texture
#must have a Lamp object named "SunLamp" and 
#world labeled as "desert_sky" (or change accordingly in code)

import bpy
import mathutils as util
import math

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
#bpy.data.node_groups["Shader Nodetree"].nodes["Sky Texture"].sun_direction = vec
