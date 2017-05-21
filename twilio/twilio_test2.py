#!/usr/bin/python3

# we import the Twilio client from the dependency we just installed
from twilio.rest import Client

# the following line needs your Twilio Account SID and Auth Token
client = Client("AC949bdf062f5c1e54fc6bc846b994c18e", "670f4d55115f3de01b29cad2ca9b8437")

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
client.messages.create(to="+15127996965", from_="+17372104374", 
                       body="Hello from your hubby John. This is one of the new things I've been working on today, after the gym AND nebulizing Marta! LU ~Me",
                       media_url="https://c1.staticflickr.com/3/2899/14341091933_1e92e62d12_b.jpg")
