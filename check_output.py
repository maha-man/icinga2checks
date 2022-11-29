#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on November 2021

@author: michael
"""

import os
import subprocess
            
program = "check_output.py"

STATE_OK = 0
STATE_WARNING = 1
STATE_CRITICAL = 2
STATE_UNKNOWN = 3


# change values

mongoAnswer = subprocess.getoutput("mongo ip test") 

mongoExpect = "Implicit session: session"


if mongoExpect in str(mongoAnswer):
    print(program, " - OK - Erwartete Antwort kommt zurück.")
    exit(STATE_OK)
else:
    print(program, " - CRITICAL - Erwartete Antwort kommt nicht zurück.")
    exit(STATE_CRITICAL) 
