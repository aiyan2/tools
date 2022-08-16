#!/bin/bash
FGT=172.18.43.67
pc100=172.18.43.100

sleep=1
counter=10000

# curl -x fgt34.devqa.lab:8080 --proxy-nego -u: pc100

runcases(){

tc=./mlog-proxy/mmlog-$1

echo 'on pc100 with http1.1'
time  python3 enghttp.py --uri https://$pc100  --username u1 --password 12345678 --data-tuples pc100tuple.txt  --proxy $FGT:8080 >
$tc-d1.1-$pc100

sleep $sleep
echo 'on pc100 with http2'
time   python3 enghttp.py --uri https://172.18.43.100:8448 --version 2  --username u1 --password 12345678 --data-tuples pc100tuple
.txt  --proxy $FGT:8080 > $tc-d2-$pc100

sleep $sleep
echo 'on cnn.com with http1.1'
#time python3 enghttp.py --uri https://www.cnn.com   --username u1 --password 12345678 --data-tuples pc100tuple.txt  --proxy $FGT:
8080 > $tc-d1.1-cnn


sleep $sleep
echo 'on cnn.com with http2'
#time python3 enghttp.py --uri https://www.cnn.com --version 2  --username u1 --password 12345678 --data-tuples pc100tuple.txt  --
proxy $FGT:8080 > $tc-d2-cnn


}

#while true
#do


## monitor memory
{ echo "";  echo " diag hardware sysinfo memory | grep Mem"; sleep 0.1; echo " exit"; } | ssh -tt admin@$FGT

echo " set to h2 deep-inspection"
{ echo "config firewall proxy-policy";  echo " edit 1"; sleep 0.1; echo " set ssl-ssh-profile h2-deep "; "  ";   sleep 0.1; echo "
 end";echo " exit"; } | ssh -tt admin@$FGT
runcases h2-deep



echo " set to cert_inspection, h2-cert with port 8448"
{ echo "config firewall proxy-policy";  echo " edit 1"; sleep 0.1; echo " set ssl-ssh-profile h2-cert ";  sleep 0.1; echo " end";e
cho " exit"; } | ssh -tt admin@$FGT
runcases h2-cert

echo " set to cert_inspection,  default cic "
{ echo "config firewall proxy-policy";  echo " edit 1"; sleep 0.1; echo " set ssl-ssh-profile certificate-inspection ";  sleep 0.1
; echo " end";echo " exit"; } | ssh -tt admin@$FGT
runcases default-cic


echo " set to cert_inspection,  default dpi "
{ echo "config firewall proxy-policy";  echo " edit 1"; sleep 0.1; echo " set ssl-ssh-profile deep-inspection ";  sleep 0.1; echo
" end";echo " exit"; } | ssh -tt admin@$FGT
runcases default-dpi


echo " set to inspect_all"
{ echo "config firewall proxy-policy";  echo " edit 1"; sleep 0.1; echo " set ssl-ssh-profile inspect_all ";  sleep 0.1; echo " en
d";echo " exit"; } | ssh -tt admin@$FGT

runcases inspect_all


echo " set to inspect_all_cic"
{ echo "config firewall proxy-policy";  echo " edit 1"; sleep 0.1; echo " set ssl-ssh-profile inspect_all_cic ";  sleep 0.1; echo
" end";echo " exit"; } | ssh -tt admin@$FGT

runcases inspect_all_cic
