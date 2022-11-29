#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created 6.9.2021

@author: michael
"""

program = "check_user_login_time.py"


STATE_OK = 0
STATE_WARNING = 1
STATE_CRITICAL = 2
STATE_UNKNOWN = 3



import sys
import os
from datetime import datetime


# Die übergabeparameter werden abgefragt und in Variablen geschrieben.

count = 1

try:

    while count <= 4:
            
        if str("-user") in sys.argv[count]:
            count = count + 1
            user = str(sys.argv[count])
            
        if str("-hourAllowed") in sys.argv[count]:
            count = count + 1
            hourAllowed = str(sys.argv[count])
                      
        else:
            count = count + 1

except:
    print(program + " - user und time in Stunden muss mit Skriptaufruf folgendermaßen übergeben werden: -user user -hourAllowed 4")
    exit(STATE_UNKNOWN)


minutesAllowed = int(hourAllowed) * 60


whoUser = os.popen('who -u').read()

loginAllowed = os.popen('grep ' + user + ' /etc/passwd').read() 

if str(user) not in str(whoUser) and "nologin" in loginAllowed:
    print(program + " - OK - Der User " + str(user) + " ist nicht angemeldet und der Zugang ist deaktiviert.")
    exit(STATE_OK)
elif str(user) not in str(whoUser) and "bash" in loginAllowed:
    print(program + " - OK -  Der User " + str(user) + " ist nicht angemeldet aber der Zugang ist aktiviert.")
    exit(STATE_OK)


for line in whoUser.split("\n"):
    if user in line:
        userLine = (line.strip())
       
        date = userLine.split()[2]
        time = userLine.split()[3]
        stringDateLogin = (date + str(" ") + time)

        datetimeObjLogin = datetime.strptime(stringDateLogin, '%Y-%m-%d %H:%M')

        diff = datetime.now() - datetimeObjLogin
        minutesLogin = diff.total_seconds() / 60

        hoursLogin = minutesLogin / 60

        if int(minutesLogin) > int(minutesAllowed):
            print(program + "- CRITICAL - Der User " + str(user) + " ist seit " + str(hoursLogin) + " Stunden angemeldet.")
            print("Der User darf " + str(hourAllowed) + " Stunden angemeldet sein.")
            print("Bitte pruefen warum der Dienstleister so lange angemeldet ist.")
            exit(STATE_CRITICAL)
        else:
            print(program + " - OK - Der User " + str(user) + " ist seit " + str(hoursLogin) + " Stunden angemeldet.")
            print("Der User darf " + str(hourAllowed) + " Stunden angemeldet sein.")
            exit(STATE_OK)






    
    



  


