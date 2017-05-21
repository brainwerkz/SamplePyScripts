#!/usr/bin/python3

#import csv
#import sqlalchemy
from datetime import datetime
#from time import gmtime, strftime
#from time import time
#from time import ctime
import time
import requests
from lxml import html



def print_lyrics():
    print ("I'm a lumberjack, and I'm okay.")
    print ("I sleep all night and I work all day!")


def repeat_lyrics():
    print_lyrics()
    print_lyrics()


repeat_lyrics()

#Today_date = datetime.date.isoformat(datetime.date.today())
#Today_time = datetime.time.isoformat(datetime.time(hour=))
#Today_time = (str(datetime.now()))
Today_time = (datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print("\nToday's date and time is: " )
#print (Today_time)

t = time.ctime()
print (t)


print ("\nThis is from the Naval Observatory:")
page = requests.get('http://tycho.usno.navy.mil/cgi-bin/timer.pl')
tree = html.fromstring(page.content)
print(tree.xpath('//html//body//h3//pre/text()')[1])
#print (tree)