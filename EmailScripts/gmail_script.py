#!/usr/bin/python3

import smtplib

gmail_user = 'jr78745@gmail.com'  
gmail_password = '**'

sent_from = gmail_user  
to = ['jrichardson@brainwerkz.com']  
subject = 'OMG Super Important Message'  
body = "Hey, what's up?\n\n- You"

email_text = """\  
From: %s  
To: %s  
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:  
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print ('Email sent!')
except:  
    print ('Something went wrong...')
