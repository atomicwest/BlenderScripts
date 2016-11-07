# Blender Scripts

### A growing library of tools for personal Blender projects.

Please visit my [blog][blog link] for more detailed discussions of my work.


## Mass Maker Toolbox
Set of tools developed mainly for handling hundreds of objects in my [Yavin-Hoth Hyperspace 360 VR][VR] project.
These include the asteroid field and hyperspace transition stars. The scripts have been tested for thousands of objects and can support as many as your hardware can handle, depending on the complexity and detail of your objects.
 
* ###[Standalone][saFolder] - Run this scripts directly from the Blender editor for specific actions; these serve the same purpose as the two UI sections below.
..* Duplicate Many Objects - [Script][dupobj] - Make copies of the selected mesh; the copies will fill 3D space in a spherically radial pattern, with randomized locations, rotations, and scaling based on three factors (rfL, rfR, rfS). The script can be easily edited for duplicating objects in specific patterns, e.g. an asteroid field.
..* Animate Many Objects - [Asteroid Field][asteroidAnim]: Current version hardcoded to duplicating "Asteroid"-named objects with a Z-axis limitation, simulating an accretion disk. See script comment for more details.
..* Duplicate Matching - [Script][matcher] - Duplicates the selected mesh and positions each object at the center of a target set of objects. E.g. if you wanted to make copies of hundreds of candles and automatically position each in the middle of hundreds of lanterns.

* ###[Mass Duplication UI][MDUI]
..* The most recent version should be fixed for the float issue on randomizing scaling, but sometimes freezes on certain Blender setups, e.g. a machine with no GPU and 4GB of RAM.
..* Previous versions of the UI script may have a base class called View3dPanel, which I believe is deprecated - omit when applicable, defined like so:
```python
class ManyDuplicate(View3dPanel, bpy.types.Operator):
    """ Mass Produce the Current Object"""
    bl_idname = "myops.massmake"
```

* ###[Mass Animation][MAUI] 
..* Current versions do not work well as a UI, it is better to modify the standalone asteroid animation script and run directly for now.

* Old subfolder contains deprecated versions of scripts mentioned above.
..* E.g. dupobj_vent.py was used to create several vent plates for the [Deathtrooper][deathtrooper] helmet project.

## Other

* Sun and Sky Environment Link script from this [tutorial](https://www.youtube.com/watch?v=YXso7kNzxIU)

[VR]: https://www.youtube.com/watch?v=thC53_FVSao
[blog link]: https://atomicprime.wordpress.com
[dupobj]: https://github.com/atomicwest/BlenderScripts/blob/master/MassMakerToolbox/standalone/duplicate_many_objects.py
[matcher]: https://github.com/atomicwest/BlenderScripts/blob/master/MassMakerToolbox/standalone/duplicate_matching.py
[asteroidAnim]: https://github.com/atomicwest/BlenderScripts/blob/master/MassMakerToolbox/standalone/asteroid_animate.py
[saFolder]: https://github.com/atomicwest/BlenderScripts/tree/master/MassMakerToolbox/standalone
[MDUI]: https://github.com/atomicwest/BlenderScripts/tree/master/MassMakerToolbox/DuplicationUI
[MAUI]: https://github.com/atomicwest/BlenderScripts/tree/master/MassMakerToolbox/AnimationUI
[deathtrooper]: https://atomicprime.wordpress.com/2016/10/07/dynamic-linking-and-other-updates/
