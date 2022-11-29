#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created 01.08.2022

@author: michael
"""


import os
import subprocess


program = "check_mx_record.py"


STATE_OK = 0
STATE_WARNING = 1
STATE_CRITICAL = 2
STATE_UNKNOWN = 3

# replace url

def dig():
    dig = subprocess.getoutput('dig url mx')
    dig = dig.splitlines()
    return dig


def line_count():
    line_count = len(dig())
    return line_count


count = 0
count2 = 0


for line in dig():

    if 'mail.telent.de.' in line:

# replace value

        print(program + ' - STATE OK - Im MX Record ist value enthalten.')
        print(line)
        exit(STATE_OK)

    else:
        count += 1

        if count == line_count():

            os.system('systemctl restart dnsmasq')


            for line in dig():

                if 'mail.telent.de.' in line:

# replace value

                    print(program + ' - STATE OK - dnsmasq musste neu gestartet werden, jetzt ist der MX Record value enthalten.')
                    print(line)
                    exit(STATE_OK)

                else:
                    count2 += 1

                    if count2 == line_count():

# replace value

                        print(program + ' - STATE_CRITICAL - Trotz dnsmasq neustart ist im MX Record value nicht enthalten.')
                        print(str(dig()))
                        exit(STATE_CRITICAL)


