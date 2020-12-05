import os
from twilio.rest import Client


TWILIO_ACCOUNT_SID='ACdc153c808931e214b1efdb12d15b6080'
TWILIO_AUTH_TOKEN='48f2e2708a97f2baac493e12a6f23cbf'
Client = Client( TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN)

from_whatsapp_number='whatsapp:+12345256527'
to_whatsapp_number='whatsapp:+9997539024'

Client.messages.create(body='its good to have you',from_=from_whatsapp_number,to=to_whatsapp_number)
