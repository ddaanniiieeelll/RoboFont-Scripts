# MenuTitle: Add Anchors

font = CurrentFont()

marks_top = ["acutecmb", "gravecmb", "circumflexcmb", "tildecmb", "macroncmb", "brevecmb", "dotaccentcmb", "dieresiscmb", "ringabovecmb", "hungarumlautcmb", "caroncmb", "commaturnedabovecmb"]
marks_bottom = ["dotbelowcmb","commaaccentbelowcmb","cedillacmb"]
lc_top = ["a", "c", "e", "g", "i", "dotlessi", "dotlessj", "n", "o", "p", "r", "s", "u", "w", "x", "y", "z"]
lc_asc = ["b","d","h","k","l","t"]
uc_top = ["A", "B", "C", "D", "E", "G", "H", "I", "J", "K", "L", "N", "O", "P", "R", "S", "T", "U", "W", "X", "Y", "Z"]
bottom = ["A", "B", "C", "D", "E", "G", "H", "I", "K", "L", "N", "O", "R", "S", "T", "U", "Z", "a", "b", "c", "d", "e", "h", "i", "k", "l", "n", "o", "r", "s", "u", "z"]
bottom_dsc = ["g"]

def addAnchors(name: str, glyphList: list, yPosition: int):
    anchorname = name
    verticalPosition = yPosition

    for i in glyphList:
        if i not in font:
            continue
        glyph = font[i]
        width = glyph.width

        if width is None:
            continue
        horizontalPosition = width / 2

        with glyph.undo("add Anchors"):
            if glyph is None:
                continue
            glyph.appendAnchor(anchorname, (horizontalPosition, verticalPosition))

addAnchors("_top", marks_top, font.info.xHeight)
addAnchors("_bottom", marks_bottom, 0)
addAnchors("top", lc_top, font.info.xHeight)
addAnchors("top", lc_asc, font.info.ascender)
addAnchors("top", uc_top, font.info.capHeight)
addAnchors("bottom", bottom, 0)
addAnchors("bottom", bottom_dsc, font.info.descender)
