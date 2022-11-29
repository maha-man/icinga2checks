# -*- coding: utf-8 -*-




"""
Created on Thu Apr 15 18:23:50 2021

@author: michael

Skrippt durchsucht verschieden Logs mit verschiedennen Werten.

"""

program = "check_log.py"



# Hier können beliebig viele Werte eingetagen werden nach denen gesucht werden soll.
# replace values

gesuchteWerte = ['wert1','wert2','wert3']

# Hier wird der Pfad zu den Logs eingegeben (bei windows, am Ende muessen zwei \\ stehen):

# replace logpath

logpath = 'D:\path\log\\'

# Hier werden die zu ueberpreufenden Logs eingetraen.
#replace logfilname

logs = ['log1', 'log2', 'log3



import pprint
from sys import exit

STATE_OK = 0
STATE_WARNING = 1
STATE_CRITICAL = 2
STATE_UNKNOWN = 3

log_fund = {}


# Replace path

warningFile = "D:\path\warningFile.txt"

countNOk = 0
countOk = 0
countLog = 0
countNotFound = 0
countWert = 0

anzahlGesuchteWerte =len(gesuchteWerte)
anzahLogs = len(logs)



def ins_log_schreiben(line):
    text_file = open(warningFile, "a")
    text_file.write(line)
    text_file.close()
    


while countLog < anzahLogs:
  
    for line in open(logpath + logs[countLog]):
              
        for wert in gesuchteWerte:
        
            if wert in line and line not in open(warningFile):
        
                ins_log_schreiben(line)
                log_fund[logs[countLog]] = line
                countNOk = countNOk + 1
                

                
    countLog = countLog + 1



if countNOk == 0:
    print(program, "- OK - In den Logs wurden keine aktuellen Probleme erkannt.")
    print("Der / die gesuchte(n) Wert(e):")
    print(gesuchteWerte)
    print("wurde(n) in den folgenden Logs aktuell nicht gefunden:")
    print(logs)
    exit(STATE_OK)  
        
else:
    print(program, "- WARNING - In den Logs wurden Probleme erkannt.")
    print()
    print("Der / die gesuchte(n) Wert(e):")
    print(gesuchteWerte)
    print("wurde(n) gefunden. Zum jeweiligen Log wird im Icina nur der letzte Fund angzeigt.")
    print("Alle " + str(countNOk) + " Funde wurden zu diesem File hinzugefuegt: \"" + warningFile +"\"")
    print("")
    pprint.pprint(log_fund)
    exit(STATE_WARNING)




