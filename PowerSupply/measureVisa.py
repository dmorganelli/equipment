# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 13:40:21 2020

@author: Darrel
"""
startString = ':MEAS';
class measureVisa:    
    def all(self,port):
        command = startString + ':ALL';
        return command
        
    def curr(self,port):
        command = startString + ':CURR';
        return command
        
    def pwr(self,port):
        command = startString + ':POWE';
        return command
        
    def volt(self,port):
        command = startString + ':VOLT';
        return command