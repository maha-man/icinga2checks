#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 08.11 2021

@author: michael
"""



import os

program = "check_middleware"

STATE_OK = 0
STATE_WARNING = 1
STATE_CRITICAL = 2
STATE_UNKNOWN = 3


mware = os.popen('/root/check_middleware.pl').read()


if str("Service PROD/m_listen on port 8095 is running") in mware and str("Service PROD/ServiceNET_listen on port 8101 is running") in mware:
    print(program, " - STATE OK")
    print(mware)
    exit(STATE_OK)


startMware = os.system('/root/start_middleware_prod.sh')
startMware 

import time
time.sleep(3)



if str("Service PROD/m_listen on port 8095 is running") in mware and str("Service PROD/ServiceNET_listen on port 8101 is running") in mware:
    print(program, " - STATE OK")
    print(mware)
    exit(STATE_OK)


print(program + '- STATE_CRITICAL')
print(mware)
exit(STATE_CRITICAL)
