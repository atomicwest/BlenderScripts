#!/bin/bash

sourcefolder="/the/directory/with/your/mixed/files"
destfolder="/the/directory/you/want/to/move/the/files/to"

find "${sourcefolder}" -name "*.filtered.exr" | while read -r file
do
  mv "${file}" "${destfolder}"
done

# save file to a directory; change source/destfolders
# $ chmod +x move_frames.sh
# ./move_frames.sh