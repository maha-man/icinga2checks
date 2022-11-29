#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created 9.5.2022

@author: michael
"""

import os
import time


program = "check_ceph_hold-packages.py"

STATE_OK = 0
STATE_WARNING = 1
STATE_CRITICAL = 2
STATE_UNKNOWN = 3


global hold


# in die Liste die Pakete eintragen die auf hold gesetzt sein sollen

hold = ["ceph-base", "ceph-common", "ceph-mds", "ceph-mgr", "ceph-mgr-modules-core", "ceph-mon", "ceph-osd", "mysql-common", "ceph", "ceph-fuse", "ceph-immutable-object-cache", "ceph-iscsi", "ceph-mgr-cephadm", "ceph-mgr-dashboard", "ceph-mgr-diskprediction-local", "ceph-mgr-k8sevents", "ceph-mgr-rook", "ceph-resource-agents", "cephadm", "cephfs-shell"]


def showhold():
    showhold = os.popen('apt-mark showhold').read()
    showhold = showhold.split()
    return showhold


def checkhold():
    ishold = showhold()
    dif = set(hold) - set(ishold)
    return dif


dif = checkhold()


if dif != set():
    os.system('apt-mark hold ceph*')
    time.sleep(7)
    dif = checkhold()
    showhold = showhold()


if dif == set():

    print(program + ' - STATE OK - Es sind mindestens alle Cluster apt Pakete auf hold gesetzt die auf hold gesetzt sein muessen:')
    print(hold)
    exit(STATE_OK)


print(program + ' - STATE_CRITICAL - Es sind nicht alle Cluster apt Pakete auf hold gesetzt die auf hold gesetzt sein sollen.')
print('Diese Pakete muessen auf hold gesetzt sein:')
print(hold)
print('Diese Pakete sind auf hold gesetzt:')
print(showhold)
print("Diese(s) Paket(e) fehlen / fehlt:")
print(dif)
exit(STATE_CRITICAL)




