# RoboPython
Python Scripts for Robofont

## saveCopy
Creates a new .ufo in the same directory with the current date and time in the name.
Notice that you will stay in your original sourcefile.  
Added a shortCut so saving is more accessible.
Also the output window gives the path to the saveCopied .ufo (it should be next to the source, but just in case)

## SoftOtterTool
Used as a Start-Up Script this adds a custom panel to the inspector containing the outlineTool and the markingTool.

**Note:** As I described in my [post](https://forum.robofont.com/topic/631/hasoverlap-does-not-detect-all-overlaps) in the RF Forum, there is no overlap detected when the outline goes through 2 points. Therefore the *Remove overlap* button in this tool will not work in that case. The built-in remove overlap function in the context menu of the glyph however works as expected.  
I'll try to find a way to work this out.  
**Edit:** following my initial post [gferreira](https://github.com/gferreira) filed an [issue](https://github.com/typemytype/booleanOperations/issues/54). As [typemytype](https://github.com/typemytype) explains  `getIntersections()` just returns new points. In this case there are no *new* points, but the already existing points are used.

## outlineTool
A set of handy functions
- **mark all glyphs with overlaps**  
checks all glyphs and marks the ones with overlaps
- **remove overlaps in current glyph**  
removes the overlaps in the current glyph
- **remove overlaps in all glyphs**  
removes the overlaps in all glyphs
- **set current glyph to PS direction**  
sets the contour of the current glyph to PS direction
- **set all glyphs to PS direction**  
sets the contours of all the glyphs to PS direction
- **set current glyph to TT direction**  
sets the contour of the current glyph to TT direction
- **set all glyphs to TT direction**  
sets the contours of all the glyphs to TT direction

## markingTool
Tool to mark certain glyphs   
- **composites and outlines**  
marks glyphs that contain both, components and outlines  
- **components**  
marks glyphs that only consist of components  
- **used as components**  
marks the glyphs that are used as components in the current glyph

Additionally the markingTool now has an option to create Smart Sets that include the glyphs with components and outlines and glyphs that are completely made of components. 
