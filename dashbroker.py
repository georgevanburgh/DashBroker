__author__ = 'George'

SMART_WATER_BUTTON_MAC = '74:75:48:2e:2b:4c'
HEFTY_BUTTON_MAC = '74:c2:46:4f:56:d8'
GILETTE_BUTTON_MAC = '74:c2:46:84:ab:8e'

from scapy.all import *
from actions import *
from database import *

buttonAddresses = [button.macAddress for button in Button.select()]

def arp_display(pkt):
  if pkt[ARP].op == 1: #who-has (request)
    if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
      if pkt[ARP].hwsrc in buttonAddresses:
        processMacAddress(pkt[ARP].hwsrc) 
      else:
        print "ARP Probe from unknown device: " + pkt[ARP].hwsrc

def processMacAddress(macAddress):
  if macAddress == SMART_WATER_BUTTON_MAC: # SmartWater
    print "Pushed SmartWater"
    notifyHouse("The house notification button has been pressed. This probably means that dinner is ready!")
    logButtonPress(macAddress, "DinnerNotification")
  elif macAddress == HEFTY_BUTTON_MAC: # Hefty
    print "Pushed Hefty"
    logButtonPress(macAddress, "Debug")
  elif macAddress == GILETTE_BUTTON_MAC: # Gilette
    print "Pushed Gilette"
    logButtonPress(macAddress, "Debug")

if __name__ == "__main__":
  print sniff(prn=arp_display, filter="arp", store=0, count=0)
