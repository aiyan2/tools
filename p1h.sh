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

# while in one line

while true; do { echo -e 'HTTP/1.1 200 OK\r\n'} | nc -l 8909; done;
while true; do curl -x 172.18.43.64:8080 172.18.43.100;sleep 2; done
while true; do curl -x 172.18.43.64:8080 172.18.43.100 172.18.43.100/eicar.com.1  172.18.43.100/test/badips   172.18.43.100/test/m4 -o tmp2; done
# create files
cmd:
python: 
