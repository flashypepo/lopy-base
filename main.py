from settings import app_eui, app_key
from network import LoRa

import socket
import time
import pycom
import struct
import binascii

# Disable the heartbeat LED
pycom.heartbeat(False)

# Make the LED light up in black
pycom.rgbled(0x000000)

# Initialize LoRa in LORAWAN mode.
lora = LoRa(mode=LoRa.LORAWAN, adr=True)

# Retrieve the dev_eui from the LoRa chip (Only needed for OTAA to retrieve once)
dev_eui = binascii.hexlify(lora.mac()).upper().decode('utf-8')
print(dev_eui)

# Join a network using OTAA (Over the Air Activation)
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

# Wait until the module has joined the network
count = 0
while not lora.has_joined():
    pycom.rgbled(0xffa500) # Make the LED light up in orange
    time.sleep(0.2)
    pycom.rgbled(0x000000) # Make the LED light up in black
    time.sleep(2)
    print("retry join count is:" ,  count)
    count = count + 1

print("join procedure succesfull")

# Show that LoRa OTAA has been succesfull by blinking blue
pycom.rgbled(0x0000ff)
time.sleep(0.5)
pycom.rgbled(0x000000)
time.sleep(0.1)
pycom.rgbled(0x0000ff)
time.sleep(0.5)
pycom.rgbled(0x000000)

# Create a raw LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
# Set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
# Make the socket non-blocking
s.setblocking(False)

while True:

    # send the data over LPWAN network
    s.send('Hello world')
    print('LoRa packet sent')
    
    pycom.rgbled(0x007f00) # Make the LED light up in green
    time.sleep(0.2)
    pycom.rgbled(0x000000)
    time.sleep(2.8)

    # Wait for 60 seconds before moving to the next iteration
    time.sleep(60)
