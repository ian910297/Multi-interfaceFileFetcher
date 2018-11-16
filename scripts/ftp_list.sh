#!/usr/bin/env bash

ADDR=$1
TARGET_DIR=$2

ftp -n $ADDR << EOF | awk 'BEGIN { printf "[\n" } { printf "%s[\"%s\",%s]", t, $9, $5; t=",\n" } END { printf "\n]\n"}'
user anonymous passwd
cd $TARGET_DIR
ls
quit
EOF
