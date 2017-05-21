#!/usr/bin/python

import smtplib

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders 
 
fromaddr = "jr78745@gmail.com"
toaddr = "jrichardson@brainwerkz.com"

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "This is a PYTHON send"
 
body = "SUCCESS!"

msg.attach(MIMEText(body, 'plain'))

filename = "redhead.jpg"
attachment = open("/home/john/Pictures", "rb")

#filename = "Name of the file with its path extension" 
#attachment = open("Path of the File", "rb") 


part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part) 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "***")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
