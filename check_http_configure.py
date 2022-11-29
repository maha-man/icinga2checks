#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 12.01 2022

@author: michael
"""

program = "check_http_content_configure.py"

import sys
from sys import exit
import requests
import warnings
warnings.filterwarnings("ignore")



STATE_OK = 0
STATE_WARNING = 1
STATE_CRITICAL = 2
STATE_UNKNOWN = 3



year = 0
month = 0
day = 0
count = 1

try:

    while count <= 6:
            
        if str("-url") in sys.argv[count]:
            count = count + 1
            url = str(sys.argv[count])
    
        if str("-responsible") in sys.argv[count]:
            count = count + 1
            responsible = str(sys.argv[count])
        
        if str("-wert_ok") in sys.argv[count]:
            count = count + 1
            wert_ok = str(sys.argv[count])



        else:
            count += 1

except:

    print(program + ' - Parameter muessen mit Skriptaufruf uebergeben werden: -wert_ok -responsible -url')
    exit(STATE_UNKNOWN)



try:

    response = requests.get(url, verify = False)    
    content = response.content

except:

    print(responsible + " - " + program + " - STATE_CRITICAL - Das Ergebnis vom Monitoring ist nicht wie erwartet da keine Verbindung zu dieser URL aufgebaut werden kann:")
    print(url)
    print()
    print("Folgendes Ergebniss wird erwartet:")
    print(wert_ok)
    exit(STATE_CRITICAL)
    


if wert_ok in str(content):
    pass

else:
    print(responsible + " - " + program + " - STATE_CRITICAL - Das Ergebnis vom Monitoring ist nicht wie erwartet.")
    print("Diese URL wird geprueft:")
    print(url)
    print()
    print("Folgendes Ergebniss wird erwartet:")
    print(wert_ok)
    print()
    print("Dises Ergebniss wurde uebermittelt:")
    print(content)
    exit(STATE_CRITICAL)

print(responsible + " - " +  program, " - OK - Das Ergebnis vom Monitoring ist wie erwartet.")
print("Diese URL wird geprueft:")
print(url)
print()
print("Das erwartete Ergebnis wurde uebermittelt:")
print(content)
exit(STATE_OK)

