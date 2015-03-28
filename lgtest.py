#!/usr/bin/python

import LGtv

tv = LGtv.LGtv('/dev/ttyUSB0')
if tv.isOn() == False:
	tv.powerOn()
tv.setChannelDTV(9)


