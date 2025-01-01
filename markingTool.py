#menuTitle: 🖍 Marking Tool

import ezui

class markingTool(ezui.WindowController):

    def build(self):
        content = """
        (Mark Components)   @button1
        (Nested Components) @button2
        """
        self.w = ezui.EZWindow(
            title="Mark Glyphs",
            content=content,
            controller=self
        )

    def started(self):
        self.w.open()

    def checkComponents(self, f):
        for glyph in f:
            if len(glyph.contours) == 0 and len(glyph.components) > 0:
                glyph.markColor = 0.8, 1, 0.4, 0.75

    def nestedComponents(self, f):
        for glyph in f:
            if len(glyph.components) > 0:
                for component in glyph.components:
                    baseGlyph = f[component.baseGlyph]
                if len(baseGlyph.components) > 0:
                    glyph.markColor = 1, 0, 0, 0.75

    def button1Callback(self, sender):
        f = CurrentFont()
        self.checkComponents(f)

    def button2Callback(self, sender):
        f = CurrentFont()
        self.nestedComponents(f)


markingTool()