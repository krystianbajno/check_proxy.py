#!/usr/bin/python
 
# Copyright 2018 Krystian Bajno
# v2 2024
# Usage: check_proxy.py <proxy-list> <output-list> <number-of-threads>

import re
import requests
import threading
import sys
import argparse

from time import sleep

# Reset
Color_Off='\033[0m'       # Text Reset

# Regular Colors
Green='\033[0;32m'        # Green
Yellow='\033[0;33m'       # Yellow
Cyan='\033[0;36m'         # Cyan

banner = f"""{Green}
       _               _                                                
      | |             | |                                               
   ___| |__   ___  ___| | __    _ __  _ __ _____  ___   _   _ __  _   _ 
  / __| '_ \\ / _ \\/ __| |/ /   | '_ \\| '__/ _ \\ \\/ / | | | | '_ \\| | | |
 | (__| | | |  __/ (__|   <    | |_) | | | (_) >  <| |_| |_| |_) | |_| |
  \\___|_| |_|\\___|\\___|_|\\_\\   | .__/|_|  \\___/_/\\_\\\\__, (_) .__/ \\__, |
                         ______| |                   __/ | | |     __/ |
                        |______|_|                  |___/  |_|    |___/ 
{Color_Off}
                                                       Krystian Bajno 2018
                                                                   {Cyan}v2 2024{Color_Off}
"""

UNTAMPERED_PROXY_REGEX = r"<HTML><HEAD><TITLE>Success</TITLE></HEAD><BODY>Success</BODY></HTML>$"
INTERROGATOR_URL = "https://captive.apple.com/"

def print_help():
    print("Usage: check_proxy.py <proxy-list> <output-list> <number-of-threads>")
    sys.exit(1)

def read_proxies(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file]

def write_proxy(file_path, line):
    with open(file_path, "a") as file:
        file.write(line + "\n")

class Counter:
    def __init__(self):
        self.working = 0
        self.progress = 0
        self.total = 0
        
    def add_working(self):
        self.working = self.working + 1
        
    def add_progress(self):
        self.progress = self.progress + 1
        
    def set_total(self, total):
        self.total = total
    
    def get_progress(self):
        return self.progress
    
    def get_total(self):
        return self.total
    
    def get_working(self):
        return self.working
         

def check_proxies(proxy_list, regex, output_file, counter):
    for line in proxy_list:
        try:
            counter.add_progress()

            session = requests.Session()
            print(f"{Green}{counter.get_working()} WORKING{Color_Off} - {counter.get_progress()}/{counter.get_total()} - trying {Cyan}{line}{Color_Off}")
            
            proxies = { 
                "http": f"socks5://{line}", 
                "https": f"socks5://{line}",
                "http": f"socks4://{line}",
                "https": f"socks4://{line}",
                "http": line,
                "https": line
            }
            response = session.get(INTERROGATOR_URL, proxies=proxies, timeout=8)
            
            if regex.match(response.text):
                print(f"[{Green}+{Color_Off}] {Yellow}{line}{Color_Off} is a {Green}valid{Color_Off} proxy! Saving.")
                counter.add_working()
                write_proxy(output_file, line)
        except requests.RequestException:
            continue

def partition(lst, n):
    return [lst[i::n] for i in range(n)]

def main():
    parser = argparse.ArgumentParser(description='Check proxies from a list.')
    parser.add_argument('proxy_list', help='Path to the proxy list file')
    parser.add_argument('output_list', help='Path to the output file')
    parser.add_argument('num_threads', type=int, help='Number of threads')

    args = parser.parse_args()

    if args.proxy_list == args.output_list:
        print("Input and output files must be different.")
        sys.exit(1)

    proxies = read_proxies(args.proxy_list)
    divided_proxies = partition(proxies, args.num_threads)

    print(f"[*] {len(proxies)} proxies divided into {args.num_threads} threads and sublists (approx. {len(divided_proxies[0])} each)")
    print(f"Input file: {args.proxy_list}")
    print(f"Output file: {args.output_list}")
    input(f"[*] Press enter to start!\n")
    
    counter = Counter()
    counter.set_total(len(proxies))

    regex = re.compile(UNTAMPERED_PROXY_REGEX)

    threads = []
    for n in range(args.num_threads):
        thread = threading.Thread(target=check_proxies, args=(divided_proxies[n], regex, args.output_list, counter))
        thread.daemon = True
        threads.append(thread)
        thread.start()

    try:
        while any(thread.is_alive() for thread in threads):
            sleep(1)
    except KeyboardInterrupt:
        print("[*] Stopping")
        sys.exit(0)

if __name__ == "__main__":
    print(banner)
    main()
