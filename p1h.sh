#!/bin/bash
counter=0

while true
do
date

counter=$((counter+1))
curl 172.18.43.100/eicar.com.1 -H "Counter: $counter"
curl https://172.18.43.100/eicar.com.1 -H "Counter: $counter" -k 
echo $counter

sleep 1 
done

