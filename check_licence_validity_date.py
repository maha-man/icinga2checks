#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 16 19:37:22 2021

@author: Michael
"""

program = "check_licence_validity_date.py"

# Ohne Übergabeparameter


STATE_OK = 0
STATE_WARNING = 1
STATE_CRITICAL = 2
STATE_UNKNOWN = 3


import sys, datetime
from sys import exit



def extract_days(nmbrDayOb):
    nmbrDay = str(nmbrDayOb)
    nmbrDay = nmbrDay.strip()
    nmbrDay = nmbrDay.split()[0]
    nmbrDay = int(nmbrDay)
    return nmbrDay



    

# Replace Department

responsible = "Department" 


# Replace values

asset = "asset"

day = 31 

month = 12 

year =  2022

warnDay = 20 

critDay = 10



warning = datetime.timedelta(warnDay)

critical = datetime.timedelta(critDay)
    
currentDate = datetime.date.today()
  
endeDate = datetime.date(year, month, day)

lastLicence = endeDate - currentDate

lastLiDays =  extract_days(lastLicence)


if "-" in str(lastLicence):
    
   print(responsible + " - " + program + " - CRITICAL - Die Lizenz fuer " + str(asset) +  " ist seit " + str(abs(lastLiDays)) + " Tagen nicht mehr gueltig. Bitte neue Lizenz beantragen.")
   exit(STATE_CRITICAL)
   
   

elif str(lastLicence) == str("0:00:00"):

    print(responsible + " - " + program + " - CRITICAL - Die Lizenz fuer " + str(asset) +  " ist seit heute nicht mehr gueltig. Bitte neue Lizenz beantragen.")
    exit(STATE_CRITICAL)




critDate = endeDate - critical
warnDate = endeDate - warning


hwMnyDy = endeDate - currentDate



hwMnyDy = extract_days(hwMnyDy)



if currentDate >= critDate:

        print(responsible + " - " + program + " - CRITICAL - Die Lizenz fuer " + str(asset) +  " ist nur noch " + str(hwMnyDy) + " Tage bis zum "  + str(endeDate) + " gueltig. Bitte neue Lizenz beantragen.")
        exit(STATE_CRITICAL)


if currentDate >= warnDate:

        print(responsible + " - " + program + " - WARNING - Die Lizenz fuer " + str(asset) +  " ist nur noch " + str(hwMnyDy) + " Tage bis zum "  + str(endeDate) + " gueltig. Bitte neue Lizenz beantragen.")
        exit(STATE_WARNING)


print(responsible + " - " + program + " - OK - Die Lizenz fuer " + str(asset) +  " ist noch " + str(hwMnyDy) + " Tage bis zum "  + str(endeDate) + " gueltig.")
exit(STATE_OK)



