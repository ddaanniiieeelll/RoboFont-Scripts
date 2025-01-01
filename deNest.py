# menuTitle: De-Nest selected Components

# Script originally from Okay-Type
# https://gist.github.com/okay-type/c8b09f538521d2accb287c1205162c92

f = CurrentFont()

for g in f.selectedGlyphs:
    if len(g.components) > 0:
        with g.undo('de-nest ' + g.name):
            for c in g.components:
                baseGlyph = f[c.baseGlyph]
                if len(baseGlyph.components) > 0:
                    pen = g.getPointPen()
                    baseGlyph.drawPoints(pen)
                    g.removeComponent(c)
                else:
                    component.decompose()