#!/usr/bin/env bash

IP_ADDR=$1      # pi7, 192.168.0.2
CREATE_DIR=$2   # ~/model_root
ADDR=$3         # pi7, 192.168.0.2
DOWNLOAD_DIR=$4 # model_root
TEST_SIZE=$5    # 16384

testfile="target"
cnt=1

echo -en "[\n"
while true;
do
    ssh pi@$IP_ADDR "cd $CREATE_DIR; ~/testSH/createfile $testfile $cnt 2>&1 > /dev/null" 2>&1 > /dev/null

    in_loop_cnt=0
    while true;
    do
        scp_time=$( (time scp pi@pi7:~/$DOWNLOAD_DIR/$testfile ./) 2>&1 | grep real | awk -F'm' '{ print $2 }' | awk -F's' '{print $1}' )
        echo -en "[ $cnt, $scp_time ]"

        (( in_loop_cnt += 1 ))

        if [ $in_loop_cnt -eq 30 ];
        then
            break
        fi
        echo -en ",\n"
    done

    (( cnt *= 4 ))
    if [ $cnt -gt $TEST_SIZE ];
    then
        break
    fi
    echo -en ",\n"
done

ssh pi@$IP_ADDR "cd $CREATE_DIR; rm -f $testfile > /dev/null" 2>&1 > /dev/null
rm -f $testfile

echo -en "\n]\n"
