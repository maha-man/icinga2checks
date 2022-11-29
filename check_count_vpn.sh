#!/bin/bash



################################################################################
# Nagios plugin to check how many vpn are in aktiv                      #
# Author: Michael
# Datum 14.06.2021                        #
################################################################################


VERSION="Version 1.0"
AUTHOR="Michael Tschoepe"

PROGNAME="check_count_vpn.sh"

# Exit codes
STATE_OK=0
STATE_WARNING=1
STATE_CRITICAL=2
STATE_UNKNOWN=3



#Main #########################################################################


# Die Parameter werden übergeben


while [ "$1" ] 


do


case "$1" in


-w) 

warni=$2

# die zwei linken kommandozeilen Optionen wegschmeißen

shift 2

;;


-c)

# die zwei linken kommandozeilen Optionen wegschmeißen

criti=$2

shift 2

;;


-H)

ip=$2

shift 2

;;


esac


done



# Aktive VPNs werden ausgelesen und an Icinga übergeben


# replace IP an Object Identifier

vpns=$(snmpwalk -v2c -c public IP Object Identifier |awk '{print $4}')


if [  $vpns -ge $criti ]

then

echo  "$PROGNAME: CRITICAL - Es sind $vpns VPNS aktiv. Der Schwellwert fuer kritisch betraegt: $criti.|'DialUp-VPN'=$vpns"


exit $STATE_CRITICAL


elif [  $vpns -ge $warni ]

then

echo  "$PROGNAME: WARNING - Es sind $vpns VPNS aktiv. Der Schwellwert fuer eine Warnung betraegt: $warni.|'DialUp-VPN'=$vpns"

exit $STATE_WARNING


else

echo "$PROGNAME: OK - Es sind $vpns VPNS aktiv.|'DialUp-VPN'=$vpns"

exit $STATE_OK


fi

