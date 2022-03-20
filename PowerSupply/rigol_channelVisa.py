# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 12:23:38 2022

@author: Darrel
"""


class apply():
    def __init__(self,visaCommands):
        self.visaCommands = visaCommands
        self.defaultChannel = 'CH1'
        self.startString = ':APPL';

    def ch1(self):
        self.defaultChannel = 'CH1'
        self.visaCommands._writeVal(self.startString)

    def ch2(self):
        self.defaultChannel = 'CH2'
        self.visaCommands._writeVal(self.startString)

    def ch3(self):
        self.defaultChannel = 'CH3'
        self.visaCommands._writeVal(self.startString)

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
