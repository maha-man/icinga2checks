#!/bin/bash


################################################################################
# Nagios plugin to check if a reboot is required                        #
# Author: Michael
# Datum 28.12.2020                        #
################################################################################


PROGNAME="check_reboot.sh"

# Tage nach deinen neu gestartet werden soll

days=


# Exit codes
STATE_OK=0
STATE_WARNING=1
STATE_CRITICAL=2
STATE_UNKNOWN=3


#Main #########################################################################



# Der Parameter fuer die Tage wird uebergeben


if [[ -z "$1" || -z "$2" ]]


then

echo "$PROGNAME: Es muss eine Option und eine Anzahl von Tagen angegeben werden, zum Beispiel -d 23"

exit $STATE_UNKNOWN


elif [ "$2" -ge 0 ] && [ "$2" -le 1000 ]

then

# Tage sind als Zahl angegeben

days=$2


else

echo "$PROGNAME: Tage sind keine Zahl zwischen 0 und 1000"

exit $STATE_UNKNOWN


fi



# Es wird geprueft wieviel Tage der Server laeuft


day=$(uptime |awk '{print $4}')

if  [[ "$day" == "days," ]]

then

up=$(uptime |awk '{print $3}')

else

up=0

fi



# Es wird geprueft ob der Server einen Neustart benoetigt und ob der Server neugesartet werden soll


restart=$([ -f /var/run/reboot-required ] && cat /var/run/reboot-required)


if [[ -z "$restart" ]]


then

echo "$PROGNAME: OK - NO restart required - Das System laeuft seit $up Tagen."

exit $STATE_OK


elif [[ ! -z "$restart" ]] && [ "$up" -le "$days" ]

then

echo "$PROGNAME: OK - Es wird ein Neustart benoetigt aber eine Warnung soll aufgrund dem Wert (Anzahl Tage) in reboot_warning verzoegert werden. - Das System laeuft seit $up Tagen."

exit $STATE_OK



elif [[ ! -z "$restart" ]] && [ "$up" -gt "$days" ]

then

echo "$PROGNAME: $restart Das System laeft seit $up Tagen. Der Schwellwert ab wie vielen Tagen eine Warnung erzeugt wird kann mit dem Wert (Anzahl Tage) in reboot_warning angepasst werden."
 
exit $STATE_WARNING

else 

echo "$PROGNAME: STATE_UNKNOWN"

exit $STATE_UNKNOWN

fi
