'''Use Shift + c to open the base glyph of a selected component in a separate Glyph Window.'''

from mojo.UI import OpenGlyphWindow
from mojo.events import addObserver

class BaseGlyphJumper(object):

    def __init__(self):
        # add observer on key down
        addObserver(self, "keyDown", "keyDown")

    def keyDown(self, notification):
        # get the event
        event = notification["event"]
        # get the pressed character
        char = event.characters()
        # check it against a predefined character
        if char == "C": # capital 'c' --> shift 'c'
            # get the glyph
            glyph = notification["glyph"]
            # get the parent font
            font = glyph.font
            # loop over all components
            for component in glyph.components:
                # check if the component is selected
                if component.selected:
                    # check if the base glyph is in the font
                    if component.baseGlyph in font:
                        # get the base glyph as a glyph object
                        baseGlyph = font[component.baseGlyph]
                        # open a new glyph window with the base glyph
                        OpenGlyphWindow(baseGlyph, newWindow=True)

# go!
BaseGlyphJumper()