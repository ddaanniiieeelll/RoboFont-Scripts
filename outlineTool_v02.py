from vanilla import *
from mojo.UI import *
from defconAppKit.windows.baseWindow import BaseWindowController


class outlineTool(BaseWindowController):

    def __init__(self):
        self.w = FloatingWindow((1800, 500, 310, 170), 'Outline Tool')

        self.w.checkBoxOverlaps = CheckBox((10, 10, -10, 20), 'Remove overlaps')
        self.w.checkBoxPS = CheckBox((10, 40, -10, 20), 'Set PS direction')
        self.w.checkBoxTT = CheckBox((10, 70, -10, 20), 'Set TT direction')

        self.w.buttonCurrent = Button((10, -30, 90, 15), 'Current glyph', sizeStyle = 'small')
        self.w.buttonAll = Button((110, -30, 90, 15), 'All glyphs', sizeStyle = 'small')
        self.w.buttonClose = Button((210, -30, 90, 15), 'Close', sizeStyle = 'small', callback=self.closeWindow)



        self.w.open()


    def closeWindow(self, sender):
        self.w.close()

outlineTool()
