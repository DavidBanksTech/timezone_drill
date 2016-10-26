import datetime
from datetime import time

potime= datetime.datetime.now()

print "Current Time in Portland:"
print potime


#NY time
nytime = potime + datetime.timedelta(hours= 3, minutes= 00)
ytime = time(hour=nytime.hour)
print "Current Time in New York:"
print nytime

if ytime > datetime.time(hour= 9, minute = 0) and  ytime < datetime.time(hour= 21, minute = 0):
    print " The New York Branch Is Currently Open. "

else:
    print " The New York Branch Is Currently Closed. "

#London Time
lotime = potime + datetime.timedelta(hours= 8, minutes= 00)
ltime = time(hour= lotime.hour)
print "Current Time in London:"
print lotime

if ltime > datetime.time(hour=9, minute= 00) and ltime < datetime.time(hour=21, minute= 00):
    print " The London Branch Is Currently Open. "

else:
    print " The London Branch Is Currently Closed. "


