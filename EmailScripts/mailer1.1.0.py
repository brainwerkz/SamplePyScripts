#!/usr/bin/python


import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def send(name, passwd, subject, body, addrto, q):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = name + '@gmail.com' 
    msg['To'] = addrto

    text = MIMEText(body)
    msg.attach(text)

    if(q == "y"):
        img = askopenfilename() 
        img_data = open(img, 'rb').read()
        image = MIMEImage(img_data, name=os.path.basename(img))
        msg.attach(image)

    print("connecting")
    s = smtplib.SMTP('smtp.gmail.com', '587')
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(name, passwd)
    print("connected")
    s.sendmail(name + '@gmail.com', addrto, msg.as_string())
    print("sent")
    s.quit()

Tk().withdraw()
name = input("Type your name in Gmail > ")
passwd = input("Type your password in Gmail > ")
subject = input("Type the subject of your mail > ")
body = input("Type the text of your mail > ")
q = input("If you want to attach an image type y/n > ")
addrto = input("Where do you wish to send the mail? > ")

send(name, passwd, subject, body, addrto, q)
