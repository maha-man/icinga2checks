#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 17:03:45 2021

@author: michael
"""


program = "check_proces_and_serivce.py"

STATE_OK = 0
STATE_WARNING = 1
STATE_CRITICAL = 2
STATE_UNKNOWN = 3

 
 
import os

# replace serice

status = os.system('systemctl is-active --quiet service')



if status == 0:
    postgre = "service ist aktiv."
else:
    print(program, "- STATE_CRITICAL - serice ist nicht aktiv.")
    exit(STATE_CRITICAL)

# replace proces1 proces2

proces_ = os.popen('ps -ef |grep "proces1 \| proces2" |grep -v grep').read()

# replace proces search pattern

procesValues = ["proces_search_pattern1", "proces_search_pattern2"]


dienstYes = []
dienstNo = []

element = 0
elementRun = 0 



element = 0
elementActiv = 0 

while element < 2:
    if procesValues[element] in proces_:
        hinzu = (procesValues[element])
        dienstYes.append(hinzu)
        element = element + 1
        elementActiv = elementActiv  + 1

    else:
        hinzu = (procesValues[element])
        dienstNo.append(hinzu)
        element = element + 1
       
       
        
        
        
if elementActiv == 2:
    print(program, "- STATE_OK")
    print(postgre)
    print("Alle 2 Prozessse die benötigt werden sind aktiv:")
    print(dienstYes)
    exit(STATE_OK)

else:
    print(program, "- STATE_CRITICAL")
    print("Folgende(r) Prozess(e) sind / ist nicht aktiv:")
    print(dienstNo)
    exit(STATE_CRITICAL)



