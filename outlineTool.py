from vanilla import FloatingWindow, Button
from mojo.UI import Message
from mojo.roboFont import OpenWindow

class outlineTool(object):

    def __init__(self):
        

        self.w = FloatingWindow((250, 230), 'Outline Tool')

        x = y = padding = 10
        buttonHeight = 21

        self.w.markButton = Button(
                (x, y, -padding, buttonHeight),
                'mark all glyphs with overlaps',
                callback=self.markButtonCallback)

        y += buttonHeight + padding

        self.w.removeButton = Button(
                (x, y, -padding, buttonHeight),
                'remove overlaps in current glyph',
                callback=self.removeButtonCallback)
        
        y += buttonHeight + padding
                
        self.w.removeAllButton = Button(
                (x, y, -padding, buttonHeight),
                '\U0001F92F remove overlaps in all glyphs',
                callback=self.removeAllButtonCallback)
                
        y += buttonHeight + padding
                
        self.w.setPSButton = Button(
                (x, y, -padding, buttonHeight),
                'set to PS direction',
                callback=self.setPSCallback)
                
        y += buttonHeight + padding
        
        self.w.setAllPSButton = Button(
                (x, y, -padding, buttonHeight),
                'set all glyphs to PS direction',
                callback=self.setAllPSCallback)
                
        y += buttonHeight + padding
                
        self.w.setTTButton = Button(
                (x, y, -padding, buttonHeight),
                'set to TT direction',
                callback=self.setTTCallback)

        y += buttonHeight + padding
                
        self.w.setAllTTButton = Button(
                (x, y, -padding, buttonHeight),
                'set all glyphs to TT direction',
                callback=self.setAllTTCallback)
        
        self.w.open()

    def markButtonCallback(self, sender):
        'mark all glyphs with overlaps'
        
        print('glyphs with overlaps:')
        font = CurrentFont()
        glyph = CurrentGlyph()
        glyphsWithOverlap = []
        for glyph in font:
            if glyph.hasOverlap():
                glyph.prepareUndo('mark glyphs with overlaps')
                glyphsWithOverlap.append(glyph.name)
                glyph.markColor = 1, 0, 1, 0.5
                glyph.performUndo()

                
                
        if not glyphsWithOverlap:
            print('there are no overlaps anymore')
            
        print(glyphsWithOverlap)
        print()

    def removeButtonCallback(self, sender):
        'Remove overlap in current glyph'

        font = CurrentFont()
        glyph = CurrentGlyph()

        if glyph.hasOverlap():
            glyph.prepareUndo('remove overlap in current glyph')
            glyph.removeOverlap()
            glyph.markColor = None
            glyph.performUndo()
            print('removed overlap in:', glyph.name)
        
            
    def removeAllButtonCallback(self, sender):
        'Remove overlap in all glyphs'
        
        font = CurrentFont()
        glyph = CurrentGlyph()
    
        print('removed overlap in:')
        for glyph in font:
            if glyph.hasOverlap():
                glyph.prepareUndo('remove overlap in current glyph')
                glyph.removeOverlap()
                glyph.markColor = None
                glyph.performUndo()
                print(glyph.name)
        
        
        print()
    
    def setPSCallback(self, sender):
        'Set contour direction to PS recommendations in current glyph'
        
        font = CurrentFont()
        glyph = CurrentGlyph()


        for contour in glyph.contours:
            glyph.correctDirection(trueType=False)
        print('Corrected the direction of _%s_ following the PostScript recommendations' % glyph.name)
        glyph.changed()
        
        print()
        
    def setAllPSCallback(self, sender):
        'Set contour direction to PS recommendations in all glyphs'
        
        font = CurrentFont()
        glyph = CurrentGlyph()
        
        print('all outlines set to PS')
        for glyph in font:
            for contour in glyph.contours:
                glyph.correctDirection(trueType=False)
            glyph.changed()
        
        print()

    
    def setTTCallback(self, sender):
        'Set contour direction to TT recommendations in current glyph'
        
        font = CurrentFont()
        glyph = CurrentGlyph()


        for contour in glyph.contours:
            glyph.correctDirection(trueType=True)
        print('Corrected the direction of _%s_ following the TrueType recommendations' % glyph.name)
        glyph.changed()
        
        print()
        
    
    def setAllTTCallback(self, sender):
        'Set contour direction to TT recommendations in all glyphs'
        
        font = CurrentFont()
        glyph = CurrentGlyph()
        
        print('all outlines set to TT')
        for glyph in font:
            for contour in glyph.contours:
                glyph.correctDirection(trueType=True)
            glyph.changed()
        
        print()


if __name__ == '__main__':

    OpenWindow(outlineTool)