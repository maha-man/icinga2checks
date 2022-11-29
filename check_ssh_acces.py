#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created 7.9.2021

@author: michael
"""

program = "check_ssh_acces.py"

# Accesses are deactivated via cron and this is written to a log. This check reads the log and then outputs the status accordingly.


STATE_OK = 0
STATE_WARNING = 1
STATE_CRITICAL = 2
STATE_UNKNOWN = 3


from datetime import datetime
from file_read_backwards import FileReadBackwards


# replace server

serverGroup = ["server1", "server2", "server3", "server4"]

dateToday = datetime.today().strftime('%Y-%m-%d')

current_time = datetime.now().strftime('%Y-%m-%d %H:%M')


#replace filname and ath

log = 'path/filename.log'


nologin = 0

bash = 0


with FileReadBackwards(log, encoding="utf-8") as log:
    for line in log:

        
        if "nologin" in line and "server1" in line and dateToday in line and nologin <= 4:
            nologin += 1
        elif "nologin" in line and "server2" in line and dateToday in line and nologin <= 4:
            nologin += 1
        elif "nologin" in line and "server3" in line and dateToday in line and nologin <= 4:
            nologin += 1
        elif "nologin" in line and "server4" in line and dateToday in line and nologin <= 4:
            nologin += 1
        elif "bash" in line and "server1" in line and dateToday in line and bash <= 4:
            bash += 1
        elif "bash" in line and "server2" in line and dateToday in line and bash <= 4:
            bash += 1
        elif "bash" in line and "server3" in line and dateToday in line and bash <= 4:  
            bash += 1
        elif "bash" in line and "server4" in line and dateToday in line and bash <= 4:
            bash += 1
             
             
if nologin >= 4:
    print(program + " - OK - Crontab ist gelaufen. Zu den Servern: " + str(serverGroup) + " ist der Zugang zum Zeitpunkt der Ausfuehrung dieses Checks deaktiviert. Dieser Check wurde am " + str(current_time) + " ausgefuehrt.")
    exit(STATE_OK)
elif bash >= 4:
    print(program + " - CRITICAL - Crontab ist gelaufen. Zu den Servern: " + str(serverGroup) + " ist der Zugang zum Zeitpunkt der Ausfuehrung dieses Checks aber aktiv. Bitte pruefen warum der Zugang aktiv ist. Dieser Check wurde am " + str(current_time) + " ausgefuehrt.")
    exit(STATE_CRITICAL)
else:
    print(program + " - CRITICAL - Crontab ist nicht gelaufen oder konnte nicht fuer alle Server ausgefuehrt werden. Bitte pruefen ob der Zugang zu den Servern: " + str(serverGroup) + " deaktiviert ist. Dieser Check wurde am " + str(current_time) + " ausgeführt.")
    exit(STATE_CRITICAL)
        
             








    
    



  


