# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 17:01:32 2021

@author: michael
"""

program = "check_http_content.py"


from sys import exit
import requests
import warnings
warnings.filterwarnings("ignore")

STATE_OK = 0
STATE_WARNING = 1
STATE_CRITICAL = 2
STATE_UNKNOWN = 3



url_string = "url"

werteOK = ["key1: value2", "key2: value2", "key3: value3", "key3: value3"]
anzahlListe = len(werteOK)

response = requests.get(url_string, verify = False)
content = response.content

count = 0 

while count < anzahlListe:
    
    if werteOK[count] in str(content):
        count = count + 1
    
    else:
        print(program + '- STATE_CRITICAL')
        print("Das Ergebnis vom monitoring ist nicht wie erwartet.")
        print()
        print("Folgendes Ergebniss wird erwartet:")
        print("\n".join(werteOK))
        print()
        print("Dises Ergebniss wurde uebermittelt:")
        print(content)
        exit(STATE_CRITICAL)

print(program, "- OK")
print("Das Ergebniss vom mMnitoring ist wie erwartet:")
print("\n".join(werteOK))
exit(STATE_OK)
    
