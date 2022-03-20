# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 12:23:38 2022

@author: Darrel
"""


class apply():
    def __init__(self,visaCommands):
        self.visaCommands = visaCommands
        self._defaultChannel = 'CH1'
        self.startString = ':APPL';

    def ch1(self):
        self.defaultChannel = 1;
        self.visaCommands._writeVal(self.startString)

    def ch2(self):
        self.defaultChannel = 2;
        self.visaCommands._writeVal(self.startString)

    def ch3(self):
        self.defaultChannel = 3;
        self.visaCommands._writeVal(self.startString)

    @property #getter 
    def defaultChannel(self):
        return self._defaultChannel

    @defaultChannel.setter
    def defaultChannel(self,channel = 1):
        if channel: #channel in empty when called during visaCommands init from powerSupply class.
            if (channel >= 1 ) & (channel <= 3):
                self._defaultChannel = 'CH'+str(channel)
                self.visaCommands._writeVal(self.startString)
            else:
                print('Not a valid Channel. Defaults is still set to '+self._defaultChannel)

    def settingsDefaultCh(self):
        if not self.defaultChannel:
            print('No default channel set.\n')
            chSettings = ''
        else:
            chSettings = self._sendQuery(self.startString)
        return chSettings

    def settingsCh(self, channel=''):
        if not channel:
            channel = self.defaultChannel
        chSettings = self._sendQuery(self.startString, channel)
        return chSettings
