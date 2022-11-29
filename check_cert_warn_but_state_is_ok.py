#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 16 19:37:22 2021

@author: michael
"""

# This certificate check reports the expiry of certificates only at certain times and stays green in Icinga. If Icinga should only send a warning but should not stay on Warning or Critical in Icinga, this check is interesting. Standard certificate checks should be used for normal certificate checks.

program = "check_cert_warn_but_state_is_ok.py"


STATE_OK = 0
STATE_WARNING = 1
STATE_CRITICAL = 2
STATE_UNKNOWN = 3



import sys
from socket import socket
import OpenSSL
import ssl
from datetime import datetime, timedelta




# Tage vor Ablauf des Zertifikats an denen gewarnt wird.

timePeriods = [1, 7, 14, 21, 28]


# In diese Datei wird das Datum geschrieben an dem gewarnt wird und vor der nächsten Warnung wird geprüft ob schon gewarnt wurde.

warningFile1 = "/usr/lib/nagios/plugins/warningFile1"




def ins_log_schreiben(line):
    text_file = open(warningFile1, "a")
    text_file.write(line + "\n")
    text_file.close()
    


# Die übergabeparameter werden abgefragt und in Variablen geschrieben.

year = 0
month = 0
day = 0
count = 1

try:

    while count <= 4:
            
        if str("-hostIP") in sys.argv[count]:
            count = count + 1
            hostIP = str(sys.argv[count])
    
        if str("-port") in sys.argv[count]:
            count = count + 1
            port = int(sys.argv[count])
                      
        else:
            count = count + 1

except:
    print(program + " - HostIP und Port muss mit Skriptaufruf folgendermaßen übergeben werden: -hostIP IP Adresse -port 8443")
    exit(STATE_UNKNOWN)


# Das Zertifikat wird geprüft.

cert=ssl.get_server_certificate((hostIP, port))
x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)


#  Die Enddatum wird ermittelt.

endeDate = datetime.strptime(x509.get_notAfter().decode('ascii'), '%Y%m%d%H%M%SZ')


#  Die Gültigkeit des Zertifikats wird ausgerechnet.
     

currentDate = datetime.now()
lastCert = endeDate - currentDate



if "-" in str(lastCert):
    
   print(program + " - CRITICAL - Aber in Icinga wird die Meldung als OK angzeigt weil der IT nicht die Ueberwachung der Zertifikate uebernimmt. Der / die  Applikationsverantwortliche/n wurde/n informiert.")
   print("Das Zertifkat ist seit " + str(abs(lastCert)) + " nicht mehr gueltig. Bitte ein neues Zertifikat bei der IT ueber ein Ticket beantragen.")
   exit(STATE_OK)
   
elif str(lastCert) == str("0:00:00"):

    print(program + " - CRITICAL - Aber in Icinga wird die Meldung als OK angzeigt weil der IT nicht die Ueberwachung der Zertifikate uebernimmt. Der / die  Applikationsverantwortliche/n wurde/n informiert.")
    print("Das Zertifikat ist seit heute nicht mehr gueltig. Bitte ein neues Zertifikat bei der IT ueber ein Ticket beantragen.")
    exit(STATE_OK)


# Prüfen ob Critical verschickt werden muss.

for tp in timePeriods:
    
    days = timedelta(tp)
    #print("days" + str(days))
    checkDate = endeDate - days
    checkDDate = str(checkDate)
    checkdate = (checkDDate.strip())
    check_date = checkdate.split()[0]
    logEintrag = str(hostIP) + " " + str(checkDate)
    #print("logEintrag" + str(logEintrag))    
    with open(warningFile1) as f:       
     
        #print("ist currentDate: " + str(currentDate) + "in check_date: " + str(check_date))
        if str(check_date) in str(currentDate) and str(logEintrag) not in f.read():
         
            ins_log_schreiben(str(logEintrag))
         
            print(program + " - CRITICAL - Bitte neues Zertifikat bei der IT ueber ein Ticket beantragen.")
            print("Das Zertifiakt ist noch " + str(lastCert) + " bis zum " + str(endeDate) + " gueltig.")
            print(str(timePeriods) + " Tage vor Ablauf des Zertifikats wurden / werden Warnungen an den / die Applikationsverantwortlichen gesendet.")
            exit(STATE_CRITICAL)

print(program +" - Das Zertifiakt ist noch " + str(lastCert) + " bis zum " + str(endeDate) + " gueltig.")
print(str(timePeriods) + " Tage vor Ablauf des Zertifikats wurden / werden Warnungen an den / die Applikationsverantwortlichen gesendet.")
exit(STATE_OK)

