#!/usr/bin/python3
import datetime
from time import ctime
import webbrowser
import time


name = input('What is your name?')
print('Hello, ' + name)
play = input('How would you like to play a game?')
if play == 'yes' or 'sure':
    print('Cool')
else:
    print('Fuck off then!')

sex = input("Would you like to play a sex game and fuck me in the ass?")

# while sex != 'yes'
# if sex == 'yes':
#    print("Cool, " +name, "I'll get the KY and get ready then!!")
# else:
#    print("That's too bad, I have a TIGHT ASS and love it rough!!!")

if sex != 'yes':
    print("That's too bad, " + name, " I have a TIGHT ASS and love it rough!!!")
else:
    print("Cool, " + name, "I'll get the KY and get ready then!!")


# THIS SECTION WORKS BUT IS JUST REMMED OUT
# time.sleep(5)
# webbrowser.open('https://chaturbate.com/')
# c = webbrowser.get('firefox')
# c.open('https://chaturbate.com/')

Today_date = datetime.date.isoformat(datetime.date.today())
t = ctime()
# print (t)
print("\nToday's date is: " + t)
print("\n" + Today_date)
# print("Hello")

# else:
#    exit()
