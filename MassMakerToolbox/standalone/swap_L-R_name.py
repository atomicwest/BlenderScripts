import bpy

kids = bpy.context.scene.objects.active.children

for child in kids:
    new = ""
    if ("_L." in child.name) | ("_L_" in child.name):
        try:
            start = child.name.index("_L.")
        except:
            start = child.name.index("_L_")

        for i in range(len(child.name)):
            if i == start+1:
                new+="R"
            else:
                new+=child.name[i]

        child.name=new

    if ("_R." in child.name) | ("_R_" in child.name):
        try:
            start = child.name.index("_R.")
        except:
            start = child.name.index("_R_")

        for i in range(len(child.name)):
            if i == start+1:
                new+="L"
            else:
                new+=child.name[i]

        child.name=new
