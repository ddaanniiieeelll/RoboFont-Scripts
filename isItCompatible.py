
from random import random, randint
from vanilla import FloatingWindow, CheckBox, Button
from mojo.events import addObserver, removeObserver
from mojo.drawingTools import *
from defconAppKit.windows.baseWindow import BaseWindowController

f = CurrentFont()
# master = OpenFont(showInterface=False)

cG = CurrentGlyph()

class isItCompatible(BaseWindowController):

    def __init__(self):
        
        self.master = None

        
        self.w = FloatingWindow((155, 80), "Is it compatible?")

        # a checkbox to turn the tool on/off
        self.w.showPoints = CheckBox((10, 10, -10, 20), 'show me', value=False)
        self.w.selectMaster = Button((10, 40, -10, 20 ), 'select master', callback=self.selectMaster)
        

        # add an observer to the drawPreview event
        addObserver(self, "highlightPoints", "draw")

        # open window
        self.setUpBaseWindowBehavior()
        self.w.open()
        
    def selectMaster(self, sender):
        self.master = OpenFont(showInterface=False)

    def windowCloseCallback(self, sender):
        # remove observer when window is closed
        removeObserver(self, 'draw')
        super(isItCompatible, self).windowCloseCallback(sender)
        if self.master is not None:
            self.master.close()

    def highlightPoints(self, info):
        # check if checkbox is selected
        if not self.w.showPoints.get():
            return

        # get the current glyph
        glyph = info["glyph"]
        if self.master is None:
            return        
        masterGlyph = self.master['%s' % (glyph.name)]
        sc = info['scale']

        asc = f.info.ascender
        xhe = f.info.xHeight
        cap = f.info.capHeight
        dsc = f.info.descender
        size = 7 * sc
        # draw highlight
        # print(glyph.name)
        stroke(None)
        translate(cG.width)
        
       
        if glyph is not None:
            for c in masterGlyph:
                for s in c:
                    for p in s:
                        #if p.y == asc or p.y == xhe or p.y == cap or p.y == dsc or p.y == 0:

                            # fill(1, 0, 0, .6)
                            
                        fill(None)
                        stroke(0, 0.8, 0.8, .8)
                        strokeWidth(2 * sc)
                        
                        drawGlyph(masterGlyph)
                        if p.type == 'offcurve':
                            stroke(None)
                            strokeWidth(0)
                        if p.index == 0:
                            stroke(1, 0, 0, .8)
                            line((p.x, p.y), (p.x - size * 2, p.y - size * 2))
                        if p.smooth is False:
                            rect(p.x-size/2, p.y-size/2, size, size)
                        if p.smooth is True:
                            oval(p.x-size/2, p.y-size/2, size, size)
                        
                        
                        
                        
                        

isItCompatible()
