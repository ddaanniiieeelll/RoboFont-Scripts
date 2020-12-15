
# Move points inside a glyph (for example to quickly generate .case)
f = CurrentFont()

# get all the selected glyphs
for glyph in f.selectedGlyphs:

    # set undo state
    glyph.prepareUndo('move points')

    # loop over all contours in the glyphs
    for contour in glyph:
        # loop over all points in contour
        for point in contour.points:
            # move all points in a direction by a specified amount of units
            point.x += 0
            point.y += 70

    # update glyph
    glyph.changed()

    # restore undo state
    glyph.performUndo()
    print(glyph)
