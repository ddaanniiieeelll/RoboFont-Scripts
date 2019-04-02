font = CurrentFont()
glyph = font['e']
print (glyph)
stroke(0.7)               
line((214,548), (386,548))

fill(None)
stroke(0,0,0,0.5)
strokeWidth(2)
drawGlyph(glyph)
# stroke(1,0,0,1)
for contour in glyph:
    for segment in contour:
        for point in segment:
            #print (point.type)
            if point.type == 'line':
                fill(0,0,0.8,1)
                rect(point.x-5, point.y-5, 10, 10)
            elif point.type == 'curve':
                fill(0,0.5,0,1)
                oval(point.x-5, point.y-5, 10, 10)
            else:
                fill(0.8,0,0,1)
                stroke(0,0,0,0)
                oval(point.x-3, point.y-3, 6, 6)
