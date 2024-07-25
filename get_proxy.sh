while read -r line; do wget $line -O ->> proxies ; done < proxy-providers.txt
