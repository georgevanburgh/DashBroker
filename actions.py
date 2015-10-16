__author__ = 'George'

from twilio.rest import TwilioRestClient
from database import *

config = ConfigParser.RawConfigParser()
config.read("dashbroker.ini")

twilio_sid = config.get("Twilio", "SID")
twilio_auth_token = config.get("Twilio", "Token")

def notifyHouse(message):
  for housemate in Housemates.select():
    sendMessage(message, housemate.phoneNumber) 

def sendMessage(message, phoneNumber):
  client = TwilioRestClient(twilio_sid, twilio_auth_token)
  message = client.messages.create(to=phoneNumber, from_="+441173252273",
                                     body=message)

def logButtonPress(macAddress, reason):
  ButtonLog.create(reason=reason, button=macAddress)

if __name__ == "__main__":
  print "Debug"
