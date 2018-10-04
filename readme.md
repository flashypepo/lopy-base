# TTN Flevoland, Windesheim - Lopy Workshop

## The Things Network

### Make sure to have your account registered at The Things Network
Registering your account can be done at
https://account.thethingsnetwork.org/register

### Applications
Create you application here:
https://console.thethingsnetwork.org/applications/

#### Application EUI
The AppEUI: This is an Application End Device Unique Identifier used to group objects. This address, 64 bits, is used to classify the peripheral devices by application. This setting can be adjusted.

### Devices
Add your device to your application
https://console.thethingsnetwork.org/applications/your-application/devices

- DeviceID: A unique name
- DeviceEUI: This identifier, factory set, makes each object unique. In principle, this setting cannot be adjusted.
- AppKey: This is a secret key shared between the peripheral device and the network. It is used to determine the session keys. This setting can be adjusted.

##### Retrieve the DeviceEUI
For OTAA you can retrieve the dev_eui from the LoRa chip with the following commands:
```python
>>> import binascii
>>> from network import LoRa
>>> dev_eui = binascii.hexlify(lora.mac()).upper().decode('utf-8')
>>> print(dev_eui)
```

### Security
#### Activation types
There are two ways of activating a device on the network OTAA and ABP. OTAA is more secure and default.

OTAA: Over-The-Air-Activation
Over-the-Air Activation (OTAA) is the preferred and most secure way to connect with The Things Network. Devices perform a join-procedure with the network, during which a dynamic DevAddr is assigned and security keys are negotiated with the device.

ABP: Activation By Personalization
Activation by Personalization (ABP)
In some cases you might need to hardcode the DevAddr as well as the security keys in the device. This means activating a device by personalisation (ABP). This strategy might seem simpler, because you skip the join procedure, but it has some downsides related to security.

#### Frame counters
It is however possible to re-transmit the messages. These so-called replay attacks can be detected and blocked using frame counters.

When a device is activated, these frame counters (FCntUp and FCntDown) are both set to 0. Every time the device transmits an uplink message, the FCntUp is incremented and every time the network sends a downlink message, the FCntDown is incremented. If either the device or the network receives a message with a frame counter that is lower than the last one, the message is ignored.

This security measure has consequences for development devices, which often are statically activated (ABP). When you do this, you should realize that these frame counters reset to 0 every time the device restarts (when you flash the firmware or when you unplug it). As a result, The Things Network will block all messages from the device until the FCntUp becomes higher than the previous FCntUp. Therefore, you should re-register your device in the backend every time you reset it.

For the development devices the setting [Frame Counter Checks] is unchecked.

#### Memory error
If the following error occurs:
```python
An error occurred: Not enough memory available on the board.
Upload failed. Please reboot your device manually.
```
Factory Reset the Filesystem by
```
>>> import os
>>> os.mkfs('/flash')
```

## References
### The Things Network
https://www.thethingsnetwork.org/forum/t/what-is-the-difference-between-otaa-and-abp-devices/2723
https://www.thethingsnetwork.org/docs/devices/bytes.html
https://www.thethingsnetwork.org/wiki/LoRaWAN/Duty-Cycle

### Pycom
https://startiot.telenor.com/learning/pysense-quick-start-guide/
https://forum.pycom.io/topic/2001/pysense-accuracy
https://docs.pycom.io/chapter/pytrackpysense/apireference/pysense.html

### Python
https://docs.python.org/2/library/struct.html

### Datarates
https://blog.dbrgn.ch/2017/6/23/lorawan-data-rates/

### Security
https://www.jaguar-network.com/en/news/lorawan-in-a-nutshell-2-internet-of-things-iot/
https://zakelijkforum.kpn.com/lora-forum-16/over-the-air-activation-otaa-8323
