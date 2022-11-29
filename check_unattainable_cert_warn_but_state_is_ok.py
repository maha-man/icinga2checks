#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 16 19:37:22 2021

@author: ubuntu
"""

program = "check_unattainable_cert_warn_but_state_is_ok.py"

# Mit Übergabeparameter


# This certificate check reports the expiry of certificates only at certain times and stays green in Icinga. If Icinga should only send a warning but should not stay on Warning or Critical in Icinga, this check is interesting. Standard certificate checks should be used for normal certificate checks.




STATE_OK = 0
STATE_WARNING = 1
STATE_CRITICAL = 2
STATE_UNKNOWN = 3


import sys, datetime


# Tage vor Ablauf des Zertifikats an denen gewarnt wird.

timePeriods = [1, 7, 14, 21, 28]


# In diese Datei wird das Datum geschrieben an dem gewarnt wird und vor der nächsten Warnung wird geprüft ob schon gewarnt wurde.

warningFile = "/usr/lib/nagios/plugins/warningFile"


def ins_log_schreiben(line):
    text_file = open(warningFile, "a")
    text_file.write(line + "\n")
    text_file.close()
    


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
    print(program + " - Das Ablaufdatum muss mit Skriptaufruf folgendermaßen übergeben werden: -hostIP IP Adresse -year 2021 -month 6 -day 6")
    exit(STATE_UNKNOWN)
    

#  Die Gültigkeit des Zertifikats wird ausgerechnet.
     
currentDate = datetime.date.today()
  
endeDate = datetime.date(year, month, day)

lastCert = endeDate - currentDate

if "-" in str(lastCert):
    
   print(program + "- CRITICAL - Aber in Icinga wird die Meldung als OK angzeigt weil IT nicht die Ueberwachung der Zertifikate uebernimmt. Der Applikationsverantwortliche wurde informiert.")
   print("Das Zertifkat ist seit " + str(abs(lastCert)) + " nicht mehr gueltig. Bitte neues Zertifikat bei IT ueber ein Ticket beantragen. Falls ein neues Zertifikat eingespielt wurde dies bitte dem Icinga Verantwortlicen mitteilen.")
   exit(STATE_OK)
   
   

elif str(lastCert) == str("0:00:00"):

    print(program + "- CRITICAL - Aber in Icinga wird die Meldung als OK angzeigt weil IT nicht die Ueberwachung der Zertifikate uebernimmt. Der Applikationsverantwortliche wurde informiert.")
    print("Das Zertifikat ist seit heute nicht mehr geultig. Bitte neues Zertifikat bei IT ueber ein Ticket beantragen. Falls ein neues Zertifikat eingespielt wurde dies bitte dem Icinga Verantwortlichen mitteilen.")
    exit(STATE_OK)

#    


# Prüfen ob Warnung verschickt werden muss. Wenn ja wird Warnung versendet.

for tp in timePeriods:
    
    days = datetime.timedelta(tp)

    checkDate = endeDate - days
    
    logEintrag = str(hostIP) + " " +  str(checkDate)
        
    with open(warningFile) as f:       
        
        if str(currentDate) in str(checkDate) and str(logEintrag) not in f.read():
         
            ins_log_schreiben(str(logEintrag))
         
            print(program + "- CRITICAL - Bitte neues Zertifikat bei IT ueber ein Ticket beantragen.")
            print("Das Zertifiakt ist noch " + str(lastCert) + " bis zum " + str(endeDate) + " gueltig.")
            print(str(timePeriods) + " Tage vor Ablauf des Zertifikats wurden / werden Warnungen an den Applikationsverantwortlichen gesendet.")
            print("Falls ein neues Zertifikat eingespielt wurde dies bitte dem Icinga Verantwortlichen mitteilen.")
            exit(STATE_CRITICAL)


print(program)
print("Das Zertifiakt ist noch " + str(lastCert) + " bis zum " + str(endeDate) + " gueltig.")
print(str(timePeriods) + " Tage vor Ablauf des Zertifikats  wurden / werden Warnungen an den Applikationsverantwortlichen gesendet.")
print("Falls ein neues Zertifikat eingespielt wurde dies bitte dem Icinga Verantwortlichen mitteilen.")
exit(STATE_OK)


