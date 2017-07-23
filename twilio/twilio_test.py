#!/usr/bin/python3

#// Download the twilio-csharp library from twilio.com/docs/libraries/csharp
#using System;
#using Twilio;
#using Twilio.Rest.Api.V2010.Account;
#using Twilio.Types;
#using System.Collections.Generic;

from twilio.rest import Client

account_sid = "ENTER_CORRECT_SID";
auth_token = "ENTER_CORRECT_TOKEN";

client = Client(account_sid, auth_token)

client.messages.create(
    to="+15127996965",
    from_="+17372104374",
    body="Red",
    media_url="<Insert_URL_To_Photo>")

