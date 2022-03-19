# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 19:39:31 2020

@author: Darrel
"""
from measureVisa import measureVisa
# from types import SimpleNamespace
from visaCommands import commands
class powerSupply(measureVisa,commands):
    def __init__(self,psVisa):
        commands.__init__(self, psVisa)
        self.measure = measureVisa(self)
    
        
        

