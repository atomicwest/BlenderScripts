# Blender Scripts

### A growing library of tools for personal Blender projects.

Please visit my [blog][blog link] for more detailed discussions of my work.

![Deathtroopers](/Other/Images/deathtroopers.png "Deathtroopers from Rogue One")

## Mass Maker Toolbox
Set of tools developed mainly for handling hundreds of objects in my [Yavin-Hoth Hyperspace 360 VR][VR] project.
These include the asteroid field and hyperspace transition stars. The scripts have been tested for thousands of objects and can support as many as your hardware can handle, depending on the complexity and detail of your objects.
 
* [Standalone][saFolder] - Run these scripts directly from the Blender editor for specific actions; these serve the same purpose as the two UI sections below.
  * Select Many Objects - [Script][selection] - Selects all objects in the scene that have the same name scheme as entered in the UI field
  * Assign Textures - [Script][textures] - Assigns a material to objects based on the object name; e.g. all objects with "light" in their name will be assigned the "Limb-light" material. Can be generalized to match any criteria depending on existing textures.
  * Duplicate Many Objects - [Script][dupobj] - Make copies of the selected mesh; the copies will fill 3D space in a spherically radial pattern, with randomized locations, rotations, and scaling based on three factors (rfL, rfR, rfS). The script can be easily edited for duplicating objects in specific patterns, e.g. an asteroid field.
  * Animate Many Objects - [Asteroid Field][asteroidAnim]: Current version hardcoded to duplicating "Asteroid"-named objects with a Z-axis limitation, simulating an accretion disk. See script comment for more details.
  * Duplicate Matching - [Script][matcher] - Duplicates the selected mesh and positions each object at the center of a target set of objects. E.g. if you wanted to make copies of hundreds of candles and automatically position each in the middle of hundreds of lanterns.
  * Swap Left-to-Right Naming - [Script][LtoR]: Intended for mesh objects that are mirrored across an axis of symmetry. This specifically targets a naming convention such as "legArmor\_L.001" or "legArmor\_L_001"
  * Duplicate Floorboards
  * Remove Frames From Many - [RemoveMany][remmany]: Remove key frames from objects and set frame for the freeze position

* [Single Direction Duplication UI][SDUI]
  * Duplicates an object along one vector with the same magnitude applied to all axes.
  * You can modify the operator to take 3 separate values for each axis
  
* [Mass Duplication UI][MDUI]
  * The most recent version should be fixed for the float issue on randomizing scaling, but sometimes freezes on certain Blender setups, e.g. a machine with no GPU and 4GB of RAM.
  * Previous versions of the UI script may have a base class called View3dPanel, which I believe is deprecated - omit when applicable, defined like so:
```python
class ManyDuplicate(View3dPanel, bpy.types.Operator):
    """ Mass Produce the Current Object"""
    bl_idname = "myops.massmake"
```


* [Mass Selection UI][selectionUI]
  * By default selects all objects in the scene, then selects all objects that match the "Duplicate Name" UI field

* [Parent Many UI][parentmanyUI]
  * Select the parent object first, then run the script and enter the children name scheme to complete parenting
  
* [Add Dynamics to Many UI][adddyn]
  * After duplicating and selecting target objects, run this to add rigid body properties to target objects/add target objects to Blender's rigid body world. Current UI allows toggling Friction, Bounciness, and Collision Margin, but can be modified to address any other rigid body properties. 

![Dynamics](/Other/Images/improved_dynamics.gif "Working demo of dynamics script")

* [Apply Modifiers][allmods]
  * Choose between applying all modifiers beginning with the top of the stack downward, or specifying a modifier to be applied. Either way, the script will iterate through all objects in the scene and make the appropriate changes.

* [Set All Origins to Center of Mass][centerall]
  * Example use: If you start with a primitive then create separate pieces out of the primitive faces, the origin of each piece will still be the original primitive's origin. Run this script to set each pieces' origin to their center of mass. More information [here][allcenterlink]

* [Mass Animation][MAUI] 
  * Current versions of translation/rotation/scaling animation UI do not work well as a UI, it is better to modify the standalone asteroid animation script and run directly for now.

* [Rename Many][RMany] | [Standalone Version][RStand]
  * Renames objects based on target and replacement naming patterns

* Old subfolder contains deprecated versions of scripts mentioned above.
  * E.g. dupobj_vent.py was used to create several vent plates for the [Deathtrooper][deathtrooper] helmet project.

## Other

* [Select Inverse](/Other/select_inverse.py)
* [Manual Render](/Other/manual_render.py) - Run with RenderMan or any renderer that does not respond to the "Render Animation" command correctly. RenderMan has its own pipeline and as of this writing, I have only managed to produce .exr files.
* Sun and Sky Environment Link script from this [tutorial](https://www.youtube.com/watch?v=YXso7kNzxIU)

[VR]: https://www.youtube.com/watch?v=thC53_FVSao
[blog link]: https://atomicprime.wordpress.com
[dupobj]: /MassMakerToolbox/standalone/duplicate_many_objects.py
[matcher]: /MassMakerToolbox/standalone/duplicate_matching.py
[asteroidAnim]: /MassMakerToolbox/standalone/asteroid_animate.py
[saFolder]: /MassMakerToolbox/standalone
[MDUI]: /MassMakerToolbox/DuplicationUI
[SDUI]: /MassMakerToolbox/DuplicationUI/simple_copy.py
[MAUI]: /MassMakerToolbox/AnimationUI
[deathtrooper]: https://atomicprime.wordpress.com/2016/10/07/dynamic-linking-and-other-updates/
[selection]: /MassMakerToolbox/standalone/select_many_objects.py
[selectionUI]: /MassMakerToolbox/DuplicationUI/select_many_objects_UI.py
[adddyn]: /MassMakerToolbox/AnimationUI/add_dynamics_to_many_UI.py
[parentmanyUI]: /MassMakerToolbox/DuplicationUI/parent_many_objects_UI.py
[remmany]: /MassMakerToolbox/standalone/remove_frames_from_many.py
[centerall]: /MassMakerToolbox/DuplicationUI/origin_to_centerofmass.py
[allcenterlink]: https://atomicprime.wordpress.com/2016/12/30/quick-python/
[allmods]: /MassMakerToolbox/DuplicationUI/apply_all_mods.py
[LtoR]: /MassMakerToolbox/standalone/swap_L-R_name.py
[textures]: /MassMakerToolbox/standalone/apply_texture.py
[RMany]: /MassMakerToolbox/DuplicationUI/rename_many.py
[RStand]: /MassMakerToolbox/standalone/rename_by_selection.py


