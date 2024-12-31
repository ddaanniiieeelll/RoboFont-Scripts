# MenuTitle: 􏿾 .notdef maker

import ezui

class notdef_maker(ezui.WindowController):
    
    def build(self):
        content = """
        Create a .notdef glyph 
        [_Vertical Stroke_]   @numberTextFieldVertical
        [_Horizontal Stroke_] @numberTextFieldHorizontal
        [_Advance Width_]     @numberTextFieldADV
        ---
        (Make .notdef)        @makeNotdefButton 
        """
        descriptionData = dict(
            numbertextFieldVertical=dict(
                valueType='integer'
            ),
            numbertextFieldHorizontal=dict(
                valueType='integer'
            ),
            numbertextFieldADV=dict(
                valueType='integer'
            )
        )
        
        self.w = ezui.EZWindow(
            title='notdef maker',
            size=('auto', 100),
            content=content,
            descriptionData=descriptionData,
            controller=self
        )
        
    def started(self):
        self.w.open()
        
    def numberTextFieldVerticalCallback(self, sender):
        self.v = sender.get()
    
    def numberTextFieldHorizontalCallback(self, sender):
        self.h = sender.get()
        
    def numberTextFieldADVCallback(self, sender):
        self.adv = sender.get()
        
    def makeNotdefButtonCallback(self, sender):
        # f = CurrentFont()
        fonts = AllFonts()

        for f in fonts:
            nd = f.newGlyph('.notdef')
            nd.clear()
            nd.width = int(self.adv)
            
            v = int(self.v)
            h = int(self.h)
            
            pen = nd.getPen()
            
            startX = 80
            startY = 0
            
            endX = nd.width - startX
            endY = f.info.capHeight
            
            BL = (startX, startY)
            BR = (endX, startY)
            TR = (endX, endY)
            TL = (startX, endY)
            
            BLI = (startX+v, startY+h)
            BRI = (endX-v, startY+h)
            TRI = (endX-v, endY-h)
            TLI = (startX+v, endY-h)
            
            pen.moveTo(BL)
            pen.lineTo(BR)
            pen.lineTo(TR)
            pen.lineTo(TL)
            pen.closePath()

            pen.moveTo(BLI)
            pen.lineTo(TLI)
            pen.lineTo(TRI)
            pen.lineTo(BRI)
            
            pen.closePath()
            
            nd.changed()
        
        print('Made .notdef with %s v and %s h stroke width and %s advance width' % (self.v, self.h, self.adv))
        self.w.close()
        
                
notdef_maker()

   
   
    
        
