# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 19:55:56 2022

@author: Darrel
"""
from rigol_outputVisa import *
from rigol_sourceVisa import source
from rigol_measureVisa import measureVisa

class channel(output):
    def __init__(self, visaCommands, channel = ''):
        self.visaCommands=visaCommands;
        self.channel = channel2String(channel)
        output.__init__(self,visaCommands,channel)
        self.measure = measureVisa(visaCommands, channel)
        self.current = source(visaCommands,'CURR',channel)
        self.voltage = source(visaCommands,'VOLT',channel)

