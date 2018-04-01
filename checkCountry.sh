#!/bin/bash
# Usage: ./checkCountry.sh <proxylist> optional: <searched country name>

if [[ "$#" -lt 1 ]] || [[ "$#" -gt 2 ]];then
echo "Usage: ./checkCountry.sh <proxylist> optional: <searched country name>"
else
which geoiplookup
geoip=$?
filename="$1"
while read -r line
do	
   host=$(echo $line | cut -d ":" -f 1 )
   port=$(echo $line | cut -d ":" -f 2 )
    if [[ $geoip == 0 ]]; then
    	geoiplookup  $host | grep -i "$2" -A 3 -B 1 && echo -e "$host\n";
    else
    	whois $host | grep -i "$2" && echo -e "$host\n";
    fi
done < "$filename"
fi
