import bpy
import numpy as np

class RandMaker():
    def __init__(self, num, shape="cube"):
        self.copies = num
        self.shape = shape
    
    def rTup(a=1, b=10):
        x = np.random.randint(a,b) + np.random.random()
        y = np.random.randint(a,b) + np.random.random()
        z = np.random.randint(a,b) + np.random.random()
        return (x,y,z)
    
    def rNum(a=1,b=10):
        return np.random.randint(a,b) + np.random.random()
    
    def genCopies(self,a,b):
        for i in range(self.copies):
            loc = RandMaker.rTup(a,b)
            rot = RandMaker.rTup(a,b)
            if self.shape=="cube":
                bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, location=loc)
            else:
                bpy.ops.mesh.primitive_torus_add(align='WORLD', location=loc, rotation=rot, major_radius=RandMaker.rNum(3,10), minor_radius=RandMaker.rNum(0,3), abso_major_rad=1.25, abso_minor_rad=0.75)

            bpy.ops.transform.rotate(value=RandMaker.rNum(), orient_axis='Z', orient_type='VIEW', orient_matrix=(RandMaker.rTup(0,20), RandMaker.rTup(0,20), RandMaker.rTup(0,20)), orient_matrix_type='VIEW', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
            bpy.context.object.data.materials.append(bpy.data.materials["glass"])

rm = RandMaker(125,"torus")
rm.genCopies(1,70)
