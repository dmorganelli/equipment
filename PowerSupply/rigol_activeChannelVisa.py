# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 12:23:38 2022

@author: Darrel
"""

class apply():
    def __init__(self):
        self.visaCommands = self
        self.startString_active = ':APPL';
        self.activeChannel = 1

    def ch1(self):
        self.activeChannel = 1
        self.visaCommands._writeVal(
            self.startString_active + ' ' + self._activeChannel)

    def ch2(self):
        self.activeChannel = 2;
        self.visaCommands._writeVal(
            self.startString_active + ' ' + self._activeChannel)

    def ch3(self):
        self.activeChannel = 3;
        self.visaCommands._writeVal(
            self.startString_active + ' ' + self._activeChannel)

    @property #getter 
    def activeChannel(self):
        print("Power supply doesn't return active channel.")

    @activeChannel.setter
    def activeChannel(self,channel = 1):
        if channel: #channel in empty when called during visaCommands init from powerSupply class.
            if (channel >= 1 ) & (channel <= 3):
                self._activeChannel = 'CH'+str(channel)
                self._writeVal(
                    self.startString_active + ' ' + self._activeChannel)
            else:
                print('Not a valid Channel. actives is still set to '+self._activeChannel)

    def settingsCh(self, channel=''):
        if not channel:
            channel = self.activeChannel
        # else:
            # if _checkChannel(channel):
            #     channel = 'CH'+str(channel)
            # else:
            #     print('Not a valid Channel.')
        chSettings = self._sendQuery(self.startString_active, channel)
        return chSettings

def _checkChannel(channel):
    validChannel = False
    if (type(channel) == int) and (channel >= 1) & (channel <= 3):
        validChannel = True
    return validChannel
