# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 8:42:44 2022

@author: Darrel
"""

class output():
    def __init__(self, visaCommands, channel = ''):
        self.visaCommands = visaCommands
        self.channel = channel2String(channel)
        self.startString = ':OUTP'

    @property
    def mode(self):
        val = self.visaCommands._sendQuery(self.startString + ':MODE', self.startString)
        return val

    @property
    def isEnabled(self):
        val = self.visaCommands._sendQuery(self.startString, self.channel)
        return val

    def enable(self):
        if self.channel == '':
            self.visaCommands._writeVal(
                self.startString + ' ON')
        else:
            self.visaCommands._writeVal(
                self.startString + ' ' + self.channel + ',ON')

    def disable(self):
        if self.channel == '':
            self.visaCommands._writeVal(
                self.startString + ' OFF')
        else:
            self.visaCommands._writeVal(
                self.startString + ' ' + self.channel + ',OFF')

def channel2String(channel):
    channelStr = channel
    if channel:  # channel in empty when called during visaCommands init from powerSupply class.
        if (channel >= 1) & (channel <= 3):
            channelStr = 'CH'+str(channel)
        else:
            print('Not a valid Channel. actives is still set to ' +
                  channel)
    return channelStr
