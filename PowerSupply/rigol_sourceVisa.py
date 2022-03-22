# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 20:17:21 2022

@author: Darrel
"""

class source():
    def __init__(self, visaCommands, channel, sourceType): 
        self.visaCommands = visaCommands
        self.channel = channel
        self.sourceType = sourceType
        self.startString = ':SOUR%d:%s' % (channel,sourceType)
        self._absolutLimit = getLimit(channel,sourceType)
        self.enableLimit = 0;
        self.limit = 'MAX'

    @property
    def limitTripped(self):
        isTripped = False
        limitTripped = self.visaCommands._sendQuery(
            self.startString+':PROT:TRIP')
        if limitTripped.upper().replace('\n', '') == 'YES':
            isTripped = True
        return isTripped 

    def clearTrip(self):
        isClear = True
        self.visaCommands._writeVal(self.startString+':PROT:CLE')
        if self.limitTripped:
            isClear = False
            print('Limit still tripped check connections.')
        return isClear

    @property
    def enableLimit(self):
        isEnabled = False
        limitEnabled = self.visaCommands._sendQuery(
            self.startString+':PROT:STAT')
        if limitEnabled.upper().replace('\n', '') == 'ON':
            isEnabled = True
        return isEnabled

    @enableLimit.setter
    def enableLimit(self,setLimit):
        if setLimit:
            self.visaCommands._writeVal(self.startString+':PROT:STAT ON')
        else:
            self.visaCommands._writeVal(self.startString+':PROT:STAT OFF')

    @property
    def limit(self):
        return self.visaCommands._convertToNumber(self.visaCommands._sendQuery(
                self.startString+':PROT'))

    @limit.setter
    def limit(self,limit):
        validSetLimit = 0
        if (type(limit) == str):
            if ((limit.upper() == 'MAX') or (limit.upper() == 'MIN')):
                validSetLimit = 1;
            else:
                print('Only acceptable string is MIN or MAX.')
        elif (limit<=self._absolutLimit)&(limit>=0):
            validSetLimit = 1
            limit = str(limit)

        if validSetLimit:
            self.visaCommands._writeVal(
                self.startString+':PROT '+limit)

def getLimit(channel,sourceType):
    """
    Channel (Range) | OVP/OCP Settable Range   | OVP/OCP Default Value
    ----------------------------------------------------------------
    CH1 (30V/3A)    | 10mV to 33V/1mA to 3.3A  | 33.00V/3.300A
    CH2 (30V/3A)    | 10mV to 33V/1mA to 3.3A  | 33.00V/3.300A
    CH3 (5V/3A)     | 10mV to 5.5V/1mA to 3.3A | 5.50V/3.300A
    
    """
    absoluteLimit = None
    if sourceType == 'CURR':
        absoluteLimit = 3.3
    elif sourceType == 'VOLT':
        absoluteLimit = 33
        if channel == 3:
            absoluteLimit = 5.5
    
    return absoluteLimit
