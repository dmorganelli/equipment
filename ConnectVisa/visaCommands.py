# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 20:28:46 2020

@author: Darrel
"""
import regex as re

class commands:
    def __init__(self,visaPort):
        self.visaPort = visaPort;
        self.idn = self.getIdn();
        self.activeChannel = '';
        
    def getIdn(self):
        stringVal = self.visaPort.query("*IDN?")
        return stringVal  
       
    def _sendQuery(self, command, secondCommand = ''):
        if not secondCommand:
            val = self.visaPort.query(command + '?')
        else:
            if _checkChannel(secondCommand):
                secondCommand = 'CH%d' % secondCommand
            val = self.visaPort.query(command + '? ' + secondCommand)
        findLogic = re.findall('(YES*|NO*)', val.upper())
        if findLogic != []:
            val = False
            if findLogic[0] == 'YES':
                val = True
        return val
    
    def _writeVal(self, command):
        self.visaPort.write(command)
        
    def _convertToNumber(self,stringArray):
        # ([0-9],'.',',')
        val = [float(x) for x in re.findall("(\d+\.\d*|\d+)", stringArray)]
        if len(val)==1:
            val = val[0];
        return val

def _checkChannel(channel):
    validChannel = False
    if (type(channel) == int) and (channel >= 1) & (channel <= 3):
        validChannel = True
    return validChannel
