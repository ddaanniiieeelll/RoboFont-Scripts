# MenuTitle: GSUB Feature Writer
"""
Generates OpenType GSUB feature code for stylistic sets.
"""

import ezui


def generate_sub_rules(font, glyph_suffix: str, indent: str = "    ") -> list[str]:
    """
    Generate substitution rules for glyphs matching the glyph suffix.

    Args:
        font: RoboFont font object
        glyph_suffix: Glyph suffix (e.g., "ss01", "alt1") - what appears after the dot in glyph names
        indent: Indentation string (default: 4 spaces)

    Returns:
        List of substitution rule strings
    """
    rules = []
    suffix_pattern = f".{glyph_suffix}"

    for glyph in font:
        glyph_name = glyph.name
        # Check if glyph name ends with .glyph_suffix (e.g., "a.ss01" or "a.alt1")
        if glyph_name.endswith(suffix_pattern):
            base_name = glyph_name.rsplit(".", 1)[
                0
            ]  # Split from right to handle multiple dots
            rule = f"{indent}sub {base_name} by {glyph_name};"
            rules.append(rule)

    return rules


def generate_feature_block(
    font,
    feature_name: str,
    glyph_suffix: str,
    feature_display_name: str | None = None,
    indent: str = "    ",
) -> str:
    """
    Generate a complete GSUB feature block.

    Args:
        font: RoboFont font object
        feature_name: Feature tag (e.g., "ss01")
        glyph_suffix: Glyph suffix (e.g., "ss01", "alt1") - what appears after the dot in glyph names
        feature_display_name: Optional display name for featureNames table
        indent: Indentation string (default: 4 spaces)

    Returns:
        Complete feature block as a string
    """
    if font is None:
        raise ValueError("No font is open")

    lines = []

    # Open feature block
    lines.append(f"feature {feature_name} {{")

    # Optional feature name definition
    if feature_display_name:
        lines.append(f"{indent}featureNames {{")
        lines.append(f'{indent}{indent}name "{feature_display_name}";')
        lines.append(f"{indent}}};")

    # Generate substitution rules using glyph_suffix
    rules = generate_sub_rules(font, glyph_suffix, indent)
    if rules:
        lines.extend(rules)
    else:
        lines.append(f"{indent}# No matching glyphs found")

    # Close feature block
    lines.append(f"}} {feature_name};")

    return "\n".join(lines)


class GSUBWriter(ezui.WindowController):
    """UI controller for GSUB feature writer."""

    def build(self):
        content = """
        [_ _]            @featureNameTextField
        [_ _]            @glyphSuffixTextField
        [_ _]    @featureDisplayNameTextField
        ---
        (Generate Feature Code)    @generateButton
        ---
        [[_~ ~_]] @outputTextEditor
        ---
        (Copy to Clipboard)       @copyButton
        """

        descriptionData = dict(
            featureNameTextField=dict(placeholder="Feature Name", valueType="string"),
            glyphSuffixTextField=dict(placeholder="Glyph Suffix", valueType="string"),
            featureDisplayNameTextField=dict(
                placeholder="Display Name (optional)", valueType="string"
            ),
            outputTextEditor=dict(),
        )

        self.w = ezui.EZWindow(
            title="GSUB Feature Writer",
            size=(300, 300),
            content=content,
            descriptionData=descriptionData,
            controller=self,
        )

    def started(self):
        """Called when the window is opened."""
        self.w.open()

    def generateButtonCallback(self, sender):
        """Generate the GSUB feature code."""
        font = CurrentFont()  # type: ignore

        if font is None:
            self.w.getItem("outputTextEditor").set("Error: No font is open")
            return

        # Get values from text fields
        feature_name = self.w.getItem("featureNameTextField").get().strip()
        glyph_suffix = self.w.getItem("glyphSuffixTextField").get().strip()
        feature_display_name = (
            self.w.getItem("featureDisplayNameTextField").get().strip()
        )

        # Validate feature name
        if not feature_name:
            self.w.getItem("outputTextEditor").set("Error: Feature name is required")
            return

        # Validate glyph suffix
        if not glyph_suffix:
            self.w.getItem("outputTextEditor").set("Error: Glyph suffix is required")
            return

        # Use None if display name is empty
        if not feature_display_name:
            feature_display_name = None

        try:
            # Generate the feature block
            output = generate_feature_block(
                font, feature_name, glyph_suffix, feature_display_name
            )
            self.w.getItem("outputTextEditor").set(output)
            print(output)  # Also print to console
        except Exception as e:
            error_msg = f"Error: {str(e)}"
            self.w.getItem("outputTextEditor").set(error_msg)
            print(error_msg)

    def copyButtonCallback(self, sender):
        """Copy the content of the output text editor to clipboard."""
        from AppKit import NSPasteboard, NSStringPboardType

        output_text = self.w.getItem("outputTextEditor").get()

        if output_text:
            pasteboard = NSPasteboard.generalPasteboard()
            pasteboard.clearContents()
            pasteboard.setString_forType_(output_text, NSStringPboardType)
            print("Copied to clipboard")
        else:
            print("Nothing to copy - output is empty")


# Main execution
if __name__ == "__main__":
    GSUBWriter()
