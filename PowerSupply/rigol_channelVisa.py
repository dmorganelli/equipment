# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 12:23:38 2022

@author: Darrel
"""


class apply():
    def __init__(self,visaCommands):
        self.visaCommands = visaCommands
        self.startString = ':APPL';
        self.defaultChannel = 1

    def ch1(self):
        self.defaultChannel = 1;
        self.visaCommands._writeVal(
            self.startString + ' ' + self._defaultChannel)

    def ch2(self):
        self.defaultChannel = 2;
        self.visaCommands._writeVal(
            self.startString + ' ' + self._defaultChannel)

    def ch3(self):
        self.defaultChannel = 3;
        self.visaCommands._writeVal(
            self.startString + ' ' + self._defaultChannel)

    @property #getter 
    def defaultChannel(self):
        return self._defaultChannel

    @defaultChannel.setter
    def defaultChannel(self,channel = 1):
        if channel: #channel in empty when called during visaCommands init from powerSupply class.
            if (channel >= 1 ) & (channel <= 3):
                self._defaultChannel = 'CH'+str(channel)
                self.visaCommands._writeVal(
                    self.startString + ' ' + self._defaultChannel)
            else:
                print('Not a valid Channel. Defaults is still set to '+self._defaultChannel)

    def settingsCh(self, channel=''):
        if not channel:
            channel = self.defaultChannel
        else:
            if _checkChannel(channel):
                channel = 'CH'+str(channel)
            else:
                print('Not a valid Channel.')
        chSettings = self._sendQuery(self.startString, channel)
        return chSettings

def _checkChannel(channel):
    validChannel = False
    if (type(channel) == int) and (channel >= 1) & (channel <= 3):
        validChannel = True
    return validChannel
