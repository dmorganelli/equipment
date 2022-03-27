# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 13:40:21 2020

@author: Darrel
"""
from rigol_outputVisa import channel2String

class measureVisa():
    def __init__(self,visaCommands,channel = ''):
        self.visaCommands = visaCommands;
        self.startString = ':MEAS'; 
        self.channel = channel2String(channel)
 
    def all(self):
        val = self.visaCommands._convertToNumber(
            self.visaCommands._sendQuery(self.startString + ':ALL', self.channel))
        return val

    def curr(self):
        val = self.visaCommands._convertToNumber(
            self.visaCommands._sendQuery(self.startString + ':CURR', self.channel))
        return val
        
    def pwr(self):
        val = self.visaCommands._convertToNumber(
            self.visaCommands._sendQuery(self.startString + ':POWE', self.channel))
        return val
        
    def volt(self):
        val = self.visaCommands._convertToNumber(
            self.visaCommands._sendQuery(self.startString + ':VOLT', self.channel))
        return val
