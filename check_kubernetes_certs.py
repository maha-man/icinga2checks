#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Michael
25.07.2022
"""


import os
import subprocess
from datetime import datetime, timedelta


program = "check_kubernetes_certs.py"


STATE_OK = 0
STATE_WARNING = 1
STATE_CRITICAL = 2
STATE_UNKNOWN = 3


certs =  subprocess.getoutput("kubeadm certs check-expiration |grep -v 'check-expiration' |grep -v CERTIFICATE | sed /^$/d &> /dev/null")


dateList =[]

def extract_dateobject(line):
    line = (line.strip())
    date = line.split()[1:4]
    date = ' '.join(date)
    date = datetime.strptime(date,'%b %d, %Y')
    return date

for line in certs.splitlines():
    if not "The recommended value for" in line:
        dateList.append(extract_dateobject(line))
    

endeDate = min(dateList)

currentDate = datetime.now()

lastCert = endeDate - currentDate

daysC = timedelta(10)

daysW = timedelta(30)


if "-" in str(lastCert):
    
   print(program + " - CRITICAL - Das aelteste Kubernetes Zertifkat ist seit " + str(abs(lastCert)) + " nicht mehr gueltig. Bitte ein neues Zertifikat erzeugen und einspielen.")
   print(certs)
   exit(STATE_CRITICAL)


if str(lastCert) == str("0:00:00"):

    print(program + " - CRITICAL - Das aelteste Kubernetes Zertifikat ist seit heute nicht mehr gueltig. Bitte ein neues Zertifikat erzeugen und einspielen.")
    print(certs)
    exit(STATE_CRITICAL)


if lastCert <= daysC:
   print(program + " - STATE_CRITICAL - Das aelteste  Kubernetes Zertifikat ist noch " + str(lastCert) + " Tage bis zum " + str(endeDate) + " gueltig.")
   print(certs)
   exit(STATE_CRITICAL)


if lastCert <= daysW:

    print(program + " - WARNING - Das aelteste Kubernetes Zertifikat ist noch " + str(lastCert) + " Tage bis zum " + str(endeDate) + " gueltig.")
    print(certs)
    exit(STATE_WARNING)


print(program + " - OK - Das aelteste Kubernetes Zertifikat ist noch " + str(lastCert) + " bis zum " + str(endeDate) + " gueltig.")
print(certs)
exit(STATE_OK)
