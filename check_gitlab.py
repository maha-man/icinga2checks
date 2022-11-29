#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 08:09:36 2021

@author: michael
"""



import os
            
program = "check_gitlab"

STATE_OK = 0
STATE_WARNING = 1
STATE_CRITICAL = 2
STATE_UNKNOWN = 3



gitDienste = ["alertmanager", "gitaly", "gitlab-exporter", "gitlab-workhorse", "grafana","logrotate", "nginx","node-exporter", "postgres-exporter","postgresql","prometheus","puma","redis","redis-exporter","sidekiq"]

gitlab = os.popen('gitlab-ctl status').read()

dienstYes = []
dienstNo = []

element = 0
elementRun = 0 
elementNoRun = 0


while element < 15:
    if ('run: ' + gitDienste[element]) in gitlab:
        hinzu = (gitDienste[element])
        dienstYes.append(hinzu)
        element = element + 1
        elementRun = elementRun + 1
    else:
        hinzu = (gitDienste[element])
        dienstNo.append(hinzu)
        element = element + 1
        elementNoRun = elementNoRun + 1
             

if elementRun == 15:
    print(program, "- STATE_OK")
    print("Alle 15 Dienste die git benoetigt sind aktiv:")
    print(dienstYes)
    exit(STATE_OK)
else:
    print(program, "- STATE_CRITICAL")
    print("Folgende(r) Dienst(e) sind / ist nicht aktiv:")
    print(dienstNo)
    exit(STATE_CRITICAL)
