# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 20:28:46 2020

@author: Darrel
"""
outString = ':OUTP';
class commands:
    def __init__(self,psVisa):
        self._visa = psVisa;
        self.idn = self.getIdn();
        self.defaultChannel = '';
        
    def getIdn(self):
        stringVal = self._visa.query("*IDN?");
        return stringVal  
       
    def _sendQuery(self, command, secondCommand = ''):
        if not secondCommand:
            val = self._visa.query(command + '? ');
        else:
            val = self._visa.query(command + '? ' + secondCommand);
        return val
    
    def _writeVal(self, command):
        self._visa.write(command);
        
    def _convertToNumber(self,stringArray):
        val = [float(x) for x in stringArray.split(',')];
        if len(val)==1:
            val = val[0];
        return val
    

    
class output(commands):
    """
    Channel (Range) | OVP/OCP Settable Range   | OVP/OCP Default Value
    ----------------------------------------------------------------
    CH1 (30V/3A)    | 10mV to 33V/1mA to 3.3A  | 33.00V/3.300A
    CH2 (30V/3A)    | 10mV to 33V/1mA to 3.3A  | 33.00V/3.300A
    CH3 (5V/3A)     | 10mV to 5.5V/1mA to 3.3A | 5.50V/3.300A
    
    """
    def getMode(self):
        val = self._sendQuery(outString + ':MODE');
        return val
    
    def outModeCheckEnable(self,channel = ''):
        if not channel:
            channel = self.defaultChannel;
        val = self._sendQuery(outString,channel);
        return val
    
    def outputEnable(self,channel = ''):
        if not channel:
            channel = self.defaultChannel;
        self._writeVal(outString + ' ' + channel + ',ON','');
        
    def outputDisable(self,channel = ''):
        if not channel:
            channel = self.defaultChannel;
        self._writeVal(outString + ' ' + channel + ',OFF','');
        
# class channel(commands,measure):
#     def __init__(self):
#         super.__init__();
        
# class ch1(channel):
#     def __init__(self):
#         super.__init__();
#         self.defaultChannel = 'CH1';
