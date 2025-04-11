# MenuTitle: Make NULL, CR, 00A0 and FEFF

# Add Control gyphs NULL, CR, 00A0 and FEFF to font.


f = CurrentFont()

# define glyph names
newGlyphs = ['NULL', 'CR', 'uni00A0', 'zerowidthnobreakspace']

# check if glyphs are already present and delete them
for glyphName in newGlyphs:
    if glyphName in f:
        del f[glyphName]

# create the new glyphs
for glyphName in newGlyphs:
    f.newGlyph(glyphName)
    
# give CR and 00A0 the same width as space
f['CR'].width = f['space'].width
f['uni00A0'].width = f['space'].width

# add proper unicodes
unicode_dict = {
    'NULL': 0,
    'CR': 13,
    'uni00A0': 160,
    'zerowidthnobreakspace': 65279
}

for k, v in unicode_dict.items():
    f[k].unicode = v
    
print('Added NULL, CR, uni00A0 and FEFF to font.\nPlease sort again.')