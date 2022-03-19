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
            self.visaCommands._sendQuery(self.startString + ':ALL'))
        return val

    def curr(self):
        val = self.visaCommands._convertToNumber(
            self.visaCommands._sendQuery(self.startString + ':CURR'))
        return val
        
    def pwr(self):
        val = self.visaCommands._convertToNumber(
            self.visaCommands._sendQuery(self.startString + ':POWE'))
        return val
        
    def volt(self):
        val = self.visaCommands._convertToNumber(
            self.visaCommands._sendQuery(self.startString + ':VOLT'))
        return val
