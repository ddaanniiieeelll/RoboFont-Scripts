# Little helper scripts for RoboFont

## saveCopy
Creates a new .ufo in the same directory with the current date and time in the name.
Notice that you will stay in your original sourcefile.  
Added a shortCut so saving is more accessible.
Also the output window gives the path to the saveCopied .ufo (it should be next to the source, but just in case)

## highlightPointsAtMetricLine

Turning this on shows a red rectangle around those points that are exactly at the metric lines (ascender, descender, xHeight and baseline).  

~~## SoftOtterTool~~
~~Used as a Start-Up Script this adds a custom panel to the inspector containing the outlineTool and the markingTool.~~
Don’t use the soft otter tool atm, it’s a mess.  
-> removed from repo


## outlineTool
Let's you remove overlaps and set the direction of contours.

## markingTool
Marks glyphs with overlaps, glyphs made out of components and glyphs made out of outlines and components.  
*new feature: instead of marking them with a colour you can put them in smart sets*

## Mirror Tool
Using ctrl + m opens up a tiny window with two buttons. One for mirroring horizontal, one for vertical.
