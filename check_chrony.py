#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 15:50:05 2021

@author: michael
"""

import os
import time

program = "check_chrony"

STATE_OK = 0
STATE_WARNING = 1
STATE_CRITICAL = 2
STATE_UNKNOWN = 3


# will return 0 for active else inactive.

status = os.system('systemctl is-active --quiet chrony')

tracking = os.popen('chronyc tracking').read()

state = "ok"

printwarn = "no"

notAktive = "no"



# Es wird geprüft ob in der letzen Zeile von "systemctl status chrony" "System clock wrong" steht
# und ob die letzte Zeile vom heutigen Tag ist. Nur dann erscheind die Warnung.
# Anderfalls wird sich das Warning nie ändern ausser das "System clock wrong" verschwindet ganz aus dem Log.



global clock_checking

clock_checking = os.popen('systemctl status chrony').read()


def last_line():
    lastLine = clock_checking.splitlines()[-1]
    return lastLine


day = time.strftime("%d", time.localtime())


if "System clock wrong " in last_line() and " "+ day +" " in last_line(): 
    
    os.system('systemctl restart chrony')
    time.sleep(5)

    if "System clock wrong " in last_line() and " "+ day +" " in last_line():

        state = "warn"
        printwarn = "yes"
        warnMessage = "chrony Zeitserver hat Probeleme bezueglich der Zeitabweichung: System clock wrong."


    
if status == 0:
    chronyDienst = "chrony Zeitserver ist aktiv."
else:
    state = "criti"
    notAktive = "yes"
    printZeitNichtAktiv = "chrony Zeitserver ist nicht aktiv."    


if "Leap status     : Normal" in tracking:
    verbunden = "chrony Zeitserver ist mit (einem) anderen Zeitserver(n) verbunden."
else:
    state = "criti" 
    notCon = "yes"
    nichtVerbunden = "chrony Zeitserver ist nicht mit einem anderen Zeitserver verbunden."


    
if state == "ok":
    print(program, "- STATE_OK")
    print(chronyDienst)
    print(verbunden)
    print("Die Synchronisation meldet keine Probleme bezueglich der Zeitabweichung.")
    exit(STATE_OK)   
elif state == "criti":
    print(program, "- STATE_CRITICAL")
    if notAktive == "yes":
        print(printZeitNichtAktiv)
        exit(STATE_CRITICAL)
    elif notCon == "yes":
        print(nichtVerbunden)
        print(chronyDienst)
        exit(STATE_CRITICAL)
    elif printwarn == "yes" and notCon == "yes":
        print(nichtVerbunden)
        print(warnMessage)
        print(chronyDienst)
        exit(STATE_CRITICAL)     
        
        
elif state == "warn":
    print(program, "- STATE_WARNING")
    print(warnMessage)
    print(chronyDienst)
    print(verbunden)
    exit(STATE_WARNING)
  
