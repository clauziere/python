#!/usr/bin/env python
# example : mailman.send('info@example.net',['johndoe@gmail.com'],['info@example.net','yourpassword','smtp.gmail.com:587'],'This is a subject','this is the content')
import smtplib

def send(fromaddr, toaddrs,configs, subject, mainMsg):
    header = 'To:' + ", ".join(toaddrs) + '\n' + 'From: ' + fromaddr + '\n' + 'Subject:' + subject + ' \n'
    msg = header + '\n ' + mainMsg + '\n\n'

    # Credentials (if needed)
    username = configs[0]
    password = configs[1]

    # The actual mail send
    server = smtplib.SMTP(configs[2])
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
