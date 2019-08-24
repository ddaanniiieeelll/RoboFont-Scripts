from vanilla import *
from mojo.UI import *
from defconAppKit.windows.baseWindow import BaseWindowController


class markingTool(BaseWindowController):

    def __init__(self):
        self.w = FloatingWindow((1800, 550, 310, 170), 'Marking Tool')

        self.w.checkBoxOverlaps = CheckBox((10,10,-10,20), 'Overlaps', callback=self.checkBoxOverlapsCallback)
        self.w.checkBoxComponents = CheckBox((10,40,-10,20), 'Components', callback=self.checkBoxComponentsCallback)
        self.w.checkBoxComponentsAndOutlines = CheckBox((10,70,-10,20), 'Components and Outlines', callback=self.checkBoxComponentsAndOutlinesCallback)
        # self.w.checkBoxUsedAsComponents = CheckBox((10,100,-10,20), 'Used as components')

        self.w.buttonCheck = Button((10, -30, 90, 15), 'Mark', sizeStyle = 'small', callback=self.checks)
        self.w.buttonGroup = Button((110, -30, 90, 15), 'Group', sizeStyle = 'small', callback=self.groups)
        self.w.buttonClose = Button((210, -30, 90, 15), 'Close', sizeStyle = 'small', callback=self.closeWindow)

        self.w.open()


    def closeWindow(self, sender):
        self.w.close()



    def checkBoxOverlapsCallback(self, sender):
        sender.get()

    def checkBoxComponentsCallback(self, sender):
        sender.get()

    def checkBoxComponentsAndOutlinesCallback(self, sender):
        sender.get()

    # def checkBoxUsedAsComponentsCallback(self, sender):
    #     sender.get()



    def checks(self, sender):
        if self.w.checkBoxOverlaps.get():
            self.progress = self.startProgress('looking for overlaps')
            self.checkOverlaps(f)
            self.progress.close()

        if self.w.checkBoxComponents.get():
            self.progress = self.startProgress('looking for components')
            self.checkComponents(f)
            self.progress.close()

        if self.w.checkBoxComponentsAndOutlines.get():
            self.progress =self.startProgress('looking for glyphs with components and outlines')
            self.checkComponentsAndOutlines(f)
            self.progress.close()

        # if self.w.checkBoxUsedAsComponents.get():
        #     self.progress = self.startProgress('looking where outline is used as component')
        #     # self.checkUsedAsComponents(f)
        #     self.progress.close()

    def groups(self, sender):
        if self.w.checkBoxComponents.get():
            self.progress = self.startProgress('looking for components')
            self.groupComponents(f)
            self.progress.close()

        if self.w.checkBoxComponentsAndOutlines.get():
            self.progress =self.startProgress('looking for glyphs with components and outlines')
            self.groupComponentsAndOutlines(f)
            self.progress.close()


        # self.w.close()

    def checkOverlaps(self, f):
        self.progress.setTickCount(len(f))
        print()
        print('>>> Glyphs with overlaps')
        print('------------------------')
        for glyph in f:
            self.progress.update()
            compareGlyph = glyph.copy()
            compareGlyph.removeOverlap()
            if len(glyph) != len(compareGlyph) or glyph.hasOverlap():
                # glyph.prepareUndo('mark overlaps')
                glyph.markColor = 0.5, 0, 0.2, 0.75
                # glyph.performUndo()
                print(glyph.name, end = ", ")

        # f.update()
        print()

    def checkComponents(self, f):
        self.progress.setTickCount(len(f))
        print()
        print('>>> Glyphs completely made out of components:')
        print('---------------------------------------------')
        for glyph in f:
            self.progress.update()
            if len(glyph.contours) == 0 and len(glyph.components) > 0:
                # glyph.prepareUndo('mark components')
                glyph.markColor = 0, 0.25, 0.5, 0.35
                # glyph.performUndo()
                print(glyph.name, end = ", ")

        # f.update()
        print()

    def checkComponentsAndOutlines(self, f):
        self.progress.setTickCount(len(f))
        print()
        print('>>> Glyphs combining components and outlines:')
        print('---------------------------------------------')
        for glyph in f:
            self.progress.update()
            if len(glyph.contours) > 0 and len(glyph.components) > 0:
                # glyph.prepareUndo('mark components and outlines')
                glyph.markColor = 1, 0, 0.5, 0.35
                # glyph.performUndo()
                print(glyph.name, end = ", ")

        # f.update()
        print()

    def groupComponents(self, f):
        self.progress.setTickCount(len(f))
        componentsGroup = SmartSet()
        componentsGroup.name = 'components'
        componentsGroup.query = 'Contours == 0 and Components > 0'
        addSmartSet(componentsGroup)
        updateAllSmartSets()

    def groupComponentsAndOutlines(self, f):

        self.progress.setTickCount(len(f))
        contoursAndComponentsGroup = SmartSet()
        contoursAndComponentsGroup.name = 'components and outlines'
        contoursAndComponentsGroup.query = 'Contours > 0 and Components >0'
        addSmartSet(contoursAndComponentsGroup)
        updateAllSmartSets()















f = CurrentFont()
markingTool()
