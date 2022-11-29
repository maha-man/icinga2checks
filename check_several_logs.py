# -*- coding: utf-8 -*-




"""
Created on Thu Apr 15 18:23:50 2021

@author: michael

"""
# check in serveral logsfiles

import glob
import os
from sys import exit
import re

STATE_OK = 0
STATE_WARNING = 1
STATE_CRITICAL = 2
STATE_UNKNOWN = 3

program = "check_several_logs.py"

# change value

gesuchterWert = "Connection refused"

#replace path 

warningFile = "D:\path\warningFile.txt"
warningList = []



# replace path
list_of_files = glob.glob('D:\path\log\*')
latest_file = max(list_of_files, key=os.path.getmtime)
anzehlWert = open(latest_file, 'r').read().count(gesuchterWert)

#print(latest_file)

if anzehlWert == 0:
    print(program, "- OK")
    print("Aktuell bestehen bei der Anmeldung keine Probleme mit: \"" + gesuchterWert + "\"")
    exit(STATE_OK)    



pattern = re.compile(gesuchterWert)

countNOk = 0
countOk = 0
count = 0

while count <= anzehlWert:

    for line in open(latest_file):
        count = count + 1 
        
        for match in re.finditer(pattern, line):

            if line not in open(warningFile):
                
                text_file = open(warningFile, "a")
                text_file.write(line)
                text_file.close()
                warningList.append(line)
                countNOk = countNOk + 1
            else:
                countOk = countOk + 1


                
if anzehlWert == countOk:
    print(program, "- OK")
    print("Aktuell bestehen bei der Anmeldung keine Probleme mit: \"" + gesuchterWert + "\"")
    exit(STATE_OK) 
else:
    print(program, "- WARNING")

    print ("Es koenen derzeit Probleme bei der Anmeldung bestehen.")
    print("Seit der letzen Warnungsmeldung ist/sind im Log \"" + latest_file + "\" " + str(countNOk) + " Anmeldungsproblem(e) mit: \"" + gesuchterWert + "\" aufgezeichnet worden:") 
    print()
    print(warningList)
    exit(STATE_WARNING)

























#alt



# """

# Michael Tschoepe

# 08.04.2021

# """
# # zeile einfügen

# program = "check_login"

# gesuchterWert = "Connection refused"

# STATE_OK = 0
# STATE_WARNING = 1
# STATE_CRITICAL = 2
# STATE_UNKNOWN = 3

# import glob
# import os
# from sys import exit


# list_of_files = glob.glob('D:\mobilex\mxdispatch\log\*')
# latest_file = max(list_of_files, key=os.path.getmtime)

# anzehlWert = open(latest_file, 'r').read().count(gesuchterWert)


# if anzehlWert == 0:
    # print(program, "- OK")
    # print("Aktuell bestehen bei der Anmeldung keine Probleme mit: \"" + gesuchterWert + "\"")
    # exit(STATE_OK)          
# else:
    # print(program, "- WARNING")
    # print ("Es koenen derzeit Probleme bei der Anmeldung bestehen.")
    # print("Im aktuellsten Log \"" + latest_file + "\" kommt der Wert: \"" + gesuchterWert + "\" insgesammt " + str(anzehlWert) + " mal vor.") 
    # exit(STATE_WARNING)