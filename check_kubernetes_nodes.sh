#!/bin/bash

# test kube
################################################################################
# Nagios plugin to check Kubernetesnodes                        #
# Author: Michael
# Datum 30.12.2020                        #
################################################################################

# Replace number of nodes

PROGNAME="kubernetes_nodes.sh"


# Exit codes
STATE_OK=0
STATE_WARNING=1
STATE_CRITICAL=2
STATE_UNKNOWN=3


#Main #########################################################################



shownode=$(kubectl --kubeconfig=/usr/lib/nagios/plugins/kube_config get nodes |grep -i "Ready" |awk '{print $1, $2}')

shownodeNotReady=$(kubectl --kubeconfig=/usr/lib/nagios/plugins/kube_config get nodes |grep -i -v 'Ready[[:blank:]]' |grep -i -v 'Name' |awk '{print $1, $2}')

ncount=0

for node in $(kubectl --kubeconfig=/usr/lib/nagios/plugins/kube_config get nodes |grep -i "Ready" |awk '{print $2}')

do

if [ "$node" = "Ready" ]

then 

 (( ncount++  ))

fi

done




if [ "$ncount" -eq  5 ]


then

echo "$PROGNAME: OK - Im Kubernetescluster sind alle 4 Nodes und der Master im Status Ready:"

echo

echo "$shownode"

exit $STATE_OK


else

echo "$PROGNAME: Im Kubernetescluster sind keine oder nicht alle Nodes verfuegbar. Diese Nodes bzw. der Master sind nicht ready:"

echo

echo "$shownodeNotReady"

exit $STATE_CRITICAL

fi
