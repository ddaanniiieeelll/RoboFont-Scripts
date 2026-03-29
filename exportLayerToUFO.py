# MenuTitle: Export layer to new UFO
# -*- coding: utf-8 -*-
"""
Creates a new UFO from one layer of the current font.
The new font gets the same info, and only glyphs from the chosen layer
(copied into the default layer). Groups and kerning are copied only for
glyphs that exist in the selected layer.
"""

import os
import ezui


def export_layer_to_ufo(sourceFont, layerName):
    """Create a new UFO from sourceFont's layer. Saves to same folder as source, filename = layer name."""
    layer = sourceFont.getLayer(layerName)
    glyphNames = list(layer.keys())
    if not glyphNames:
        return False, "The layer '%s' has no glyphs." % layerName

    # New UFO path: same directory as source, filename = layer name
    if sourceFont.path:
        folder = os.path.dirname(sourceFont.path)
        savePath = os.path.join(folder, layerName + ".ufo")
    else:
        return False, "Source font has no path. Save the source font first."

    try:
        newFont = NewFont(showInterface=True)
    except Exception as e:
        return False, "Could not create new font: %s" % e

    try:
        # Copy font-level info from source
        newFont.info.copyData(sourceFont.info)

        # Copy groups: only for glyphs that exist in the layer
        layerSet = set(glyphNames)
        for groupName, groupGlyphs in sourceFont.groups.items():
            if groupName.startswith("public.") or not groupName.startswith("_"):
                filtered = [g for g in groupGlyphs if g in layerSet]
                if filtered:
                    newFont.groups[groupName] = filtered

        # Copy kerning: only pairs where both glyphs are in the layer
        for (g1, g2), value in sourceFont.kerning.items():
            if g1 in layerSet and g2 in layerSet:
                newFont.kerning[(g1, g2)] = value

        # Copy features text (user can trim later)
        newFont.features.text = sourceFont.features.text

        # Copy font guidelines
        for guideline in sourceFont.guidelines:
            newFont.appendGuideline(
                position=guideline.position,
                angle=guideline.angle,
                name=guideline.name,
                color=guideline.color,
            )

        # Copy glyphs from the selected layer into the default layer
        defaultLayer = newFont.defaultLayer
        for name in glyphNames:
            sourceGlyph = layer[name]
            defaultLayer.insertGlyph(sourceGlyph, name=name)

        # Preserve glyph order
        order = [g for g in sourceFont.glyphOrder if g in layerSet]
        if order:
            rest = [g for g in glyphNames if g not in order]
            newFont.glyphOrder = order + rest
        else:
            newFont.glyphOrder = glyphNames

        newFont.save(savePath)
        return True, "Saved %s (%i glyphs) to %s" % (layerName, len(glyphNames), savePath)

    except Exception as e:
        try:
            newFont.close()
        except Exception:
            pass
        return False, str(e)


class ExportLayerToUFOController(ezui.WindowController):

    def build(self):
        self.font = CurrentFont()
        if self.font is None:
            self.layerOrder = []
            sourceLabel = "No font open."
        else:
            self.layerOrder = self.font.layerOrder or []
            sourcePath = self.font.path or self.font.info.familyName or "Untitled"
            sourceLabel = "Source: %s" % sourcePath

        # First item in popup so there is always something to show
        if not self.layerOrder:
            self.layerOrder = ["(no layers)"]

        content = """
        !- """ + sourceLabel + """

        Choose layer:
        (Layer ...)             @layerPopUp

        ---
        (Create new UFO…)       @exportButton

        ---
        !- @statusLabel
        """

        descriptionData = dict(
            layerPopUp=dict(
                items=self.layerOrder,
                selected=0,
            ),
            statusLabel=dict(
                text="",
                sizeStyle="small",
            ),
        )

        self.w = ezui.EZWindow(
            title="Export layer to new UFO",
            size=("auto", "auto"),
            content=content,
            descriptionData=descriptionData,
            controller=self,
        )

    def started(self):
        self.w.open()
        # Disable export if no font or only one layer
        font = CurrentFont()
        if font is None or len(font.layerOrder or []) < 2:
            self.w.getItem("exportButton").enable(False)

    def layerPopUpCallback(self, sender):
        pass

    def exportButtonCallback(self, sender):
        layerPopUp = self.w.getItem("layerPopUp")
        statusLabel = self.w.getItem("statusLabel")
        layerName = layerPopUp.getItem()

        if not self.font or layerName == "(no layers)":
            statusLabel.set("No layer selected.")
            return

        ok, msg = export_layer_to_ufo(self.font, layerName)
        statusLabel.set(msg)
        if ok:
            print(msg)


# Run when executed in RoboFont
if __name__ == "__main__" or "ExportLayerToUFOController" in dir():
    ExportLayerToUFOController()
