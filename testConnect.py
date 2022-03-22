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
# ps.defaultChannel = 'CH1';
# measuredValues = ps.measureAll();
ps.activeChannel = 2;
print(ps.settingsCh(3));
measuredValues = ps.measure.all();
measuredVoltage = ps.measure.volt();
measuredLimit = ps.ch1.voltage.limit;
# measuredValues = ps.measure('all','ch1')
# ps.meas();
# ps.all();
# measuredValues = ps.ch3();
print(measuredValues);
print(measuredVoltage);
print(measuredLimit)
ps.ch1.voltage.enableLimit;
ps.activeChannel = 1
#measuredValues = ps,meas.all.ch3();
