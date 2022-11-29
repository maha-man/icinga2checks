#!/bin/bash


# :: Output:
#       ok  : Abruf und Vergleich positiv, ok
#       nok : Abruf fehlerhaft (Server nicht erreichbar) oder Rückgabewerte abweichend.
# ---


AUTHOR="Michael" 

PROGNAME="check_url_response.sh"


# Exit codes

STATE_OK=0
STATE_WARNING=1
STATE_CRITICAL=2
STATE_UNKNOWN=3


# -- zu verwendender PTV Server

# replace server

server_=server


# -- erwarteter Rückgabewert der Anfrage

# replace string

EXPECT='string'


# -- Abruf

# replace url

ANSWER=$(curl -s -X GET -H "Content-Type: application/json" url)


# -- Auswertung

if [ "$ANSWER" = "$EXPECT" ]; then

echo

echo " $PROGNAME: OK - Der Monitoringcheck zeigt dass der Abruf in Ordnung ist."

echo

exit $STATE_OK

else

echo "RESPONSIBLE: TCDA / CS - $PROGNAME: CRITICAL -  Der Monitoringcheck fuer den Server $server_ zeigt dass der Abruf einer Musterkarte nicht in Ordnung ist ."

echo

echo Folgendes Ergebniss wird erwartet:

echo

echo $EXPECT 

echo

echo Dises Ergebniss wurde uebermittelt:

echo

echo $ANSWER

exit $STATE_CRITICAL


fi
