# check_proxy.py
A fast Cyber Threat Intelligence tool for creating a list of working proxies. Use it to obtain, validate, and check proxy origins. Easily create IoC proxy lists. Supports vmess, HTTPS, and SOCKS.

```
       _               _                                                
      | |             | |                                               
   ___| |__   ___  ___| | __    _ __  _ __ _____  ___   _   _ __  _   _ 
  / __| '_ \ / _ \/ __| |/ /   | '_ \| '__/ _ \ \/ / | | | | '_ \| | | |
 | (__| | | |  __/ (__|   <    | |_) | | | (_) >  <| |_| |_| |_) | |_| |
  \___|_| |_|\___|\___|_|\_\   | .__/|_|  \___/_/\_\\__, (_) .__/ \__, |
                         ______| |                   __/ | | |     __/ |
                        |______|_|                  |___/  |_|    |___/ 

                                                       Krystian Bajno 2018
Contributors:                                                      v2 2024
@Artideusz (https://github.com/Artideusz)
   
usage: run_check_proxy.py [-h] [--socks-only] input_file output_file [num_threads]
run_check_proxy.py: error: the following arguments are required: input_file, output_file
```

<img src="https://raw.githubusercontent.com/krystianbajno/krystianbajno/main/img/check-proxy/check-proxy.gif"/>

### Validate proxies in seconds.
The `check_proxy.py` script supports the following proxy formats in the input file:

```
vmess://base64-encoded-config
socks4://ip:port
socks5://ip:port
http://ip:port
https://ip:port
ip:port
```

# Usage:

### To obtain proxies, run the following command in your terminal:
This command retrieves proxies from the providers listed in the `proxy-providers.txt` file.
```
bash get_proxy.sh
```

### To validate the proxies, use the following command:
```
python run_check_proxy.py <input-file> <output-file> <number-of-threads>
```

### The script generates several reports:
- `output-file`: A plain text file containing the proxies connection strings.
- `output-file_details`: - An extended report with information on proxy geo-location, integrity, IP, and port.
- `output-file_details.csv`: A CSV report with detailed information, useful for banning IP ranges or reporting threats to the Blue Team.

# Installation:
Install the required packages using:

```
pip install -r requirements.txt
```
