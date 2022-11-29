#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 10.12.2021 Michael 

# check temperature with raspberry pi and linkerkit

program = "check_senrasp_temp.py"


import glob 
import time 
from time import sleep 
import RPi.GPIO as GPIO 
import sys

STATE_OK = 0
STATE_WARNING = 1
STATE_CRITICAL = 2
STATE_UNKNOWN = 3

# An dieser Stelle kann die Pause zwischen den einzelnen Messungen eingestellt werden 
 
#sleeptime = 1 
# Der One-Wire EingangsPin wird deklariert und der integrierte PullUp-Widerstand aktiviert 
 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
 
# Nach Aktivierung des Pull-UP Widerstandes wird gewartet, 
# bis die Kommunikation mit dem DS18B20 Sensor aufgebaut ist 
 
base_dir = '/sys/bus/w1/devices/' 

while True: 
    try: 
        device_folder = glob.glob(base_dir + '28*')[0] 
        break 
    except IndexError: 
        sleep(0.5) 
        continue 

device_file = device_folder + '/w1_slave' 


# Funktion wird definiert, mit dem der aktuelle Messwert am Sensor ausgelesen werden kann 
 
def TemperaturMessung(): 
    f = open(device_file, 'r') 
    lines = f.readlines() 
    f.close() 
    return lines 


# Zur Initialisierung, wird der Sensor einmal "blind" ausgelesen 

TemperaturMessung() 

# Die Temperaturauswertung: Beim Raspberry Pi werden erkennte one-Wire Slaves im Ordner 
# /sys/bus/w1/devices/ einem eigenen Unterordner zugeordnet. In diesem Ordner befindet sich die Datei w1-slave 
# in dem Die Daten, die über dem One-Wire Bus gesendet wurden gespeichert. 
# In dieser Funktion werden diese Daten analysiert und die Temperatur herausgelesen und ausgegeben 
 

def TemperaturAuswertung(): 
    lines = TemperaturMessung() 
    while lines[0].strip()[-3:] != 'YES': 
        time.sleep(0.2) 
        lines = TemperaturMessung() 
    equals_pos = lines[1].find('t=') 
    if equals_pos != -1: 
        temp_string = lines[1][equals_pos+2:] 
        temp_c = float(temp_string) / 1000.0 
        return temp_c 
                 

temp = TemperaturAuswertung()

count = 0

try:

    while count <= 4:

        if str("-warningSchwellWert") in sys.argv[count]:
            count = count + 1
            warningSchwellWert = int(sys.argv[count])

        if str("-criticalSchwellWert") in sys.argv[count]:
            count = count + 1
            criticalSchwellWert = int(sys.argv[count])

        else:
            count = count + 1

except:
    print(program + " -warningSchwellWert und -criticalSchwellWert muss mit Skriptaufruf folgendermaßen übergeben werden: -criticalSchwellWert 40 -warningSchwellWert 30")
    exit(STATE_UNKNOWN)


if temp >= criticalSchwellWert:

    print(program + " - CRITICAL - Der Temperatur CRITICAL Schwellwert wurde überschritten.")
    print("Die Temperatur betraegt: " + str(temp) + " Grad Celsius. |'TEMP-Wert'=" + str(temp))
    exit(STATE_CRITICAL)

elif temp >= warningSchwellWert:
    print(program + " - WARNING - Der Temperatur WARNING Schwellwert wurde überschritten.")
    print("Die Temperatur betraegt: " + str(temp) + " Grad Celsius. |'TEMP-Wert'=" + str(temp))
    exit(STATE_WARNING)

else:
    print(program + " - OK - Die Temperatur Schwellwerte wurden nicht ueberschritten.")
    print("Die Temperatur betraegt: " + str(temp) + " Grad Celsius.  |'TEMP-Wert'=" + str(temp))
    exit(STATE_OK)






