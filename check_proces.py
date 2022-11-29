#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 11:30:05 2021

@author: michael
"""

# replace procesName, procesText1, procesText2 and procesText3 with the appropriate values


import os

            
program = "check_proces.py"

STATE_OK = 0
STATE_WARNING = 1
STATE_CRITICAL = 2
STATE_UNKNOWN = 3



# will return 0 for active else inactive.

proces_ = os.popen('ps ax | grep procesName |grep -v grep').read()


procesValues = ["procesText1", "procesText2", "procesText3"]


element = 0
elementActiv = 0 
elementNoRun = 0

dienstYes = []
dienstNo = []


while element < 3:
    if procesValues[element] in proces_:
        hinzu = (procesValues[element])
        dienstYes.append(hinzu)
        element = element + 1
        elementActiv = elementActiv  + 1

    else:
        hinzu = (procesValues[element])
        dienstNo.append(hinzu)
        element = element + 1
        elementNoRun = elementNoRun + 1
       
        

if elementActiv == 3:
    print(program, "- STATE_OK")
    print("Alle 3 Prozesse die benoetigt werden sind aktiv:")
    print(dienstYes)
    exit(STATE_OK)
else:
    print(program, "- STATE_CRITICAL")
    print("Folgende(r) Prozess(e) sind / ist nicht aktiv:")
    print(dienstNo)
    exit(STATE_CRITICAL) 
