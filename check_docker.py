#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 17:26:28 2021

@author: michael
"""

# The values of the transfer parameters dock 1 and dock2 are used to check whether the corresponding containers are running.

import os, sys

program = "check_docker"

STATE_OK = 0
STATE_WARNING = 1
STATE_CRITICAL = 2
STATE_UNKNOWN = 3



# will return 0 for active else inactive.

status = os.system('systemctl is-active --quiet docker')

dockerps = os.popen('docker ps').read()


if status == 0:
    dockerStatus = "docker ist aktiv."
else:
    print(program, "- STATE_CRITICAL - docker ist nicht aktiv.")
    exit(STATE_CRITICAL)


if "dock1" in sys.argv[1] or sys.argv[3]:
    if sys.argv[2] in dockerps:
        wert1 = ('Der Wert ' + sys.argv[2] + ' wird mit docker ps angezeigt. Der entsprechnede Container laeuft.')
        if "dock2" in sys.argv[1] or sys.argv[3]:
            if sys.argv[4] in dockerps:
                wert2 = ('Der Wert ' + sys.argv[4] + ' wird mit docker ps angezeigt. Der entsprechnede Container laeuft.')
                print(program, " - STATE OK")
                print(dockerStatus)
                print(wert1)
                print(wert2)
                exit(STATE_OK)

print(program + '- STATE_CRITICAL')
print(dockerStatus + ' Aber einer oder beide der Werte ' + sys.argv[2] + ' und / oder ' + sys.argv[4] + ' werden nicht mit docker ps angezeigt.')
print('Der oder die entsprechende(n) Container laeuft / laufen nicht.')
exit(STATE_CRITICAL)
