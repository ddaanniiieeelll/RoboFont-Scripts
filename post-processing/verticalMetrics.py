
import sys
import os
import calculate

from icecream import ic

upm = calculate.find_upm(sys.argv[1])
yMax = calculate.find_yMax(sys.argv[1])
yMin = calculate.find_yMin(sys.argv[1])
capHeight = calculate.find_capHeight(sys.argv[1])


ic(upm)
ic(yMax)
ic(yMin)
ic(capHeight)