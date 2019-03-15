# f1 = AllFonts().getFontsByStyleName('round')[0]
# f2 = AllFonts().getFontsByStyleName('rect')[0]
# print(f1['a'].isCompatible(f2['a']))

# from random import randint
# font = CurrentFont()
# glyph1 = font['a']
# glyph1.clear()
# pen = glyph1.getPen()
# pen.moveTo((0, 0))
# pen.lineTo((0, 200))
# pen.curveTo((50, 150), (150, 150), (200, 200))
# pen.lineTo((200, 0))
# pen.closePath()

# glyph = CurrentGlyph()
# for contour in glyph:
#         for point in contour.points:
#             #print (point)
#             print (point.index)
#             if point.index == 0:
#                 print (point.x)
#                 print (point.y)

f1 = AllFonts().getFontsByStyleName('round')
f2 = AllFonts().getFontsByStyleName('rect')
# def StartPoint():
glyph = CurrentGlyph()
for contour in glyph:
    for point in contour.points:
        if point.index == 0:
            point.name = 'Starting Point'
            print (point.name)
            #print (point.name, glyph, point.font)
        elif point.index != 0:
            point.name = None
        if point.name == 'Starting Point':
            print ('x =',point.x, 'y =',point.y, point.type)
            
###Anzahl der Punkte, Vergleich smooth true/false mit anderer glyphe

        # numberofpoints = point.index
        # #numberofpoints.append(point.index)
        # print (numberofpoints)
        # for item in numberofpoints:
        #     print (len(item))