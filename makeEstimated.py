# MenuTitle: Draw estimated glyph

f = CurrentFont()

est = f.newGlyph('estimated')
est.clear()

pen = est.getPen()

pen.moveTo((463, 0))
pen.curveTo((625, 0), (725, 72), (770, 135))
pen.lineTo((702, 135))
pen.curveTo((649, 71), (561, 26), (463, 26))
pen.curveTo((370, 26), (294, 60), (236, 117))
pen.curveTo((224, 128), (221, 141), (221, 161))
pen.lineTo((221, 327))
pen.curveTo((221, 334), (227, 340), (235, 340))
pen.lineTo((845, 340))
pen.curveTo((845, 534), (705, 700), (463, 700))
pen.curveTo((224, 700), (80, 547), (80, 349))
pen.curveTo((80, 147), (231, 0), (463, 0))
pen.closePath()

pen.moveTo((235, 361),)
pen.curveTo((227, 361), (221, 366), (221, 374))
pen.lineTo((221, 540))
pen.curveTo((221, 559), (224, 570), (236, 581))
pen.curveTo((294, 639), (370, 674), (463, 674))
pen.curveTo((540, 674), (619, 649), (687, 581))
pen.curveTo((700, 570), (703, 559), (703, 540))
pen.lineTo((703, 374))
pen.curveTo((703, 366), (697, 361), (689, 361))
pen.lineTo((235, 361))
pen.closePath()

est.rightMargin = 80

x = 700
y = f.info.capHeight

if x == y:
    pass
else:
    scale = y / x
    est.scaleBy((scale, scale))
    est.leftMargin = 80
    est.rightMargin = 80

print(scale)

est.changed()
