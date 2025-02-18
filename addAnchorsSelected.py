# MenuTitle: Add Anchors to selected glyphs

import ezui


class DemoController(ezui.WindowController):

    font = CurrentFont()

    def build(self):
        content = """
        [__]      @anchorName
        (x-height)   @button1
        (cap height) @button2
        (ascender)   @button3
        (baseline)   @button4
        (?)          @helpButton
        """
        descriptionData = dict(
            anchorName=dict(placeholder="Anchor", valueType="string")
        )
        self.w = ezui.EZWindow(
            title="Add Anchor",
            content=content,
            descriptionData=descriptionData,
            controller=self,
        )

    def started(self):
        self.w.open()

    def anchorNameCallback(self, sender):
        anchorName = sender.get()
        return anchorName

    def button1Callback(self, sender):
        anchorName = self.anchorNameCallback(self.w.getItem("anchorName"))
        for glyph in self.font.selectedGlyphs:
            width = glyph.width

            if width is None:
                continue
            horizontalPosition = width / 2
            with glyph.undo("add Anchor"):
                glyph.appendAnchor(
                    anchorName, (horizontalPosition, self.font.info.xHeight)
                )

    def button2Callback(self, sender):
        anchorName = self.anchorNameCallback(self.w.getItem("anchorName"))
        for glyph in self.font.selectedGlyphs:
            width = glyph.width

            if width is None:
                continue
            horizontalPosition = width / 2
            with glyph.undo("add Anchor"):
                glyph.appendAnchor(
                    anchorName, (horizontalPosition, self.font.info.capHeight)
                )

    def button3Callback(self, sender):
        anchorName = self.anchorNameCallback(self.w.getItem("anchorName"))
        for glyph in self.font.selectedGlyphs:
            width = glyph.width

            if width is None:
                continue
            horizontalPosition = width / 2
            with glyph.undo("add Anchor"):
                glyph.appendAnchor(
                    anchorName, (horizontalPosition, self.font.info.ascender)
                )

    def button4Callback(self, sender):
        anchorName = self.anchorNameCallback(self.w.getItem("anchorName"))
        for glyph in self.font.selectedGlyphs:
            width = glyph.width

            if width is None:
                continue
            horizontalPosition = width / 2
            with glyph.undo("add Anchor"):
                glyph.appendAnchor(anchorName, (horizontalPosition, 0))

    def helpButtonCallback(self, sender):
        print("Help button pressed")


DemoController()
