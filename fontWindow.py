## Add observers so the list in the FontWindow
## gets updates when a font is opened/closed



from vanilla import FloatingWindow, Button, List
from mojo.roboFont import FontsList
from mojo.events import addObserver, removeObserver

class fontWindow(object):

    def __init__(self):

        fontsList = FontsList(AllFonts())
        fontsList.sortBy('openTypeOS2WeightClass')
        self.fontList = fontsList

        # addObserver(self, 'checks', 'fontDidOpen')


        padding = 10
        buttonHeight = 20
        columnFonts = 230
        columnGlyphs = 130
        listHeight = 240
        width = 280 + padding*3
        height = 240 + buttonHeight*2 + padding*4

        addObserver(self, 'updateWindow', 'fontWillOpen')
        addObserver(self, 'updateWindow', 'fontDidClose')



        self.w = FloatingWindow((width, height), 'FontWindow')

        x = y = padding
        # y += padding
        self.w.fonts = List (
            (x, y, width - padding*2, listHeight),
            [f.info.familyName + ' ' + f.info.styleName for f in self.fontList],
            selectionCallback=self.getFontsCallback,
            allowsMultipleSelection=False)



        self.w.buttonCheck = Button((10, -30, 90, 15), 'update', sizeStyle = 'small', callback=self.updateWindow)
        self.w.buttonClose = Button((110, -30, 90, 15), 'Close', sizeStyle = 'small', callback=self.closeWindow)
        self.w.buttonOpen = Button((210, -55, 90, 15), 'Open Font', sizeStyle = 'small', callback=self.openFont)
        self.w.buttonCloseFont = Button((210, -30, 90, 15), 'Close Font', sizeStyle = 'small', callback=self.closeFont)


        self.w.open()


    def getFontsCallback(self, sender):
        f = AllFonts()
        selectionList = sender.getSelection()
        for i in selectionList:
            num = i
        self.requestedFont = self.fontList[num]
        activeFontWindow = self.requestedFont.document().getMainWindow()
        activeFontWindow.show()

    def updateWindow(self, sender):
        self.w.close()
        removeObserver(self, 'fontWillOpen')
        removeObserver(self, 'fontDidClose')
        fontWindow()


    def closeWindow(self, sender):
        self.w.close()
        removeObserver(self, 'fontWillOpen')
        removeObserver(self, 'fontDidClose')

    def openFont(self, sender):
        f = OpenFont()

    def closeFont(self,sender):
        closeFontWindow = self.requestedFont.document().getMainWindow()
        closeFontWindow.close()






fontWindow()
