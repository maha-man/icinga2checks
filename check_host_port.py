#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 16 19:37:22 2021

@author: michael
"""

program = "check_host_port.py"


STATE_OK = 0
STATE_WARNING = 1
STATE_CRITICAL = 2
STATE_UNKNOWN = 3


import sys
import socket


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
    print(program + " - HostIP und Port muss mit Skriptaufruf folgendermaßen übergeben werden: -hostIP 10.2.2.73 -port 8443")
    exit(STATE_UNKNOWN)


a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

location = (hostIP, port)

result_of_check = a_socket.connect_ex(location)

a_socket.close()


if result_of_check == 0:

    print(program + " - OK - Port: " + str(port) + " ist offen bei Host: " + hostIP)
    exit(STATE_OK)
    
else:
    print(program + " - CRITICAL - Port: " + str(port) + " ist nicht offen bei Host: " + hostIP)
    exit(STATE_CRITICAL)

