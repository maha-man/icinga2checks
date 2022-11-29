#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on September 2022

@author: michael
"""

import sys
import os
import subprocess


program = "check_db.py"

# repalce values

db = "mongod"

port = "27017"

STATE_OK = 0
STATE_WARNING = 1
STATE_CRITICAL = 2
STATE_UNKNOWN = 3



# will return 0 for active else inactive.

status = os.system('systemctl is-active --quiet ' + db)


scriptPath = os.path.abspath(os.path.dirname(sys.argv[0]))


command = subprocess.getoutput(scriptPath + '/extension_for_port_check.sh')


command = command.splitlines()


for line in command:

    if port in line and status == 0:
        print(program, " - OK - " + db + " DB ist aktiv und auf Port " + port + " wird gelauscht.")
        print(line)
        exit(STATE_OK)
else:
    print(program, " - CRITICAL - " + db + "  DB ist nicht aktiv und / oder auf Port " + port + " wird nicht gelauscht.")
    exit(STATE_CRITICAL)




