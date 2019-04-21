# RoboPython
Python Scripts for Robofont

## saveCopy
Creates a new .ufo in the same directory with the current date and time in the name.
Notice that you will stay in your original sourcefile.  
Added a shortCut so saving is more accessible.
Also the output window gives the path to the saveCopied .ufo (it should be next to the source, but just in case)

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

**ToDo:**  
- [ ] add undo option  
- [ ] come up with a good shortCut or menu button

*script is still in the development phase, no guarantee that it does what you want (or does anything at all), so use carefull and better use the saveCopy before messing with this thing.*
