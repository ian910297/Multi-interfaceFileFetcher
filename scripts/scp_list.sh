#!/usr/bin/env bash

ADDR=$1
TARGET_DIR=$2

AWK_CMD='BEGIN { printf "{\n" } { printf "%s\"%s\": %s", t, $9, $5; t=",\n" } END { printf "\n}\n"}'

ssh pi@$ADDR "/bin/ls -l $TARGET_DIR | grep -E 'd|-' | awk '$AWK_CMD'"

