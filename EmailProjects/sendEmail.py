# Invokation: python3 sendEmail.py
# Enable this from source email: https://www.google.com/settings/security/lesssecureapps


import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Avichal Srivastava'
email['to'] = 'avichalsrivastava24@gmail.com'
email['subject'] = "You won RS. 100000000000!!!"

email.set_content('I am a Python Master!!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('sample2345dummy@gmail.com', "Hello@world24")
    smtp.send_message(email)
    print("Email Sent")
