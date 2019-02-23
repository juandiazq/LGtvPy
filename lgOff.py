#!/usr/bin/python3
import LGtv

tv = LGtv.LGtv('/dev/ttyUSB0')

if tv.isOn():
    print('Se apaga la tele')
    tv.powerOff()
