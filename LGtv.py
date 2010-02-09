
class LGtv():
    id="01"
    
    INPUT_DTV_ANT = 0x00
    INPUT_DTV_CBL = 0x01
    INPUT_AN_ANT = 0x10
    INPUT_AN_CBL = 0x11
    INPUT_AV = 0x20
    INPUT_AV1 = 0x20
    INPUT_AV2 = 0x21
    INPUT_COMP = 0x40
    INPUT_COMP1 = 0x41
    INPUT_COMP2 = 0x42
    INPUT_PC = 0x60
    INPUT_HDMI = 0x90
    INPUT_HDMI1 = 0x90
    INPUT_HDMI2 = 0x91
    INPUT_HMDI3 = 0x92

    RATIO_43 = 0x01
    RATIO_169 = 0x02
    RATIO_ZOOM = 0x04
    RATIO_PROGRAM = 0x06
    RATIO_JUST_SCAN = 0x09
    RATIO_CINEMA_ZOOM_1 = 0x10
    RATIO_CINEMA_ZOOM_2 = 0x11
    RATIO_CINEMA_ZOOM_3 = 0x12
    RATIO_CINEMA_ZOOM_4 = 0x13
    RATIO_CINEMA_ZOOM_5 = 0x14
    RATIO_CINEMA_ZOOM_6 = 0x15
    RATIO_CINEMA_ZOOM_7 = 0x16
    RATIO_CINEMA_ZOOM_8 = 0x17
    RATIO_CINEMA_ZOOM_9 = 0x18
    RATIO_CINEMA_ZOOM_10 = 0x10
    RATIO_CINEMA_ZOOM_11 = 0x1A
    RATIO_CINEMA_ZOOM_12 = 0x1B
    RATIO_CINEMA_ZOOM_13 = 0x1C
    RATIO_CINEMA_ZOOM_14 = 0x1D
    RATIO_CINEMA_ZOOM_15 = 0x1E
    RATIO_CINEMA_ZOOM_16 = 0x1F

    def __init__(self, id=1):
        self.id = "%02X" % id
    
    def powerOff(self):
        """Turn the TV off"""
        return 'ka %s %02X\r' % (self.id, 0x0)
    
    def powerOn(self):
        """Turn the TV on"""
        return 'ka %s %02X\r' % (self.id, 0x1)
    
    def inputSelect(self, input):
        """Select the TV's input"""
        return 'xb %s %02X\r' % (self.id, input)
    
    def ratio(self, ratio):
        """Select the TV's ratio"""
        return 'xc %s %02X\r' % (self.id, ratio)
    
    def screenMuteOff(self):
        """Screen mute off (video on)"""
        return 'kd %s %02X\r' % (self.id, 0x0)
    
    def screenMuteOn(self):
        """Screen mute on (video off)"""
        return 'kd %s %02X\r' % (self.id, 0x1)
    
    def screenMuteOSD(self):
        """Screen mute OSD, but video is on"""
        return 'kd %s %02X\r' % (self.id, 0x10)
    
    def volumeMuteOn(self):
        """Mute TV volume"""
        return 'ke %s %02X\r' % (self.id, 0x0)
    
    def volumeMuteOff(self):
        """Unmute TV volume"""
        return 'ke %s %02X\r' % (self.id, 0x1)
    
