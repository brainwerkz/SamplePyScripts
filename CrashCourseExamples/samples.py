#!/usr/local/bin/python3

import datetime

current_date = datetime.datetime.now().date()
current_time = datetime.datetime.now().time()
current_date.isoformat()
current_time.isoformat()

print('The current date is: ')
print(current_date)
print('The current time is: ')
print(current_time)
