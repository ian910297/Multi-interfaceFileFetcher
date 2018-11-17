#!/usr/bin/env bash

ADDR=$1
CHANNAL=$2
TARGET_DIR=$3
FILENAME=$4
DEST=$5

cd $DEST
download_time=$( (time obexftp -b $ADDR -B $CHANNAL --chdir $TARGET_DIR --get $FILENAME) 2>&1 | grep real | awk -F'm' '{ print $2 }' | awk -F's' '{print $1}' );
filesize=$( ls -l  $FILENAME | awk '{ print $5 }' )
echo "{ \"$FILENAME\": [$filesize, $download_time] }"
