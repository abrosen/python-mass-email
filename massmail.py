#!/usr/bin/env python
"""massmail.py  - A script for for emailing your multiple recipients an individualized message via google."""

import smtplib

__author__  =  "Andrew Rosen"
__license__ = "GPL"


sender = 'reply-to@my-email.com'

username = raw_input("enter Google email address:\n")
password = raw_input("enter pass:\n")

subject = "Insert Subject Here"

roster = open("file.extension")
messages  = []

for student in roster:
    student = student.split(',')
    body ="\nHello, your grades are:\nHW1: " + str(student[1]) + "\nHW2: "  + str(student[2]) 
    messages.append([student[0], body])


session = smtplib.SMTP('smtp.gmail.com:587')

session.ehlo()
session.starttls()
session.ehlo
session.login(username, password)

for message in messages:
    receiver = message[0]
    headers = ["from: " + sender,
            "subject: " + subject,
            "to: " + receiver,
            "mime-version: 1.0",
            "content-type: text/html"]
    headers = "\r\n".join(headers)
    body = message[1]
    session.sendmail(sender, receiver, headers + "\r\n\r\n" + body)
