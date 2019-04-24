from vanilla import * 

class markGlyphs(object):
    def __init__(self):
        self.w = FloatingWindow((200, 165))
        self.w.button = Button((10, 10, -10, 20), "mark",
                            callback=self.toggleDrawer)
        self.d = Drawer((180, 120), self.w)
        self.d.componentsAndOutlinesButton = Button((10, 10, -10, 20), "comp. + outlines", callback=self.componentsAndOutlinesCallback)
        self.d.componentsButton = Button((10,40,-10,20), 'components', callback=self.componentsCallback)
        self.d.usedAsComponentButton = Button((10,70,-10,20), 'used as components', callback=self.usedAsComponentCallback)
        self.w.open()
        # self.d.open()
        
###        
    def toggleDrawer(self, sender):
        self.d.toggle()
        
    def componentsAndOutlinesCallback(self, sender):
        font = CurrentFont()
        glyph = CurrentGlyph()
        print('>>> Glyphs combining components and outlines:\n')
        for glyph in font:
            if len(glyph.contours) > 0 and len(glyph.components) > 0:
                glyph.prepareUndo('mark components and outlines')
                glyph.markColor = 1, 0, 0.5, 0.35
                glyph.performUndo()
                print(glyph.name, end=" ")
        print('\n')
        
                
    def componentsCallback(self,sender):
        font = CurrentFont()
        glyph = CurrentGlyph()
        print('>>> Glyphs completely made out of components:\n')
        for glyph in font:
            if len(glyph.contours) == 0 and len(glyph.components) > 0:
                glyph.prepareUndo('mark components')
                glyph.markColor = 0, 0.25, 0.5, 0.35
                glyph.performUndo()
                print(glyph.name, end = " ")
        print('\n')
        
    def usedAsComponentCallback(self, sender):
        font = CurrentFont()
        glyph = CurrentGlyph()

        print('>>> These glyphs are used as components\n')
        for component in glyph.components:
            baseGlyph = font[component.baseGlyph]
            print(component.baseGlyph)
            baseGlyph.prepareUndo('marks glyphs used as components')
            baseGlyph.markColor = 0.5, 0, 1, 0.35
            baseGlyph.performUndo()
        print('\n')
        
markGlyphs()