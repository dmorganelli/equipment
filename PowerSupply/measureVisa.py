# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 13:40:21 2020

@author: Darrel
"""

class measureVisa():
    def __init__(self,visaCommands):
        self.visaCommands = visaCommands;
        self.startString = ':MEAS'; 
 
    def all(self):
        val = self.visaCommands._convertToNumber(
            self.visaCommands._sendQuery(self.startString + ':ALL', self.visaCommands._activeChannel))
        return val

    def curr(self):
        val = self.visaCommands._convertToNumber(
            self.visaCommands._sendQuery(self.startString + ':CURR', self.visaCommands._activeChannel))
        return val
        
    def pwr(self):
        val = self.visaCommands._convertToNumber(
            self.visaCommands._sendQuery(self.startString + ':POWE', self.visaCommands._activeChannel))
        return val
        
    def volt(self):
        val = self.visaCommands._convertToNumber(
            self.visaCommands._sendQuery(self.startString + ':VOLT', self.visaCommands._activeChannel))
        return val
