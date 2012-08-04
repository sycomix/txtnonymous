from twilio.rest import TwilioRestClient
import credentials

class Twilio:
    def __init__(self):
        self.client = TwilioRestClient(credentials.sid, credentials.auth)

    def send_sms(self, number, message):
        message = self.client.sms.messages.create(to = number, from_ = credentials.phone_number,
                                       body = message)

if __name__ == "__main__":        
  twilio = Twilio()
  twilio.send_sms(credentials.joe_phone_number, "Hallo Joe")

