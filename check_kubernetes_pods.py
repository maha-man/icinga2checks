#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Michael
25.07.2022
"""



import os

program = "check_kubernetes_pods.py"

STATE_OK = 0
STATE_WARNING = 1
STATE_CRITICAL = 2
STATE_UNKNOWN = 3


#pods = os.popen('kubectl --kubeconfig=/usr/lib/nagios/plugins/kube_config get pods --all-namespaces').read()

pods = os.popen("kubectl --kubeconfig=/usr/lib/nagios/plugins/kube_config get pods --all-namespaces -o wide  |awk -v OFS='\t' '{print $1, $2, $3, $4, $5, $6, $8, $10}' | sed 's/<none>//g'").read()


pod2 = os.popen("kubectl --kubeconfig=/usr/lib/nagios/plugins/kube_config get pods --all-namespaces |grep -v STATUS |awk '{print $3}'").read()

pod3 = os.popen("kubectl --kubeconfig=/usr/lib/nagios/plugins/kube_config get pods --all-namespaces |grep -v STATUS |awk '{print $4}'").read()

pod4 = os.popen("kubectl --kubeconfig=/usr/lib/nagios/plugins/kube_config get pods --all-namespaces -o wide |grep -v '6/6\|5/5\|4/4\|3/3\|2/2\|1/1' |awk -v OFS='\t' '{print $1, $2, $3, $4, $5, $6, $8, $10}' | sed 's/<none>//g'").read()

pod3 = pod3.split()


pod2 = pod2.split()



#print(pod3)

#print(type(pod3))

count = 0

for podState in pod3:
    

    if "Running" in podState:

       #print(podState)
       pass

    else:
        print(program, " - STATE_CRITICAL - Im Kubernetescluster sind nicht alle Pods oder kein Pod im Status Running.")
        print(pod4)
        exit(STATE_CRITICAL)


for podState in pod2:
    
    if podState == "6/6" or podState == "5/5" or podState == "4/4" or podState == "3/3" or podState == "2/2" or podState == "1/1":
        count += 1

    else:
        print(program, " - STATE_CRITICAL - Im Kubernetescluster sind nicht alle Pods oder kein Pod im Status Ready.")
        print(pod4)
        exit(STATE_CRITICAL)
   

print(program + " - STATE_OK - Im Kubernetescluster sind alle Pods im Status Running und Ready. Die Anzahl der Pods betraegt " + str(count)  + ".")
print(pods)
exit(STATE_OK)
