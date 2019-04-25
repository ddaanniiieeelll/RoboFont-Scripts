from vanilla import * 
from mojo.UI import *

class markGlyphs(object):
    def __init__(self):
        # The Tool Window
        self.w = FloatingWindow((200, 195), 'Marking Tool')
        self.w.buttonMark = Button((10, 10, -10, 20), '<- mark', callback=self.toggleMarkDrawer)
        self.w.buttonGroup = Button((10, 40, -10, 20), 'make group ->', callback=self.toggleGroupDrawer)
        # mark drawer
        self.d = Drawer((180, 160), self.w)
        self.d.componentsAndOutlinesButton = Button((10, 10, -10, 20), 'comp. + outlines', callback=self.componentsAndOutlinesCallback)
        self.d.componentsButton = Button((10,40,-10,20), 'components', callback=self.componentsCallback)
        self.d.usedAsComponentButton = Button((10,70,-10,20), 'used as components', callback=self.usedAsComponentCallback)
        self.d.hasOverlapButton = Button((10,100,-10,20), 'has overlaps', callback=self.hasOverlapCallback)
        # group drawer
        self.g = Drawer((180, 120), self.w, preferredEdge = 'right')
        self.g.componentsAndOutlinesGroupButton = Button((10, 10, -10, 20), 'comp. + outlines', callback=self.componentsAndOutlinesGroupCallback)
        self.g.componentsGroupButton = Button((10, 40, -10, 20), 'components', callback=self.componentsGroupCallback)
        # self.g.usedAsComponentsGroupButton = Button((10,70,-10,20), 'used as components', callback=self.usedAsComponentsGroupCallback)
        
        self.w.open()
        # self.d.open()
        
##### Callbacks
    # open mark drawer       
    def toggleMarkDrawer(self, sender):
        self.d.toggle()
    # open group drawer
    def toggleGroupDrawer(self, sender):
        self.g.toggle()
    ##### mark Callbacks    
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
        
    def hasOverlapCallback(self, sender):
        font = CurrentFont()
        glyph = CurrentGlyph()

        for glyph in font:
            if glyph.hasOverlap():
                print(glyph.name)
                glyph.prepareUndo('mark overlaps')
                glyph.markColor = 0.5, 0, 0.2, 0.75
                glyph.performUndo()
            
        
    ##### group Callbacks
    def componentsAndOutlinesGroupCallback(self, sender):
        contoursAndComponentsGroup = SmartSet()
        contoursAndComponentsGroup.name = 'components and outlines'
        contoursAndComponentsGroup.query = 'Contours > 0 and Components >0'
        addSmartSet(contoursAndComponentsGroup)
        updateAllSmartSets()
        
    def componentsGroupCallback(self, sender):
        componentsGroup = SmartSet()
        componentsGroup.name = 'components'
        componentsGroup.query = 'Contours == 0 and Components > 0'
        addSmartSet(componentsGroup)
        updateAllSmartSets()
        
    # def usedAsComponentsGroupCallback(self, sender):
    #     usedAsComponentsGroup = SmartSet()
    #     usedAsComponentsGroup.name = 'used as components'
    #     usedAsComponentsGroup.query = 'Color = 0.5, 0, 1, 0.35'
    #     addSmartSet(usedAsComponentsGroup)
    #     updateAllSmartSets()
    
    
        
markGlyphs()