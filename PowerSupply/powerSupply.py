# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 19:39:31 2020

@author: Darrel
"""
from visaCommands import commands
from rigol_measureVisa import measureVisa
from rigol_activeChannelVisa import apply
from rigol_channelVisa import channel

class powerSupply(apply):
    def __init__(self,visaPort):
        self.visaPort = commands(visaPort)
        apply.__init__(self, self.visaPort)
        self.measure = measureVisa(self.visaPort)

        self.ch1 = channel(self.visaPort, 1)
        self.ch2 = channel(self.visaPort,2)
        self.ch3 = channel(self.visaPort, 3)
