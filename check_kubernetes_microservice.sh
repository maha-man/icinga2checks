#!/bin/bash


################################################################################                        #
# Author: Michael 
# Datum 18.02.2022                        #
################################################################################

PROGNAME="check_kubernetes_microservice.sh"


# Replace kube_service wiht the Kubernetes Microservices 



# Exit codes
STATE_OK=0
STATE_WARNING=1
STATE_CRITICAL=2
STATE_UNKNOWN=3


#Main #########################################################################



showPod=$(kubectl --kubeconfig=/usr/lib/nagios/plugins/kube_config get pods --all-namespaces |grep kube_service|awk '{print $2, $3, $4, $6}')



pod=$(kubectl --kubeconfig=/usr/lib/nagios/plugins/kube_config get pods --all-namespaces |grep kube_service |awk '{print $4}')



if [ "$pod" = "Running" ]


then 

pod=$(kubectl --kubeconfig=/usr/lib/nagios/plugins/kube_config get pods --all-namespaces |grep kube_service|awk '{print $3}')


if [ $pod = "1/1" ] || [ $pod = "2/2" ] || [ $pod = "3/3" ] || [ $pod = "4/4" ]  || [ $pod = "5/5" ] || [ $pod = "6/6" ]  || [ $pod = "6/6" ] 

then


echo "$PROGNAME: OK - Im Kubernetescluster ist die kube_service im Status Running und Ready:"

echo $showPod


exit $STATE_OK


else

echo "$PROGNAME: CRITICAL - Im Kubernetescluster ist die kube_service nicht im Status Running und Ready:"

echo $showPod



exit $STATE_CRITICAL


fi


fi

