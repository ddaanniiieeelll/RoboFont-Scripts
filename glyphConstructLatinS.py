# MenuTitle: Glyph Construct Latin S

# delete icecream stuff before merging as it is just used for debugging
from icecream import ic

from glyphConstruction import ParseGlyphConstructionListFromString, GlyphConstructionBuilder

# Define the glyph construction recipe
# keep glyph constructions in a separate txt file to keep the script clean
with open('constructionRecipes/glyphConstructionLatinS.txt', 'r') as file:
    txt = file.read()

constructions = ParseGlyphConstructionListFromString(txt)

font = CurrentFont()

# collect glyphs to ignore if they already exist in the font
ignoreExisting = []
for glyph in font:
    for line in txt.split('\n'):
        if line:
            glyph_name = line.split('=')[0].strip()
            if glyph.name == glyph_name:
                ignoreExisting.append(glyph.name)

# delete icecream stuff before merging as it is just used for debugging
ic(ignoreExisting)

# iterate over glyph construction recipes
for construction in constructions:
    # build a glyph
    constructionGlyph = GlyphConstructionBuilder(construction, font)

    # if the glyph already exists in the font, skip it
    if constructionGlyph.name in font and constructionGlyph.name in ignoreExisting:
        continue

    # get destination glyph in font
    glyph = font.newGlyph(constructionGlyph.name, clear=True)

    # draw the glyph
    constructionGlyph.draw(glyph.getPen())

    # copy attributes to the glyph
    glyph.name = constructionGlyph.name
    glyph.unicode = constructionGlyph.unicode
    glyph.width = constructionGlyph.width
    glyph.markColor = 0.9958, 0.8001, 0.4, 1.0

    # if no unicode given, try to set automatically
    if glyph.unicode is None:
        glyph.autoUnicodes()