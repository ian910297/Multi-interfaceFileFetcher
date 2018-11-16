#!/usr/bin/env bash

ADDR=$1
CHANNAL=$2
TARGET_DIR=$3

obexftp -b $ADDR -B $CHANNAL --chdir $TARGET_DIR -l 2>&1 | grep -E '<folder | <file' | awk -F'"' 'BEGIN {printf "[\n"} {printf "%s[\"%s\",%s]",t,$2,$4; t=",\n"} END{ printf "\n]\n"}'
