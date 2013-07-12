import smtplib

sender = 'reply-to@my-email.com'

username = raw_input("enter Google email address:\n")
password = raw_input("enter pass:\n")

subject = "Insert Subject Here"

roster = open("file.extension")
grades  = []

for student in roster:
    student = student.split(',')
    body ="\nHello, your grades are:\nHW1: " + str(student[1]) + "\nHW2: "  + str(student[2]) 
    grades.append([student[0], body])


session = smtplib.SMTP('smtp.gmail.com:587')

session.ehlo()
session.starttls()
session.ehlo
session.login(username, password)

for student in grades:
    receiver = student[0]
    headers = ["from: " + sender,
            "subject: " + subject,
            "to: " + receiver,
            "mime-version: 1.0",
            "content-type: text/html"]
    headers = "\r\n".join(headers)
    body = student[1]
    message = headers + "\r\n\r\n" + body
    session.sendmail(sender, receiver, headers + "\r\n\r\n" + body)
