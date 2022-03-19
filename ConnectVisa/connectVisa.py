# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 06:03:00 2020

@author: Darrel
"""
import pyvisa
# rm = pyvisa.ResourceManager();
# addresses = list(rm.list_resources());
# port =  rm.open_resource(addresses[0]);

class connectEquipment:
    
    def __init__(self):
        self.collectResources();
        
    def collectResources(self):
        self.rm = pyvisa.ResourceManager();
        self.addresses = list(self.rm.list_resources());
        
        
    def listAddresses(self):
        return self.addresses
    
    def connectVisa(self,address):
        return self.rm.open_resource(address);

    def autoConnect(self):
        addresses = self.listAddresses();
        ps = [];
        scope = [];
        for address in addresses:
            if (address.find('USB0::')>=0):
                tempConnect = self.connectVisa(address);
                idnQuery = tempConnect.query("*IDN?");
                if (idnQuery.find('DP832')>=0):
                    ps = tempConnect;
                elif (idnQuery.find('DS1054Z')>=0):
                    scope = tempConnect;
        return ps, scope