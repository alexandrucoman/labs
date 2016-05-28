#!/bin/bash

contor=1

while IFS='' read -r line || [[ -n "$line" ]]; do
    #echo "Text read from file: $line"
    IFS=',' read -a myarray <<< "$line"
    #echo "IP: ${myarray[0]}" 
    fisier="$2$contor"
    > "$fisier"
    printf "host %s {\n" "${myarray[2]}" >> $fisier
    printf "option host-name \"%s\";\n" "${myarray[2]}" >> $fisier
    printf "hardware ethernet %s;\n" "`echo ${myarray[1]:0:2}:${myarray[1]:2:2}:${myarray[1]:4:2}:${myarray[1]:6:2}:${myarray[1]:8:2}:${myarray[1]:10:2} | tr '[:lower:]' '[:upper:]'`" >> $fisier
    printf "fixed-address %s;\n" "${myarray[0]}" >> $fisier
    printf "}\n" >> $fisier
    contor=$((contor+1))
done < "$1"


