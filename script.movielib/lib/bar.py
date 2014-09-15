# -*- coding: utf-8 -*-

import xbmc
import xbmcaddon
import xbmcgui
import sys
import os

__addon__               = xbmcaddon.Addon()
__addonname__           = __addon__.getAddonInfo('name')
__addonpath__           = xbmc.translatePath(__addon__.getAddonInfo('path')).decode('utf-8')
__lang__                = __addon__.getLocalizedString

sys.path.append(os.path.join(__addonpath__, "lib"))

class Bar:
    def __init__(self):
        self.settingsBar  = __addon__.getSetting('bar')
        self.b = xbmcgui.DialogProgressBG()
    
    def create(self, message, heading):
        if 'true' in self.settingsBar:
            self.b.create(heading, message)
    
    def update(self, percent, message, heading=0):
        if 'true' in self.settingsBar:
            if heading == 0:
                self.b.update(percent, message=message)
            else:
                self.b.update(percent, heading, message)
        
    def close(self):
        if 'true' in self.settingsBar:
            self.b.close()