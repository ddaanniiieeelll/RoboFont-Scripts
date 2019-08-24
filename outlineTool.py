from vanilla import *
from mojo.UI import *
from defconAppKit.windows.baseWindow import BaseWindowController


class outlineTool(BaseWindowController):

    def __init__(self):
        self.w = FloatingWindow((1800, 500, 310, 170), 'Outline Tool')

        self.w.checkBoxOverlaps = CheckBox((10, 10, -10, 20), 'Remove overlaps', callback=self.checkBoxOverlapsCallback)
        self.w.checkBoxPS = CheckBox((10, 40, -10, 20), 'Set PS direction', callback=self.checkBoxPSCallback)
        self.w.checkBoxTT = CheckBox((10, 70, -10, 20), 'Set TT direction', callback=self.checkBoxTTCallback)

        self.w.buttonCurrent = Button((10, -30, 90, 15), 'Current glyph', sizeStyle = 'small', callback=self.currentCallback)
        self.w.buttonAll = Button((110, -30, 90, 15), 'All glyphs', sizeStyle = 'small', callback=self.allCallback)
        self.w.buttonClose = Button((210, -30, 90, 15), 'Close', sizeStyle = 'small', callback=self.closeWindow)



        self.w.open()


    def closeWindow(self, sender):
        self.w.close()

    def checkBoxOverlapsCallback(self, sender):
        sender.get()

    def checkBoxPSCallback(self, sender):
        sender.get()

    def checkBoxTTCallback(self, sender):
        sender.get()




    def currentCallback(self, sender):
        if self.w.checkBoxOverlaps.get():
            self.progress = self.startProgress('removing overlaps')
            self.removeCurrentOverlaps(f)
            self.progress.close()

        if self.w.checkBoxPS.get():
            self.progress = self.startProgress('setting PS direction')
            self.setCurrentPS(f)
            self.progress.close()

        if self.w.checkBoxTT.get():
            self.progress = self.startProgress('setting TT direction')
            self.setCurrentTT(f)
            self.progress.close()


    def allCallback(self, sender):
        if self.w.checkBoxOverlaps.get():
            self.progress = self.startProgress('removing overlaps')
            self.removeAllOverlaps(f)
            self.progress.close()

        if self.w.checkBoxPS.get():
            self.progress = self.startProgress('setting PS direction')
            self.setAllPS(f)
            self.progress.close()

        if self.w.checkBoxTT.get():
            self.progress = self.startProgress('setting TT direction')
            self.setAllTT(f)
            self.progress.close()






    def removeCurrentOverlaps(self, f):
        self.progress.setTickCount(len(f))
        print()
        print('>>> Removed overlap in')
        print('------------------------')
        self.progress.update()
        glyph = CurrentGlyph()
        compareGlyph = glyph.copy()
        compareGlyph.removeOverlap()
        if len(glyph) != len(compareGlyph) or glyph.hasOverlap():
            glyph.removeOverlap()
            print(glyph.name, end=', ')

        # f.update()
        print()

    def setCurrentPS(self, f):
        self.progress.setTickCount(len(f))
        print()
        print('>>> Set PS direction in')
        print('------------------------')
        self.progress.update()
        glyph = CurrentGlyph()
        for contour in glyph.contours:
            glyph.correctDirection(trueType=False)
        print(glyph.name, end=', ')

        # f.update()
        print()

    def setCurrentTT(self, f):
        self.progress.setTickCount(len(f))
        print()
        print('>>> Set TT direction in')
        print('------------------------')
        self.progress.update()
        glyph = CurrentGlyph()
        for contour in glyph.contours:
            glyph.correctDirection(trueType=True)
        print(glyph.name, end=', ')

        # f.update()
        print()


    def removeAllOverlaps(self, f):
        self.progress.setTickCount(len(f))
        print()
        print('>>> Removed overlap in')
        print('------------------------')
        for glyph in f:
            self.progress.update()
            compareGlyph = glyph.copy()
            compareGlyph.removeOverlap()
            if len(glyph) != len(compareGlyph) or glyph.hasOverlap():
                glyph.removeOverlap()
                print(glyph.name, end=', ')

        # f.update()
        print()

    def setAllPS(self, f):
        self.progress.setTickCount(len(f))
        print()
        print('>>> Set PS direction in')
        print('------------------------')
        for glyph in f:
            self.progress.update()
            for contour in glyph.contours:
                glyph.correctDirection(trueType=False)
            print(glyph.name, end=', ')

        # f.update()
        print()

    def setAllTT(self, f):
        self.progress.setTickCount(len(f))
        print()
        print('>>> Set TT direction in')
        print('------------------------')
        for glyph in f:
            self.progress.update()
            for contour in glyph.contours:
                glyph.correctDirection(trueType=True)
            print(glyph.name, end=', ')

        # f.update()
        print()



f = CurrentFont()
glyph = CurrentGlyph()
outlineTool()
