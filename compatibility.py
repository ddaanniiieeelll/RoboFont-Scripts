import pprint
pp = pprint.PrettyPrinter(indent=2)
glyph = CurrentGlyph()
glyphdata = {'curve':[], 'offcurve':[], 'line':[]}
comparedata = {
    'contours':len(glyph),
    'segments':0,
    'points':{
        'curve':0,
        'offcurve':0,
        'line':0
    },
    'contourdata':[]
}
for contour in glyph:
    thiscontourdata = {'index':contour.index, 'points':[], 'clockwise':contour.clockwise}
    #print (dir(contour))
    print (contour.clockwise)
    for segment in contour:
        comparedata['segments'] +=1
        #print (segment)
    for point in contour.points:
        comparedata['points'][point.type]+=1
        thiscontourdata['points'].append(point.type)
        # if point.type == 'curve':
        #     glyphdata['curve'].append(point)
        # elif point.type == 'offcurve':
        #     glyphdata['offcurve'].append(point)
        # elif point.type == 'line':
        #     glyphdata['line'].append(point)
        #print (point.type)
        if point.index == 0:
            point.name = 'Starting Point'
            print (point.name)
            #print (point.name, glyph, point.font)
        elif point.index != 0:
            point.name = None
        if point.name == 'Starting Point':
            print ('x =',point.x, 'y =',point.y, point.type)
    comparedata['contourdata'].append(thiscontourdata)
pp.pprint (comparedata)


        # numberofpoints = point.index
        # #numberofpoints.append(point.index)
        # print (numberofpoints)
        # for item in numberofpoints:
        #     print (len(item))