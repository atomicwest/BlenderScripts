import os
from shutil import copyfile

STARTDIR = "/path/to/original/folder"
TARGETDIR = "/path/to/the/destination/folder"


#only copy over files every x number of files
skipframe = 2

try:
    os.makedirs(TARGETDIR)
except Exception as e:
    print(e)

for fname in os.listdir(STARTDIR):
    for l in fname:
        if l in [str(x) for x in range(10)]:
            fnum = fname[fname.index(l):len(fname)]
            prefnum = fnum.split(".")
            nfnum = int(prefnum[0])
            if nfnum%skipframe==0:
                copyfile(STARTDIR+fname, TARGETDIR+fname)
            break
        