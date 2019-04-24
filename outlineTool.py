from vanilla import *
from mojo.UI import ProgressBar

class removeOverlaps(object):

    def __init__(self, parentWindow):
        self.w = Sheet((250, 100), parentWindow)
        self.w.removeButton = Button((10, 10, -10, 20), "remove overlap in current glyph", callback=self.removeCurrentButton)
        self.w.removeAllButton = Button((10, 40, -10, 20), "remove overlap in all glyphs", callback=self.removeAllButton)
        self.w.myTextBox = TextBox((10, 70, -10, 17), "removing the overlaps")
        self.w.closeButton = Button((-90, -30, 80, 22), "close", self.closeCallback)
        self.w.open()
        
        
## Callbacks

    def removeCurrentButton(self, sender):
        
        font = CurrentFont()
        glyph = CurrentGlyph()

        if glyph.hasOverlap():
            glyph.prepareUndo('remove overlap in current glyph')
            glyph.removeOverlap()
            glyph.markColor = None
            glyph.performUndo()
            print('removed overlap in:', glyph.name)
            self.w.close()
        
    def removeAllButton(self,sender):
        print('\nthis might take a while\n')
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
        self.w.close()

        



    def closeCallback(self, sender):
        self.w.close()

##############


class setDirection(object):

    def __init__(self, parentWindow):
        self.w = Sheet((250, 185), parentWindow) 
        self.w.setPSButton = Button((10, 10, -10, 20), 'set PS direction in current glyph', callback=self.setPSButton)
        self.w.setAllPSButton = Button((10, 40, -10, 20), 'set PS direction in all glyphs', callback=self.setAllPSButton)
        self.w.setTTButton = Button((10,70,-10, 20), 'set TT direction in current glyph', callback=self.setTTButton)
        self.w.setAllTTButton = Button((10, 100, -10, 17), 'set TT direction in all glyphs', callback=self.setAllTTButton)
        self.w.myTextBox = TextBox((10, 130, -10, 17), 'changing the paths direction')
        self.w.closeButton = Button((-90, -30, 80, 22), 'close', self.closeCallback)
        self.w.open()
        
        
## Callbacks

    def setPSButton(self, sender):
        
        font = CurrentFont()
        glyph = CurrentGlyph()


        for contour in glyph.contours:
            glyph.correctDirection(trueType=False)
        print('Corrected the direction of _%s_ following the PostScript recommendations' % glyph.name)
        glyph.changed()
        print()
        self.w.close()
        
    def setAllPSButton(self,sender):
        font = CurrentFont()
        glyph = CurrentGlyph()
        
        print('all outlines set to PS')
        for glyph in font:
            for contour in glyph.contours:
                glyph.correctDirection(trueType=False)
            glyph.changed()
        
        print()
        self.w.close()
        
    def setTTButton(self, sender):
        font = CurrentFont()
        glyph = CurrentGlyph()
        
        for contour in glyph.contours:
            glyph.correctDirection(trueType=True)
        print('Corrected the direction of _%s_ following the TrueType recommendations' % glyph.name)
        glyph.changed()
        print()
        self.w.close()

    def setAllTTButton(self,sender):
        font = CurrentFont()
        glyph = CurrentGlyph()
        
        print('all outlines set to TT')
        for glyph in font:
            for contour in glyph.contours:
                glyph.correctDirection(trueType=True)
            glyph.changed()
        
        print()
        self.w.close()



    def closeCallback(self, sender):
        self.w.close()





class outlineTool(object):

    def __init__(self):

        self.w = FloatingWindow((300, 75), title='Outline Tool')
        self.w.overlaps = Button((10, 10, -10, 22), "remove overlaps", callback=self.removeOverlapsCallback)
        self.w.direction = Button((10, 40, -10, 22), 'direction', callback=self.setDirectionCallback)
        self.w.open()

    def removeOverlapsCallback(self, sender):
        removeOverlaps(self.w) 
        
    def setDirectionCallback(self, sender):
         setDirection(self.w)

outlineTool()