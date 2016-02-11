#!/bin/bash
function work {
    touch "$2"
    string
    while read -r line; do
        ip=$(echo "$line" | cut -d "," -f1)
        mac_l=$(echo "$line" | cut -d "," -f2)
        mac=${mac_l:0:2}:${mac_l:2:2}:${mac_l:4:2}:${mac_l:6:2}
        hostname="$(echo "$line" | cut -d "," -f3)"
        host=$(echo "$line" | cut -d "," -f3)
        stringl="host $hostname {
        option host-name \"$host\";
        hardware ethernet $mac;
        fixed-address $ip;
        }"
        string="$string$stringl\n"
    done < "$1"
    echo -e "$string" > "$2"
}


if [[ "$#" -eq 2 ]]; then
    work "$1" "$2"
fi
