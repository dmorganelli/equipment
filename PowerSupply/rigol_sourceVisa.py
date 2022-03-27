# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 20:17:21 2022

@author: Darrel
"""
# from rigol_channelVisa import channel2String

class source():
    def __init__(self, visaCommands, sourceType, channel = ''): 
        self.visaCommands = visaCommands
        self.sourceType = sourceType
        if channel == '':
            self.startString = ':%s' % (self.sourceType)
        else:
            self.startString = ':SOUR%d:%s' % (channel, self.sourceType)
            self._defineLimits(channel)

    @property
    def level(self):#needs an IMMediate version. sets level on trigger event
        return self.visaCommands._convertToNumber(self.visaCommands._sendQuery(
            self.startString))

    @level.setter
    def level(self,sourceLevel):
        if (type(sourceLevel) == str) and ((sourceLevel.upper() == 'UP') or (sourceLevel.upper() == 'DOWN')):
            if (type(sourceLevel) == str) and (sourceLevel.upper() == 'UP'):
                self._level += self._setIncrement
            elif (type(sourceLevel) == str) and (sourceLevel.upper() == 'DOWN'):
                self._level -= self._setIncrement
            
            self.visaCommands._writeVal(self.startString+' '+str(self._level))# UP and DOWN commands not working 

        else:
            validLevel = self._writeValidInput(sourceLevel, self.startString)
            if validLevel:
                if (type(sourceLevel) == str) and (sourceLevel.upper()=='MAX'):
                    self._level = self._maxLimit
                elif (type(sourceLevel) == str) and (sourceLevel.upper()=='MIN'):
                    self._level = self._minLimit
                else:
                    self._level = sourceLevel

    @property
    def step(self):
        return self.visaCommands._convertToNumber(self.visaCommands._sendQuery(
            self.startString+':STEP'))

    @step.setter
    def step(self, setStep):
        validStep = 0
        if (type(setStep) == str):
            if ((setStep.upper() == 'DEF') or (setStep.upper() == 'DEFAULT')):
                validStep = 1
            else:
                print('Only acceptable string is DEF or DEFAULT.')
        elif (setStep <= self._maxLimit) and (setStep >= 0):
            validStep = 1
            setStep = str(setStep)

        if validStep:
            if (type(setStep) == str) and ((setStep.upper() == 'DEF') or (setStep.upper() == 'DEFAULT')):
                self._setIncrement = self._minIncrement
            else:
                self._setIncrement = float(setStep)
    
    # functions not available with this power supply
    # @property 
    # def trigger(self):
    #     return self.visaCommands._convertToNumber(self.visaCommands._sendQuery(
    #         self.startString+':TRIG'))

    # @trigger.setter
    # def trigger(self,triggerLevel):
    #     self._writeValidInput(triggerLevel, self.startString+':TRIG ')

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
        self._writeValidInput(limit, self.startString+':PROT ')

    def _writeValidInput(self,checkInput,writeString):
        validSetLimit = 0
        if (type(checkInput) == str):
            if ((checkInput.upper() == 'MAX') or (checkInput.upper() == 'MIN')):
                validSetLimit = 1
            else:
                print('Only acceptable string is MIN or MAX.')
        elif (checkInput <= self._maxLimit) and (checkInput >= 0):
            validSetLimit = 1
            checkInput = str(checkInput)

        if validSetLimit:
            self.visaCommands._writeVal(writeString+' '+checkInput)
        return validSetLimit

    def _defineLimits(self, channel):
        """
        Channel (Range) | OVP/OCP Settable Range   | OVP/OCP Default Value
        ----------------------------------------------------------------
        CH1 (30V/3A)    | 10mV to 33V/1mA to 3.3A  | 33.00V/3.300A
        CH2 (30V/3A)    | 10mV to 33V/1mA to 3.3A  | 33.00V/3.300A
        CH3 (5V/3A)     | 10mV to 5.5V/1mA to 3.3A | 5.50V/3.300A
        
        """
        self._minIncrement = None
        self._maxLimit = None
        self._minLimit = 0
        if self.sourceType == 'CURR':
            self._minIncrement = 0.001 #minimum increment resolition can be reduced with high resolution option
            self._maxLimit = 3.3
        elif self.sourceType == 'VOLT':
            self._minIncrement = 0.001
            self._maxLimit = 33
            if channel == 3:
                self._maxLimit = 5.5
