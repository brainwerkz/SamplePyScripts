#!/usr/local/bin/python

#import datetime
#import dateutil

#current_date = datetime.datetime.now().date()
#current_time = datetime.datetime.now().time()
#current_date.isoformat()
#current_time.isoformat()


#current_date = dateutil.dateutil.now().date()
#current_time = dateutil.dateutil.now().time()
#current_date.isoformat()
#current_time.isoformat()


#current_date = dateutil.dateutil
#current_time = dateutil.dateutil.now().time()
#current_date.isoformat()
#current_time.isoformat()

#print('The current date is: ')
#print(current_date)
#print('The current time is: ')
#print(current_time)

from dateutil.relativedelta import *
from dateutil.easter import *
from dateutil.rrule import *
from dateutil.parser import *
from datetime import *
import commands
import os
now = parse(commands.getoutput("date"))
today = now.date()
time = now.time()
year = rrule(YEARLY,bymonth=8,bymonthday=13,byweekday=FR)[0].year
rdelta = relativedelta(easter(year), today)
print("Today is:"), today
print("The time is:"), time
print("The next year where August has a Friday the 13th is:"), year
#print("How far is the Easter of that year:"), rdelta
#print("And the Easter of that year is:"), today+rdelta
