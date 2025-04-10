# MenuTitle: Decompose all components

font = CurrentFont()

decomposed: list[str] = []

for glyph in font:
    if glyph.components:
        glyph.decompose()
        decomposed.append(glyph.name)
        
print(f"Decomposed {len(decomposed)} glyphs:")
for glyphname in decomposed:
    print(f"    {glyphname}")