from notifications.config import get_config

from notifications.services.sms import send_sms


class Handler:
    def __init__(self):
        self.config = get_config()


class SMSHandler(Handler):
    def send(self, recipients, message):
        for recipient in recipients:
            if recipient in self.config["people"]:
                phone_number = self.config["people"][recipient]["sms"]
                send_sms(phone_number, message)
