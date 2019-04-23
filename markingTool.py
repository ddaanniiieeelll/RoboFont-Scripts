from vanilla import *
from mojo.events import addObserver

class CustomInspectorExample(object):

    def __init__(self):
        # subscribe to the moment when an inspector will be shown
        addObserver(self, "inspectorWindowWillShowDescriptions", "inspectorWindowWillShowDescriptions")
        # subscribe to the moment when a glyph window will be shown
        # addObserver(self, "glyphWindowWillShowToolbarItems", "glyphWindowWillShowToolbarItems")
        # subscribe to the moment when a font window will be shown
        # addObserver(self, "fontWindowWillShowToolbarItems", "fontWindowWillShowToolbarItems")
        # keep a reference of the view inserted in the inspector
        # self.chose = Group((0, 0, -0, -0))
        # self.chose.PopUpButton = PopUpButton((10, 40, 100, 22), 'Test1')
        # self.chose.checkBox = CheckBox((10, 70, -10, -0), 'check')
        # self.editor = Button((10, 10, -10, -0), 'mark glyphs with components and outlines', callback=self.markComponentsAndOutlines)
        self.editor = Group((0,0,-0,-0))
        self.editor.Button = Button((10,10,-10,-0), 'mark them', callback=self.markComponentsAndOutlines)
        self.editor.PopUpButton = PopUpButton((10,60,-10,-0), ['check', 'test'])



    def markComponentsAndOutlines(self, sender):
        font = CurrentFont()
        glyph = CurrentGlyph()

        for glyph in font:
            if len(glyph.contours) > 0 and len(glyph.components) > 0:
                glyph.markColor = 1, 0, 0.5, 0.35
            # elif len(glyph.components)>0:
            #     glyph.markColor = 0, 0.25, 0.5, 0.35
    



    def inspectorWindowWillShowDescriptions(self, notification):
        # create an inspector item
        item = dict(label="Marking Tool", view=self.editor, size = 100, collapsed=False)
        # insert or append the item to the list of inspector panes
        notification["descriptions"].insert(1, item)

    # def glyphWindowWillShowToolbarItems(self, notification):
    #     # create a toolbar item
    #     item = dict(itemIdentifier="customGlyphToolbar", label="Do It", callback=self.doIt, imageNamed="toolbarRun")
    #     # insert or append the item to the list of glyph window toolbar items
    #     notification["toolbarItems"].insert(5, item)

    # def fontWindowWillShowToolbarItems(self, notification):
    #     # create a toolbar item
    #     item = dict(itemIdentifier="customFontToolbar", label="Do It", callback=self.doIt, imageNamed="toolbarRun")
    #     # insert or append the item to the list of font window toolbar items
    #     notification["toolbarItems"].insert(2, item)

    def doIt(self, sender):
        print("do it")

CustomInspectorExample()