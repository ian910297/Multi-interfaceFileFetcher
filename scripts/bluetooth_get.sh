#!/usr/bin/env bash

ADDR=$1
CHANNAL=$2
FILENAME=$3
DEST=$4

cd $DEST
obexftp -b $ADDR -B $CHANNAL --get $FILENAME
