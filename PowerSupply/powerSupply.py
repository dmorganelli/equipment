# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 19:39:31 2020

@author: Darrel
"""
# from types import SimpleNamespace
from visaCommands import *
class powerSupply(apply,measure,output):
    def __init__(self,psVisa):
        super().__init__(psVisa);
        self.measure = measure(self._visa);
        # self.visa = psVisa;
        # self.idn = self.getIdn();
        # self.defaultChannel = '';

    # def __setValue(self, command, channel)
    
    # def measure(self,selectType,channel = ''):
        
    #     def all(self):
    #         startString = ':MEAS';
    #         val = self.sendQuery(startString + ':ALL',channel);
    #         return val
            
    #     def curr(self):
    #         startString = ':MEAS';
    #         val = self.sendQuery(startString + ':CURR',channel);
    #         return val
        
    #     def pwr(self):
    #         startString = ':MEAS';
    #         val = self.sendQuery(startString + ':POWE',channel);
    #         return val
            
    #     def volt(self):
    #         startString = ':MEAS';
    #         val = self.sendQuery(startString + ':VOLT',channel);
    #         return val
        
    #     switch = {
    #         'all':all,
    #         'curr':curr,
    #         'pwr':pwr,
    #         'volt':volt
    #         }
        
    #     funcCall = switch.get(selectType,'Options are all, curr, pwr, volt');
    #     measVal = funcCall(self);
    #     return measVal
    
    # def applyChannel(self,channel, voltage = 5, current = 1):
        
        
        