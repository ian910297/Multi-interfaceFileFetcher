#!/usr/bin/env bash

ADDR=$1
TARGET_DIR=$2
FILENAME=$3
DEST=$4

cd $DEST
download_time=$( (time scp pi@$ADDR:~/$TARGET_DIR/$FILENAME ./) 2>&1 | grep real | awk -F'm' '{ print $2 }' | awk -F's' '{print $1}' );
filesize=$( ls -l  $FILENAME | awk '{ print $5 }' )
echo "{ \"$FILENAME\": [$filesize, $download_time] }"
