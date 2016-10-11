import bpy
import random
import math

obj = bpy.context.object
orig = bpy.context.object.data
dupTemp = orig.copy()

for i in range(15):
    num = "%04d"%i
    newName = "%s%s" %(obj.name,num)
    dup = bpy.data.objects.new(newName, dupTemp)
    
    newX = math.ceil(random.uniform(-1,1)*25 + i)
    newY = math.ceil(random.uniform(-1,1)*25 + i)
    newZ = math.ceil(random.uniform(-1,1)*25 + i)
    
    dup.location = (newX,newY,newZ)
    dup.rotation_euler = (newX, newY, newZ)
    randScale = [-3,-2,-4,4,2,3]
    dup.scale = (random.choice(randScale), random.choice(randScale), random.choice(randScale))
    
    
    scene = bpy.context.scene
    scene.objects.link(dup)
    scene.update()