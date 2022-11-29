#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 15:50:05 2021

@author: michael
"""


# Change calcit with your systemd sercice.


program = "check_systemd_sercice.py"

STATE_OK = 0
STATE_WARNING = 1
STATE_CRITICAL = 2
STATE_UNKNOWN = 3



# will return 0 for active else inactive.

import os
status = os.system('systemctl is-active --quiet calcit')



if status == 0:
    print(program, "- OK - calcit ist aktiv.")
    exit(STATE_OK)

else:
    print(program, "- STATE_CRITICAL - calcit ist nicht aktiv.")
    exit(STATE_CRITICAL)
