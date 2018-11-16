#!/usr/bin/env bash

ADDR=$1
FILENAME=$2
DEST=$3

cd $DEST
wget ftp://anonymous:@pi7/$FILENAME
