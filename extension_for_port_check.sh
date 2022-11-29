#/bin/bash

ss -tulpn |grep '*:\|\0.0.0.0:' |grep -v '127.0.0\|0.0.0.0:111' | awk '{ print $1, $2, $5, $7 }' | sed 's/*://' | sed 's/0.0.0.0://' | sed 's/users:(("//' | sed 's/".*//'
