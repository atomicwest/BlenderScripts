'''

run from the directory where you want the Project directory to exist
Or copy the full path of the project's parent directory in the 
    parentpath variable
change mainfolder to be the name of the project folder

'''

import sys
import os

# parentpath = "C:/"
mainfolder = "NewProject"

def main():
    os.makedirs(mainfolder)
    dirs = [
        "models",
        "animations",
        "textures",
        "renders",
        "reference",
        ]
    
    for name in dirs:
        # os.makedirs(parentpath+mainfolder+"/"+name)
        os.makedirs(mainfolder+"/"+name)


# bpy.ops.file.directory_new()
# bpy.ops.wm.save_as_mainfile('INVOKE_SCREEN')

if __name__ == "__main__":
    main()