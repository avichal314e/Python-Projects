# Invokation: python3 customEmail.py
# Enable this from source email: https://www.google.com/settings/security/lesssecureapps


from os import name
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('sample.html').read_text())

email = EmailMessage()
email['from'] = 'Avichal Srivastava'
email['to'] = 'avichalsrivastava24@gmail.com'
email['subject'] = "You won RS. 100000000000!!!"

email.set_content(html.substitute({'name': 'Rahul'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('sample2345dummy@gmail.com', "Hello@world24")     # Email and Password
    smtp.send_message(email)
    print("Email Sent")
