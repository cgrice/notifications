import json

from notifications.handlers import SMSHandler

def outbound_handler(event, context):
    for record in event["Records"]:
        payload = record["body"]
        handle_event(json.loads(payload))


def handle_event(payload):
    if payload["type"] != "notification.send":
        pass

    if payload["medium"] == "sms":
        handler = SMSHandler()

    message = payload["message"]
    recipients = payload["recipients"]
    print(handler.send)
    handler.send(recipients, message)