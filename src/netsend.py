#!/usr/bin/env python
import getpass
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import config

from urllib2 import urlopen

class Sender:
    def __init__(self, username=config.EMAIL, password=config.PASSWORD,
            subject="", message="", recipient=""):
        """
        Initializer for Sender class. If username and password are not given as
        parameters, then it wil default to those set in the config file
        """
        self.username = username
        self.password = password
        self.subject = subject
        self.message = message
        self.recipient = recipient

    def interactive_login(self, username=""):
        """
        Prompts the user to enter login credentials in the terminal
        """
        if username == "":
            print "Enter your username. If you do not include the '@service.domain', then it will default to 'gmail.com'"
            self.username = str(raw_input("Username: "))
        else:
            self.username = username
        if len(self.username.split("@")) == 1:
            self.username += "@gmail.com"
        self.password = str(getpass.getpass("Password: "))

    def get_ip(self):
        return urlopen('http://ip.42.pl/raw').read()

    def send_message(self, subject=None, message=None, recipient=None):
        """
        Sends the message to the recipient using the username and password. If
        the message or recipient are not specified, it will assume they have
        been set already
        """
        if not subject:
            subject = self.subject
        if not message:
            message = self.message
        if not recipient:
            recipient = self.recipient
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = self.username
        msg['To'] = recipient
        message = "<p> %s </p>" % (message.replace("\n", "</p><br><p>"),)

        # Add IP to message
        message += "<br><br><p>---</p><br><p> Sent from <b>%s</b></p>" % (self.get_ip(),)

        plaintext = message
        html = "<html><head></head><body> %s </body></html>" % (message,)

        # Record the MIME types of both parts - text/plain and text/html.
        part1 = MIMEText(plaintext, 'plain')
        part2 = MIMEText(html, 'html')

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this
        # case the HTML message, is best and preferred.
        msg.attach(part1)
        msg.attach(part2)

        # Send the message via Gmail SMTP server
        s = smtplib.SMTP(host='smtp.gmail.com:587')
        s.starttls()
        s.login(self.username, self.password)

        # sendmail function takes 3 arguments: sender's address, recipient's address
        # and message to send - here it is sent as one string.
        s.sendmail(self.username, recipient, msg.as_string())
        s.quit()

    def set_message(self, message):
        self.message = message

    def set_recipient(self, recipient):
        self.recipient = recipient
