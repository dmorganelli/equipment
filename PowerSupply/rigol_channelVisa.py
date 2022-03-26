# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 19:55:56 2022

@author: Darrel
"""
from rigol_sourceVisa import source
class channel():
    def __init__(self, visaCommands, channel):
        self.visaCommands=visaCommands;
        self.channel = channel
        self.current = source(visaCommands,channel,'CURR')
        self.voltage = source(visaCommands,channel,'VOLT')