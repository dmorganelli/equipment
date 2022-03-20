# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 19:39:31 2020

@author: Darrel
"""
from visaCommands import commands
from measureVisa import measureVisa
from rigol_channelVisa import apply


class powerSupply(commands,apply):
    def __init__(self,psVisa):
        commands.__init__(self, psVisa)
        apply.__init__(self,self)
        self.measure = measureVisa(self)

    
        
        

