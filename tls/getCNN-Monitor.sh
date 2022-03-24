#!/bin/bash
HOST=www.cnn.com
PORTNUMBER=443
SERVERNAME=www.cnn.com

counter=10000

rnd=$1
counter=$rnd$counter


while true
do
  echo " curent date is::: " `date`
  echo -n | openssl s_client -connect $HOST:$PORTNUMBER -serverna
me $SERVERNAME \
     | openssl x509 > /tmp/usa/$SERVERNAME-$counter.cert
  counter=$((counter+1))

  sleep 20
done
