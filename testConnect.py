# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 22:41:29 2020

@author: Darrel
"""
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'\\ConnectVisa')
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'\\PowerSupply')
from connectVisa import connectEquipment
from powerSupply import*
os.path.exists('c:/')
equipment = connectEquipment();
pwr,scp = equipment.autoConnect();

ps = powerSupply(pwr);

ps.activeChannel = 2;
ps.ch1.voltage.level = 6;
print(ps.settingsCh(3));
measuredValues = ps.ch1.measure.all();
measuredVoltage = ps.ch1.measure.volt();
measuredLimit = ps.ch1.voltage.limit;

print(measuredValues);
print(measuredVoltage);
print(measuredLimit)
ps.ch1.voltage.enableLimit;
ps.ch1.voltage.step = 0.5
ps.ch1.voltage.level = 'DOWN'
ps.ch1.enable()
ps.ch1.disable()
ps.ch1.current.level = .1
ps.activeChannel = 1
