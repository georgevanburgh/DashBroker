__author__ = 'George'

from clockwork import clockwork
import ConfigParser
from database import *

config = ConfigParser.RawConfigParser()
config.read("dashbroker.ini")

clockwork_key = config.get("ClockworkSMS", "Key")

def notifyHouse(message):
  for housemate in Housemates.select().where(Housemates.active):
    sendMessage(message, housemate.phoneNumber)

def sendMessage(message, phoneNumber):
  client = clockwork.API(clockwork_key)
  message = clockwork.SMS(
      to=phoneNumber,
      message=message)
  response = client.send(message)
  if not response.success:
      print response.error_code
      print response.error_description

def logButtonPress(macAddress, reason):
  ButtonLog.create(reason=reason, button=macAddress)

if __name__ == "__main__":
  print "Debug"
