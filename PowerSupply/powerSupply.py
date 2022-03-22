# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 19:39:31 2020

@author: Darrel
"""
from visaCommands import commands
from measureVisa import measureVisa
from rigol_activeChannelVisa import apply
from rigol_channelVisa import channel

class powerSupply(commands,apply):
    def __init__(self,psVisa):
        commands.__init__(self, psVisa)
        apply.__init__(self,self)
        self.measure = measureVisa(self)

        self.ch1 = channel(self,1)
        self.ch2 = channel(self,2)
        self.ch3 = channel(self,3)

    
        
        

