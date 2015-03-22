#!/usr/bin/python

import LGtv

tv = LGtv.LGtv('/dev/ttyUSB0')
print tv.isOn()

