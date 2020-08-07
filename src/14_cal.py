import sys
import calendar
from datetime import datetime

print(sys.argv)
if len(sys.argv) == 1:
    calendar.TextCalendar(0).prmonth(datetime.now().year, datetime.now().month)
elif len(sys.argv) == 2:
    calendar.TextCalendar(0).prmonth(datetime.now().year, int(sys.argv[1]))
elif len(sys.argv) == 3:
    calendar.TextCalendar(0).prmonth(int(sys.argv[2]), int(sys.argv[1]))
else:
    print('This program expects arguments')
    exit()
