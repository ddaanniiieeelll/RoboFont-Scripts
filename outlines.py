glyph = CurrentGlyph()
for contour in glyph:
    for point in contour.points:
        c = contour.index
        if point.index == 0:
            point.name = 'Starting Point'
            print ([c], point.name)
            #print (point.name, glyph, point.font)
        elif point.index != 0:
            point.name = None
        if point.name == 'Starting Point':
            print ('x =',point.x, 'y =',point.y, point.type, point.index)
                        
            # create a new empty path
            newPath()
            # set the first oncurve point
            moveTo((point.x, point.y))
            # line to from the previous point to a new point
            lineTo((100, 900))
            lineTo((900, 900))

            # curve to a point with two given handles
            curveTo((900, 500), (500, 100), (100, 100))

            # close the path
            closePath()
            # draw the path
            drawPath()
