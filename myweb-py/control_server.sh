#!/bin/bash

# sed -i -e 's/\r$//' realbrowser.sh

sudo python3 /home/johns/https/myhttps/myweb443.py &

MINWAIT=10
MAXWAIT=60
sleep $((MINWAIT+RANDOM % (MAXWAIT-MINWAIT)))
pid = $!

echo " myweb443 runing " $pid

sudo pkill -9 myweb443
