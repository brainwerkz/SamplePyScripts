#!/usr/bin/python3

#// Download the twilio-csharp library from twilio.com/docs/libraries/csharp
#using System;
#using Twilio;
#using Twilio.Rest.Api.V2010.Account;
#using Twilio.Types;
#using System.Collections.Generic;

from twilio.rest import Client

account_sid = "AC949bdf062f5c1e54fc6bc846b994c18e";
auth_token = "670f4d55115f3de01b29cad2ca9b8437";

client = Client(account_sid, auth_token)

client.messages.create(
    to="+15127996965",
    from_="+17372104374",
    body="Red",
    media_url="https://a.dilcdn.com/bl/wp-content/uploads/sites/25/2014/10/disney-redhead-merida-still1-e1413248584602.jpg")

