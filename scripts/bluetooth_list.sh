#!/usr/bin/env bash

ADDR=$1
CHANNEL=$2
TARGET_DIR=$3

result=$(obexftp -b $ADDR -B $CHANNEL --chdir $TARGET_DIR -l 2>&1 | grep -E '<folder | <file' | awk -F'"' 'BEGIN {printf "{\n"} {printf "%s\"%s\": %s",t,$2,$4; t=",\n"} END{ printf "\n}\n"}')
echo -e $result
