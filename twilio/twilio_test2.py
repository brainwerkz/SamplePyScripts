#!/usr/bin/python3

# we import the Twilio client from the dependency we just installed
from twilio.rest import Client

# the following line needs your Twilio Account SID and Auth Token
client = Client("ENTER_CORRECT_INFO", "ENTER_CORRECT_INFO")

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
client.messages.create(to="+15127996965", from_="+17372104374", 
                       body="Hello from your hubby John. This is one of the new things I've been working on today, after the gym AND nebulizing Marta! LU ~Me",
                       media_url="<Insert_URL_To_Photo>")
