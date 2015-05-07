import time
import datetime


pdxtime = datetime.datetime.now()
#print(pdxtime)

newyork = datetime.timedelta(hours=3)+datetime.datetime.now()
#print(newyork)

londontime = datetime.timedelta(hours=8)+datetime.datetime.now()
#print(londontime)

open9am = pdxtime.replace(hour=9, minute=0, second=0, microsecond=0)
#print(open9am)
closed2100 = pdxtime.replace(hour=21, minute=0, second=0, microsecond=0)
#print(closed2100)
    
if (newyork > open9am) and (newyork < closed2100):
    print('New York is open!')
else:
    print('Closed.')
    
if (londontime > open9am) and (londontime < closed2100):
    print('London is open!')
else:
    print('Closed.')


print('Hello World')

