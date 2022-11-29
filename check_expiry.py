#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created 2022

@author Michael Tschoepe
"""

program = "check_expiry.py"


STATE_OK = 0
STATE_WARNING = 1
STATE_CRITICAL = 2
STATE_UNKNOWN = 3


import sys, datetime



# Die übergabeparameter werden abgefragt und in Variablen geschrieben.

year = 0
month = 0
day = 0
count = 1

try:

    while count <= 8:
            
        if str("-year") in sys.argv[count]:
            count = count + 1
            year = int(sys.argv[count])
    
        if str("-month") in sys.argv[count]:
            count = count + 1
            month = int(sys.argv[count])
            
        if str("-day") in sys.argv[count]:
            count = count + 1
            day = int(sys.argv[count])
        
        if str("-hostIP") in sys.argv[count]:
            count = count + 1
            hostIP = str(sys.argv[count])
        else:
            count = count + 1

except:
    print(program + " - Das Ablaufdatum muss mit Skriptaufruf folgendermaßen übergeben werden: -hostIP 10.2.2.123 -year 2021 -month 6 -day 6")
    exit(STATE_UNKNOWN)
    

#  Die Gültigkeit wird ausgerechnet.
     
currentDate = datetime.date.today()
  
endeDate = datetime.date(year, month, day)

lastCert = endeDate - currentDate

daysC = datetime.timedelta(10)

daysW = datetime.timedelta(30)

#checkDate = endeDate - days

# Prüfen ob Warnung .

if "-" in str(lastCert):
    print(program + " - CRITICAL - Das zu Überwachende ist seit " + str(abs(lastCert)) + " nicht mehr gueltig.")
    print("Das zu Überwachende muss erneuert werden. Sobald dies getan wurde dies bitte dem Icinga Verantwortlichen mitteilen da hier die Ablaufzeit manuell eingegeben wird da das zu Überwachende nicht ueberprueft werden kann.")
    exit(STATE_CRITICAL)


if str(lastCert) == str("0:00:00"):

    print(program + "- CRITICAL - Das zu Überwachende ist seit heute nicht mehr gueltig.")
    print("Das zu Überwachende muss erneuert werden. Sobald dies getan wurde dies bitte dem Icinga Verantwortlichen mitteilen da hier die Ablaufzeit manuell eingegeben wird da das zu Überwachende nicht ueberprueft werden kann.")
    exit(STATE_CRITICAL)


if lastCert <= daysW:

    print(program + " - WARNING - Das zu Überwachende ist noch " + str(lastCert) + " Tage bis zum " + str(endeDate) + " gueltig.")
    print("Das zu Überwachende muss erneuert werden. Sobald dies getan wurde dies bitte dem Icinga Verantwortlichen mitteilen da hier die Ablaufzeit manuell eingegeben wird da das zu Überwachende nicht ueberprueft werden kann.")
    exit(STATE_WARNING)


if lastCert <= daysC:
   print(program + " - STATE_CRITICAL - Das zu Überwachende ist noch " + str(lastCert) + " Tage bis zum " + str(endeDate) + " gueltig.")
   print("Das zu Überwachende muss erneuert werden. Sobald dies getan wurde dies bitte dem Icinga Verantwortlichen mitteilen da hier die Ablaufzeit manuell eingegeben wird da das zu Überwachende nicht ueberprueft werden kann.")
   exit(STATE_CRITICAL)


print(program + " - OK - Das zu Überwachende ist noch " + str(lastCert) + " bis zum " + str(endeDate) + " gueltig.")
print("Falls das zu Überwachende erneuert wurde dies bitte dem Icinga Verantwortlichen mitteilen da hier die Ablaufzeit manuell eingegeben wird da das zu Überwachende nicht ueberprueft werden kann.")
exit(STATE_OK)

