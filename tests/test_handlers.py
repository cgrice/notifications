from unittest.mock import patch, call

from notifications.handlers import SMSHandler

mockConfig = {
    "people": {"mallory": {"sms": "0161555555"}, "alice": {"sms": "0161999999"}}
}


@patch("notifications.handlers.get_config", return_value=mockConfig)
@patch("notifications.handlers.send_sms")
def test_handler_sends_sms_to_correct_numbers(send_sms, *args):
    handler = SMSHandler()
    handler.send(["mallory"], "test")
    send_sms.assert_called_with("0161555555", "test")


@patch("notifications.handlers.get_config", return_value=mockConfig)
@patch("notifications.handlers.send_sms")
def test_handler_sends_multiple_sms_messages(send_sms, *args):
    handler = SMSHandler()
    handler.send(["mallory", "alice"], "test")
    send_sms.assert_has_calls(
        [call("0161999999", "test"), call("0161555555", "test")], any_order=True
    )


@patch("notifications.handlers.get_config", return_value=mockConfig)
@patch("notifications.handlers.send_sms")
def test_handler_does_not_send_to_unknown_person(send_sms, *args):
    handler = SMSHandler()
    handler.send(["bob"], "test")
    send_sms.assert_not_called()
