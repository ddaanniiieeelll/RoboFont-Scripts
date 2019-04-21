# menuTitle : saveCopy
# shortCut  : command+shift+alt+s
# Creates a new .ufo in the same directory with the current date and time as name.
import time, datetime, os
from pathlib import Path

font = CurrentFont()
path = font.path
folder = Path(path).parents[0]
fName = font.info.familyName
sName = font.info.styleName
save_font = font.copy()

now = datetime.datetime.now()
today = now.strftime("%d-%m-%Y %H.%M")


save_font.save('%s/%s-%s_%s.ufo'%(folder, fName, sName, today))

print ('saveCopy done')
print ('Your saveCopy is here:', Path(path).parents[0])
