import sys

class Scraper(object):
    def __init__(self, config, client, array):
        self.config = config
        self.client = client
        self.array = array

    def run(self):
        for line in self.array:
            try:
                self.config["counter"].addCount()
                print("[* "+str(self.config["counter"].getFound())+" WORKING*]["+ str(self.config["counter"].getCount()) +"/"+ str(len(self.config["array"]))\
                        +"] trying "+line+"...")
                
                res = self.client.get(self.config["url"], proxies={ "https": "socks5://"+line ,\
                        "http": "socks5://"+line, "https": "socks4://"+line, "http":\
                        "socks4://"+line, "http": line, "https": line }, timeout=1)
                print(res)

                if (self.config["regex"]).match(res.text):
                    print("[*] " + line + " is a valid proxy! Saving. ")
                    (self.config["counter"]).addFound()
                    (self.config["saver"]).save(line)
            except:
                continue