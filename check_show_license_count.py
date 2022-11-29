# -*- coding: utf-8 -*-

"""
Created on Fri May 28 10:41:04 2021

@author: michael
"""


program = "check_show_license_count.py"


import os
from file_read_backwards import FileReadBackwards


STATE_OK = 0
STATE_WARNING = 1
STATE_CRITICAL = 2
STATE_UNKNOWN = 3


# Hier wird der Pfad zu den Logs eingegeben (am Ende muessen zwei \\ stehen wenn es sich um Windows handlet):

path = 'D:\path\Logs\\'


# Es wird geprüft wieviele Lizenzen verwendet werden.

def howMany(licenceType, log):
    for line in log:
        if licenceType in line:
		    # Nummer aus String entnehmen.
            number = [int(s) for s in line.split() if s.isdigit()]
            # Eckige Klammmer von Nummer entfernen.
            lice = str(number)[1:-1]
            return lice


# Die aktuellsten Logs werden sortiert.

os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)


# In den aktuellsten Logs werden die richtigen Logs gefunden und dann wird die Anzahl der jeweiligen Lizenen aufgrund der aktuellsten Eintraege geprueft.

count = -1

while True:
    
    newest = files[count] 
    
    if newest.startswith("ot-20") and not newest.endswith("act.log"):
	
        with FileReadBackwards(path + newest, encoding="utf-8") as log:
        
        
        # Replace strings
		
            AutomationLicenses = str(howMany("Automation Interface Licenses", log))
			
            ClientLicenses = str(howMany("Client Licenses", log))
                 
            print(program + " - Derzeit werden " + AutomationLicenses + " Automation Licenses und " + ClientLicenses + " Client Licenses genutzt.")
            print("|'AutomationLicenses'=" + AutomationLicenses)
            print("|'ClientLicenses'=" + ClientLicenses)
            exit(STATE_OK)  
 
    else:
        count = count + -1

