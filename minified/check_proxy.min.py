#!/usr/bin/python
### 
# Copyright 2018 Krystian Bajno
#Usage: check_proxy.py <proxy-list> <output-list> <number-of-threads>

import re
import requests
import threading
import sys
from time import sleep
banner = "\nPython3\n\
       _               _                                                \n\
      | |             | |                                               \n\
   ___| |__   ___  ___| | __    _ __  _ __ _____  ___   _   _ __  _   _ \n\
  / __| '_ \\ / _ \\/ __| |/ /   | '_ \\| '__/ _ \\ \\/ / | | | | '_ \\| | | |\n\
 | (__| | | |  __/ (__|   <    | |_) | | | (_) >  <| |_| |_| |_) | |_| |\n\
  \\___|_| |_|\\___|\\___|_|\\_\\   | .__/|_|  \\___/_/\\_\\\\__, (_) .__/ \\__, |\n\
                         ______| |                   __/ | | |     __/ |\n\
                        |______|_|                  |___/  |_|    |___/ \n\n\
                                                    By Krystian Bajno   \n\n\
"
def printHelp():
    print("Usage: check_proxy.py <proxy-list> <output-list> <number-of-threads>")
    sys.exit(1)
class Counter():
    def __init__(self):
        self.counter = 0
        self.found = 0
        self.array = self.readArray()
    def addCounter(self):
        self.counter = self.counter+1
    def addFound(self):
        self.found = self.found+1
    def readArray(self):
        with open(sys.argv[1], "r") as ins:
            array = []
            for line in ins:
                array.append(line.rstrip('\n').lstrip().rstrip())
            ins.close()
        return array
    def writeProxy(self, line):
        with open(sys.argv[2], "a") as valid:
                valid.write(line+ "\n")
        valid.close()
    def checkProxy(self, numarray, b):
        for line in numarray:
            try:
                session = requests.Session()
                self.addCounter()
                print("[* "+str(self.found)+" WORKING*]["+ str(self.counter) +"/"+ 
str(len(self.array))\
                        +"] trying "+line+"...")
                a = session.get("https://captive.apple.com/", proxies={ "https": "socks5://"+line ,\
                        "http": "socks5://"+line, "https": "socks4://"+line, "http":\
                        "socks4://"+line, "http": line, "https": line }, timeout=8)
                print(a)
                if b.match(a.text):
                    print("[*] " + line+" is a valid proxy! Saving. ")
                    self.addFound()
                    self.writeProxy(line)
            except:
                continue
def partition ( lst, n ):
         return [ lst[i::n] for i in range(n) ]
def main():
    if len(sys.argv) < 4 or sys.argv[1] == sys.argv[2]:
        printHelp()
    numberOfThreads = int(sys.argv[3])
    regex = re.compile(r'<HTML><HEAD><TITLE>Success</TITLE></HEAD><BODY>Success</BODY></HTML>$')
    counter = Counter()
    divided_arr = partition(counter.array, numberOfThreads)
    print("[*] "+ str(len(counter.array))+" proxies divided into "\
            +str(numberOfThreads)+" threads and sublists " \
        + "(approx. "+str(len(divided_arr[0]))+" each)")
    print("[*] Input file: "+sys.argv[1]+"\n[*] Output file: "+ sys.argv[2])
    input("[*] Press enter to start!")
    def checkProxy(n, r):
            counter.checkProxy(divided_arr[n], r)
    for n in range(0, numberOfThreads):
        thread = threading.Thread(target = checkProxy, args=(n, regex))
        thread.daemon = True
        thread.start()
    try:
        while(1):
            sleep(1)
    except KeyboardInterrupt:
        print("[*] Stopping")
        sys.exit(0)
if __name__ == "__main__":
    print(banner)
    main()
