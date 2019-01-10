import os

from twilio.rest import Client


def send_sms(recipient, message):
    # Your Account Sid and Auth Token from twilio.com/console
    account_sid = os.environ.get("TWILIO_ACCOUNT_SID", "ACXXXXX")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN", "XXXXXX")
    # Your messaging service Sid
    service_sid = os.environ.get("TWILIO_MSGSERVICE_SID", "MSGXXXXX")
    # Your twilio phone number
    sender = os.environ.get("TWILIO_SENDER", "+44000000")

    client = Client(account_sid, auth_token)

    print("Attempting to send to %s" % recipient)
    message = client.messages.create(
        body=message, messaging_service_sid=service_sid, from_=sender, to=recipient
    )
