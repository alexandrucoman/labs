#!/bin/bash

# merge doar cu source up.sh nr

function up() {
  undirector=$PWD
  for i in $(seq 1 $1)
  do
    if [[ $(grep -o "/" <<< "$undirector" | wc -l) -gt 1 ]]
    then
        undirector=${undirector%/*}
    else
        undirector='/'
    fi
  done
  cd $undirector
}

up $1
