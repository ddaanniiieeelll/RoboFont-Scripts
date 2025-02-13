


font = CurrentFont()

feature = "ss01"
tab = "    "


def subRule(featureName: str):
    for glyph in font:
        if feature in glyph.name:
            glyphName = glyph.name
            baseName = glyphName.split(".")[0]
            rule = "%ssub %s by %s;" %(tab, baseName, glyphName)
            print(rule)


def openFeature(feature: str):
    print("feature", feature, "{")

    
def closeFeature(feature: str):
    print("}", feature + ";")
    

def featureName(name: str):
    print("%sfeatureNames {\n%s%sname \"%s\";\n%s};" %(tab, tab, tab, name, tab))
    
    


   
openFeature(feature)
# featureName("Alternate a")
subRule(feature)
closeFeature(feature)
          