import json

from unittest.mock import patch

from notifications.app import outbound_handler


@patch("notifications.app.SMSHandler", autospec=True)
def test_sms_handler_is_called(SMSHandler):
    with open("tests/sample-events/basic-sms.json") as eventJson:
        event = json.loads(eventJson.read())
        outbound_handler(event, None)
        SMSHandler.return_value.send.assert_called_with(
            ["alice", "bob", "mallory"], "This is a test message in plaintext"
        )
