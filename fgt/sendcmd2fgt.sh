#!/usr/bin/env bash
#=======================
#=======================


do_ssh(){
        local array_ssh_args=()
        local input=$1
        local th_id=$2
        local result=
        branch_name=""
        ftp_file=""
        fos_num=""
        list_mode=0
        build_number=""
        image_type="out"
        red='\033[0;31m'
        no_color='\033[0m'
        port=22

        array_ssh_args+=('-oBatchMode=no')
        array_ssh_args+=('-oServerAliveInterval=1')
        array_ssh_args+=('-oServerAliveCountMax=2')
        array_ssh_args+=('-oConnectTimeout=2')
        array_ssh_args+=('-oStrictHostKeyChecking=no')
        array_ssh_args+=('-oLogLevel=ERROR')
        array_ssh_args+=('-oCheckHostIP=no')
        array_ssh_args+=('-oUserKnownHostsFile=/dev/null')
        array_ssh_args+=('-T')

        result=$(echo -e "$input" | ssh "${array_ssh_args[@]}" admin@"$FG_IP"  2>&1)

        echo -e "Input:\n$input\nResult:\n$result\nssh_args:\n${array_ssh_args[@]}"

        echo -e "$result" | sed -n "s/\(.*\)/==$th_id==:\1/p"

}

threadnum=2
FG_IP='172.18.43.38'
c=0
cmdb=0

while  [[ $c != 10000 ]]; do
        i=0
        p=101
        while  [[ $i != 100 ]]; do
                #cmd_to_send="c g\nconfig system interface\nedit v$p \n set vdom root\n set ip 3.3.$i.3 255.255.255.0\nset allowaccess ping\n set interface lag1\n set vlanid $p\nnext\nend\nend"
                #do_ssh "$cmd_to_send" "$i"
             
                cmd_to_send="c v\n edit test$p \nend"
                do_ssh "$cmd_to_send" "$i"
                echo add_vdom

                i=$(($i+1))
                p=$(($p+1))
                echo "$i times add vdom"
                echo "add $p  add vdom"
        done
       i=0
       p=101
       sleep 10
        while  [[ $i != 100 ]]; do
                #cmd_to_send="c v\n edit root\n config vpn ipsec phase2-interface\n delete p2-v$p\nend\nend"
                #do_ssh "$cmd_to_send" "$i"
                #cmd_to_send="c v\nedit  root\nconfig vpn ipsec phase1-interface\ndelete  p1-v$p\nend\nend"
                #do_ssh "$cmd_to_send" "$i"
                cmd_to_send="c v\ndelete test$p\nend\n"
                do_ssh "$cmd_to_send" "$i"
                echo delete vdom
                i=$(($i+1))
                p=$(($p+1))
                echo "$i times del vdom"
                echo "del $p  vdom"
        done


        sleep 10
        c=$(($c+1))
        echo "$c Total times"
        sleep 10
done


