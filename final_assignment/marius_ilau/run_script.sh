#!/bin/bash
attempts=0
while attempts<4
do
	attempts = attempts + 1
	bash -c 'cd /home/alex/ && exec /home/alex/script.sh'
	sleep 3
done