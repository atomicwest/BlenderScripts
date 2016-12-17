def execution:
    eval('bpy.data.objects[].rigid_body.collision_shape')


class meshBodyShape(bpy.types.PropertyGroup):
    options = [
        ("CONVEX_HULL","Convex Hull",'','CONVEX_HULL', 0),
        ("MESH", "Mesh", '','MESH', 1),
        ("BOX","Box",'', 'BOX' ,2),
        ("SPHERE","Sphere",'', 'SPHERE', 3),
        ("CAPSULE","Capsule", '', 'CAPSULE',4),
        ("CYLINDER","Cylinder", '', 'CYLINDER',5),
        ("CONE", "Cone", '', 'CONE', 6)
        ]
    
    meshAdd = bpy.props.EnumProperty(
            items = options,
            default = "Convex Hull",
            update=execution
        )