# Create Twilio account to receive sid and auth_token and trial phone number
# Invokation: python3 sms.py

from twilio.rest import Client

account_sid = '<sid>'
auth_token = '<auth>'
client = Client(account_sid, auth_token)

message = client.messages.create(from_='+91<number>',
                                 body='Hello Buddy, python code here!',
                                 to='+91<number>')

print(message.sid)
print("Message Sent!")
