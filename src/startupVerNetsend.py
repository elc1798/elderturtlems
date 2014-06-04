#!/usr/bin/env python
import getpass
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

###
### Login Sequence:
###

#Grab Password

config = open('turtleconfigs.txt')
pw = config.readline()

#Error Handling
if pw[0] = '[':
  response = str(raw_input('It seems your configurations have not been set correctly. Set now?'))
  if response.upper() = 'Y' or response.upper() = 'YES':
    config.close()
    config = open('turtleconfigs.txt' , 'w')
    passname = ''
    password = str(raw_input('Password: '))
    username = str(raw_input('Email: '))
    passname = password + '\n' + username
    config.write(passname)
    config.close
    config = open('turtleconfigs.txt')
  else:
    print('Program exiting...')
    quit()

#Grab Username

me = config.readline()
you = me

config.close()
# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "The Elder Turtle Hath Spoken!"
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"

#Grab MESSAGE From File
f = open('MESSAGE.txt')
MESSAGE = f.read()
f.close()

html = "<html><head></head><body><p>" + MESSAGE + "</p></body></html>"

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)
# Send the message via local SMTP server.
#s = smtplib.SMTP('localhost')
s = smtplib.SMTP(host='smtp.gmail.com:587')
s.starttls()
s.login(me , pw)
# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
s.sendmail(me, you, msg.as_string())
s.quit()
