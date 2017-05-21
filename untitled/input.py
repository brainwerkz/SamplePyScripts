#!/usr/bin/python3
import datetime
from time import ctime
import webbrowser


name = input('What is your name?')
print ('Hello, ' +name)
play = input('How would you like to play a game?')
if play == 'yes' or 'sure':
    print ('Cool')
else:
    print('Fuck off then!')

sex = input("Would you like to play a sex game and fuck me in the ass?")

#while sex != 'yes'
if sex == 'yes':
    print("Cool, " +name, "I'll get the KY and get ready then!!")
else:
    print("That's too bad, I have a TIGHT ASS and love it rough!!!")

#webbrowser.open('https://chaturbate.com/friendsfuckersxx69/')
c = webbrowser.get('firefox')
c.open('https://chaturbate.com/')

Today_date = datetime.date.isoformat(datetime.date.today())
t = ctime()
#print (t)
print("Today's date is: " +t)
print ("\n" +Today_date)
# print("Hello")

#else:
#    exit()
