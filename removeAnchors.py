# MenuTitle: Remove Anchors from selected glyphs

def removeAnchors():
    anchor = False
    for glyphName in font.selectedGlyphNames:
        glyph = font[glyphName]
        if len(glyph.anchors) > 0:
            glyph.clearAnchors()
            glyph.glyphChangedUpdate()
            anchor = True

    if anchor is True:
        print("Anchors removed")
    else:
        print("Selected glyphs had no anchors.")

font = CurrentFont()
if not len(font.selectedGlyphs):
    print("No glyphs selected.")
else:
    removeAnchors()