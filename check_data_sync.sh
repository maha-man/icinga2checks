#!/bin/bash

################################################################################
# Nagios plugin to monitor check_data_sync                         #
# Author: Michael
# Datum 28.09.2020                        #
################################################################################


#data from a file cluster is mounted and synchronized. If this is successfully completed, a file is created. This check checks whether such a file was created in the last 4 hours and then outputs the corresponding status.


PROGNAME="check_data_sync.sh"


# Exit codes
STATE_OK=0
STATE_WARNING=1
STATE_CRITICAL=2
STATE_UNKNOWN=3

#Main #########################################################################


finde=$(sudo find /root/script/ici_rsync_check/*.txt -mmin -240 2>/dev/null)


if [[ -z $finde ]]; then
   echo "$PROGNAME: NO ceph data synchronization "
   exit $STATE_CRITICAL

elif [[ ! -z $finde ]]; then
   echo "$PROGNAME: ceph data synchronization OK"
   exit $STATE_OK

else
   echo "$PROGNAME: UNKNOWN"
   exit $STATE_UNKNOWN

fi
