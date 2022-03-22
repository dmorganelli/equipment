# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 12:23:38 2022

@author: Darrel
"""


class apply():
    def __init__(self,visaCommands):
        self.visaCommands = visaCommands
        self.startString = ':APPL';
        self.activeChannel = 1

    def ch1(self):
        self.activeChannel = 1;
        self.visaCommands._writeVal(
            self.startString + ' ' + self._activeChannel)

    def ch2(self):
        self.activeChannel = 2;
        self.visaCommands._writeVal(
            self.startString + ' ' + self._activeChannel)

    def ch3(self):
        self.activeChannel = 3;
        self.visaCommands._writeVal(
            self.startString + ' ' + self._activeChannel)

    @property #getter 
    def activeChannel(self):
        return self._activeChannel

    @activeChannel.setter
    def activeChannel(self,channel = 1):
        if channel: #channel in empty when called during visaCommands init from powerSupply class.
            if (channel >= 1 ) & (channel <= 3):
                self._activeChannel = 'CH'+str(channel)
                self.visaCommands._writeVal(
                    self.startString + ' ' + self._activeChannel)
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
        chSettings = self._sendQuery(self.startString, channel)
        return chSettings

def _checkChannel(channel):
    validChannel = False
    if (type(channel) == int) and (channel >= 1) & (channel <= 3):
        validChannel = True
    return validChannel
