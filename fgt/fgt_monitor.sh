#! /bin/bash

#################################################
# How to run
# ./fgt_monitor.sh | ssh -t -t admin@172.18.43.67 >tt.log
#
##################################################

# General infos
echo exec time
echo exec date
echo get system status
echo get system performance status
echo diag sys session stat
echo diag hardware sysinfo memory
sleep 1
# Process informations
echo diag sys top 2 10
sleep 2
echo q
echo diag sys top-summary \"-s mem\"
sleep 2
echo q
sleep 2

### WAD
echo diag debug enable
echo diag wad stats summary list
echo diag wad stats crypto list
sleep 1
# WAD 2200 - wanopt
echo diag test app wad 2200
sleep 1
echo diag test app wad 13
sleep 3
echo diag test app wad 803
sleep 2
echo diag test app wad 104
sleep 2
echo diag test app wad 21
sleep 2
echo diag test app wad 25
sleep 2
echo diag test app wad 27
sleep 2
echo diag test app wad 33
sleep 2
echo diag test app wad 70
sleep 2
echo diag test app wad 120
sleep 2
echo diag test app wad 1
sleep 1
echo diag test app wad 2
sleep 1
echo diag test app wad 3
sleep 3
echo diag test app wad 4
sleep 3
 

# WAD 2300 - worker 1
echo diag test app wad 2300
sleep 1
echo diag test app wad 13
sleep 3
echo diag test app wad 803
sleep 2
echo diag test app wad 104
sleep 2
echo diag test app wad 21
sleep 2
echo diag test app wad 25
sleep 2
echo diag test app wad 27
sleep 2
echo diag test app wad 33
sleep 2
echo diag test app wad 70
sleep 2
echo diag test app wad 120
sleep 2
echo diag test app wad 1
sleep 1
echo diag test app wad 2
sleep 1
echo diag test app wad 3
sleep 3
echo diag test app wad 4
sleep 3
# WAD 2301 - worker 2
echo diag test app wad 2301
sleep 1
echo diag test app wad 13
sleep 3
echo diag test app wad 803
sleep 2
echo diag test app wad 104
sleep 2
echo diag test app wad 21
sleep 2
echo diag test app wad 25
sleep 2
echo diag test app wad 27
sleep 2
echo diag test app wad 33
sleep 2
echo diag test app wad 70
sleep 2
echo diag test app wad 120
sleep 2
echo diag test app wad 1
sleep 1
echo diag test app wad 2
sleep 1
echo diag test app wad 3
sleep 3
echo diag test app wad 4
sleep 3
# WAD 2302 - worker 3
echo diag test app wad 2302
sleep 1
echo diag test app wad 13
sleep 3
echo diag test app wad 803
sleep 2
echo diag test app wad 104
sleep 2
echo diag test app wad 21
sleep 2
echo diag test app wad 25
sleep 2
echo diag test app wad 27
sleep 2
echo diag test app wad 33
sleep 2
echo diag test app wad 70
sleep 2
echo diag test app wad 120
sleep 2
echo diag test app wad 1
sleep 1
echo diag test app wad 2
sleep 1
echo diag test app wad 3
sleep 3
echo diag test app wad 4
sleep 3
# Go back to manager context by default
echo diag test app wad 2000
sleep 1
# Authentication daemon checks
echo diag test app fnbamd 1
sleep 1
# Authd daemon check
echo diag debug authd memory
sleep 5
echo diag debug disable
echo exit
