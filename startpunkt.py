glyph = CurrentGlyph()
glyphdata = {'curve':[], 'offcurve':[], 'line':[]}
for contour in glyph:
    print (len(contour.points))
    for point in contour.points:
        glyphdata[point.type].append(point)
        # if point.type == 'curve':
        #     glyphdata['curve'].append(point)
        # elif point.type == 'offcurve':
        #     glyphdata['offcurve'].append(point)
        # elif point.type == 'line':
        #     glyphdata['line'].append(point)
        print (point.type)
        if point.index == 0:
            point.name = 'Starting Point'
            print (point.name)
            #print (point.name, glyph, point.font)
        elif point.index != 0:
            point.name = None
        if point.name == 'Starting Point':
            print ('x =',point.x, 'y =',point.y, point.type)
print (len(glyphdata['line']))
print (len(glyphdata['curve']))
print (len(glyphdata['offcurve']))

        # numberofpoints = point.index
        # #numberofpoints.append(point.index)
        # print (numberofpoints)
        # for item in numberofpoints:
        #     print (len(item))