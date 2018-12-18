#!/usr/bin/python
### 
# Copyright 2018 Krystian Bajno
#Usage: check_proxy.py <proxy-list> <output-list> <number-of-threads>

import re
import sys
from requests import Session as client

from libs.Misc.Banner import Banner
from libs.Misc.HelpUtils import *
from libs.Factories.ThreadFactory import ThreadFactory
from libs.Files.Reader import Reader
from libs.Files.Saver import Saver
from libs.Proxy.Scraper import Scraper
from libs.Misc.Counter import Counter

from time import sleep
from env import Env


def main():
    Banner().print()
    if len(sys.argv) < 3 or sys.argv[1] == sys.argv[2]:
        printHelp()
        sys.exit(1)
    
    env = Env().getAll()


    config = {
     "url": env["url"],
     "array": (Reader(open(sys.argv[1], 'r'))).read(),
     "counter": Counter(),
     "saver": Saver(open(sys.argv[2], 'a')),
     "regex": re.compile(env["regex"]),
     "timeout": env["timeout"],
     }

    if(len(config["array"]) < env["number_of_threads"]):
        env["number_of_threads"] = len(config["array"])
     
    divided_arr = partition(config["array"], env["number_of_threads"])


    print("[*] "+ str(len(config["array"]))+" proxies divided into "\
        +str( env["number_of_threads"])+" threads and sublists " \
    + "(approx. "+str(len(divided_arr[0]))+" each)")

    print("[*] Input file: "+sys.argv[1]+"\n[*] Output file: "+ sys.argv[2])
    input("[*] Press enter to start!")

    for i in range(env["number_of_threads"]):
        thread = ThreadFactory(Scraper(config, client(), divided_arr[i]), 1)
        thread.run()

    try:
        while(1):
            sleep(1)

    except KeyboardInterrupt:
        print("[*] Stopping")
        sys.exit(0)

if __name__ == "__main__":
    main()
