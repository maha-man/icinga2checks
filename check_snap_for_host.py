#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 23.05 2022

@author: michael
"""
# in case vspheredb doesn't show any warnings for snaps, although it should


import os
import sys


program = "check_snap_for_host.py"

STATE_OK = 0
STATE_WARNING = 1
STATE_CRITICAL = 2
STATE_UNKNOWN = 3


host = sys.argv[2]

snap  = os.popen('icingacli vspheredb check vm --name ' + host + ' |grep snapshot').read()


if str('[OK] There are no snapshots') in snap:

    print(program, "- STATE OK - Keine Snapshots sind aktiv fuer " + host + ":")
    print(snap)
    exit(STATE_OK)

else:

    print(program, "- STATE_CRITICAL  - Snapshot(s) ist / sind  aktiv fuer " + host + ":")
    print(snap)
    exit(STATE_CRITICAL)

