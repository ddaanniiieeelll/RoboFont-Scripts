# MenuTitle : 🪞 Mirror Tool
# shortCut  : control+m

from vanilla import HUDFloatingWindow, Button
class mirror_tool:

    def __init__(self):
        # create floating window
        self.w = HUDFloatingWindow((123, 70), 'Mirror')

        # layout
        x, y = 10, 10
        padding = 10
        buttonHeight = 20

        # add buttons
        self.w.vButton = Button(
            (x, y, -padding, buttonHeight), # button position
            'vertical | ',
            # callbackfunction to be performed on click
            callback = self.mirror_vertical_callback) # button label

        # increase y so the second button sits lower than the first
        y += buttonHeight + padding

        self.w.hButton = Button(
            (x, y, -padding, buttonHeight), # button position
            'horizontal ― ',
            callback = self.mirror_horizontal_callback) # button label




        self.w.open()

    def mirror_vertical_callback(self, sender):
        g = CurrentGlyph()
        sc = g.selectedContours
        # find max and min coordinates if multiple contours are selected
        xmax = []
        xmin = []
        ymax = []
        ymin = []

        for c in sc:
            # print(c.bounds)
            xmax.append(c.bounds[2])
            xmin.append(c.bounds[0])
            ymax.append(c.bounds[3])
            ymin.append(c.bounds[1])
            xmax.sort()
            xmin.sort()
            ymax.sort()
            ymin.sort()

        # find the middle between min and max
        # this if statement checks if we have more than one contour selected
        # if only one contour is selected we don't need the lists and can directly get the bounds
        if len(xmax) and len(xmin) and len(ymax) and len(ymin) == 1:
            xd = (c.bounds[2] - c.bounds[0])//2 + c.bounds[0]
            yd = (c.bounds[3] - c.bounds[1])//2 + c.bounds[1]
        else:
            xd = (xmax[1] - xmin[0])//2 + xmin[0]
            yd = (ymax[1] - ymin[0])//2 + ymin[0]

        # vertical mirror
        for c in sc:
            c.transformBy((-1, 0, 0, 1, 0, 0), origin=(xd,yd))

    def mirror_horizontal_callback(self, sender):
        g = CurrentGlyph()

        sc = g.selectedContours
        # find max and min coordinates if multiple contours are selected
        xmax = []
        xmin = []
        ymax = []
        ymin = []


        for c in sc:
            # print(c.bounds)
            xmax.append(c.bounds[2])
            xmin.append(c.bounds[0])
            ymax.append(c.bounds[3])
            ymin.append(c.bounds[1])
            xmax.sort()
            xmin.sort()
            ymax.sort()
            ymin.sort()

        # find the middle between min and max
        # find the middle between min and max
        # this if statement checks if we have more than one contours selected
        # if only one contour is selected we don't need the lists and can directly get the bounds
        if len(xmax) and len(xmin) and len(ymax) and len(ymin) == 1:
            xd = (c.bounds[2] - c.bounds[0])//2 + c.bounds[0]
            yd = (c.bounds[3] - c.bounds[1])//2 + c.bounds[1]
        else:
            xd = (xmax[1] - xmin[0])//2 + xmin[0]
            yd = (ymax[1] - ymin[0])//2 + ymin[0]

        # horizontal mirror
        for c in sc:
            c.transformBy((1, 0, 0, -1, 0, 0), origin=(xd, yd))


mirror_tool()
