from twilio.rest import Client

TWILIO_SID = "AC56a36a8fc1ef7655f8fce7199861ccf3"
TWILIO_AUTH_TOKEN = "119e2aa6af170bb80b5776fd88d232de"
TWILIO_VIRTUAL_NUMBER = "+18084259136"
TWILIO_VERIFIED_NUMBER = "+48693062747"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
