# menuTitle : Save Copy

# Creates a new .ufo in the same directory with the current date and time as name.
import time, datetime, os
from pathlib import Path

#folder = os.getcwd()
font = CurrentFont()
path = font.path
folder = Path(path).parents[0]
name = font.info.familyName
save_font = font.copy()

now = datetime.datetime.now()
today = now.strftime("%d-%m-%Y %H:%M:%S")


save_font.save('%s/%s_%s.ufo'%(folder, name, today))
print (path)
print (folder)
print ('%s/%s_%s.ufo'%(folder, name, today))

