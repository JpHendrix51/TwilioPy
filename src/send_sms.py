from twilio import twiml
from twilio.rest import Client
from twilio.twiml.messaging_response import Message, MessagingResponse


 #Download the helper library from https://www.twilio.com/docs/python/install


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
def sendSMS(phone):
account_sid = 'ACf21deb2904b14ad2094c6e6ed2620d76'
auth_token = 'f16a6a1ab906dd3df0f8070308d3a701'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+17544659541',
                     to=phone
                 )

print(message.sid)

#this is the twilio account information and the text that is sent from twilio