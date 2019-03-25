import time, datetime, os

today = datetime.date.today()
#todaystr = today.isoformat()
now = datetime.datetime.now()
todaystr = now.strftime("%d.%m.%Y %X")

os.mkdir(todaystr)
print (todaystr)
