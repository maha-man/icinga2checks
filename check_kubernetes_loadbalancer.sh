#!/bin/bash


################################################################################
# Nagios plugin to check Kubernetes loadbalancer                        #
# Author: Michael Tschoepe
# Datum 30.12.2020                        #
################################################################################

VERSION="Version 1.0"
AUTHOR="Michael Tschoepe"

PROGNAME="check_kubernetes_loadbalancer.sh"


# Exit codes
STATE_OK=0
STATE_WARNING=1
STATE_CRITICAL=2
STATE_UNKNOWN=3


#Main #########################################################################



lbPods=$(kubectl --kubeconfig=/usr/lib/nagios/plugins/kube_config get pods -n metallb-system)

lbCount=0


for lba in $(kubectl --kubeconfig=/usr/lib/nagios/plugins/kube_config get pods -n metallb-system |grep -i "Running" |awk '{print $3}')

do


if [ "$lba" = "Running" ]

then 

 (( lbCount++  ))

fi


done



if [ "$lbCount" -eq  4 ]


then

echo "$PROGNAME: OK - Im Kubernetescluster sind alle Loadbalancer Pods im Status Running."

echo

echo "$lbPods"

exit $STATE_OK


else

echo "$PROGNAME: Im Kubernetescluster sind nicht alle Pods vom Loadbalancer im Status Running."

echo

echo "$lbPods"

exit $STATE_CRITICAL


fi
