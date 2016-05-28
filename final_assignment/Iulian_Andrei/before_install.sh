#!/bin/bash

mysource=$1
destination=$2

if [[ -z "$destination" ]]; then
    echo "Before install error: No directory parameter"
    echo "No directory parameter" >> info.log
    exit
fi

if [[ ! -d "$destination" ]]; then
    echo "Before install error: Directory does not exist"
    exit
fi

wget $mysource --output-document=$destination$3

echo "Before install: Download completed to specified directory" >> info.log
