# menuTitle : Save Copy
# Creates a new .ufo in the same directory with the current date and time as name.
import time, datetime, os

path = os.getcwd()
font = CurrentFont()

now = datetime.datetime.now()
todaystr = now.strftime("%d-%m-%Y %H:%M:%S")

#font.save('%s.ufo'% (todaystr))
print (path)