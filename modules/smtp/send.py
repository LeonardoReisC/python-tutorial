import os
import pathlib
from string import Template
from dotenv import load_dotenv

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


load_dotenv()

HTML_PATH = pathlib.Path(__file__).parent / 'message.html'

# sender and receiver data
sender = os.getenv('FROM_EMAIL', '')
receiver = sender

# SMTP Settings
smtp_server = os.getenv('SMTP_SERVER', '')
smtp_port = os.getenv('SMTP_PORT', '')
smtp_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')

# Text message
with HTML_PATH.open('r') as file:
    file_text = file.read()
    template = Template(file_text)
    email_text = template.substitute(name='Leonardo')

# Transforms the message in MIMEMultipart
mime_multipart = MIMEMultipart()
mime_multipart['from'] = receiver
mime_multipart['to'] = sender
mime_multipart['subject'] = 'This is the email body'

email_body = MIMEText(email_text, 'html', 'utf-8')
mime_multipart.attach(email_body)

# E-mail sending
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)
    print('E-mail successfully sent!')