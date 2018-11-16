#!/usr/bin/env bash

ADDR=$1
FILENAME=$2
DEST=$3

cd $DEST
scp pi@$ADDR:$2 ./
