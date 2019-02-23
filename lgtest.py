#!/usr/bin/python

import LGtv

tv = LGtv.LGtv('/dev/ttyUSB0')
print(tv.isOn())
if tv.isOn():
    tv.powerOff()
    print("Estaba encendida la tele\n")

