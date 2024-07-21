import re
import requests

class ProxyChecker:
    UNTAMPERED_PROXY_REGEX = re.compile(r"<HTML><HEAD><TITLE>Success</TITLE></HEAD><BODY>Success</BODY></HTML>$")
    INTERROGATOR_URL = "https://captive.apple.com/"

    def __init__(self, proxy_list, on_proxy_found, on_progress):
        self.proxy_list = proxy_list
        self.on_proxy_found = on_proxy_found
        self.on_progress = on_progress

    def check_proxy(self, line):
        try:
            self.on_progress(line)
            session = requests.Session()

            proxies = {
                "http": f"socks5://{line}",
                "https": f"socks5://{line}",
                "http": f"socks4://{line}",
                "https": f"socks4://{line}",
                "http": line,
                "https": line
            }
            response = session.get(self.INTERROGATOR_URL, proxies=proxies, timeout=8)

            if self.UNTAMPERED_PROXY_REGEX.match(response.text):
                self.on_proxy_found(line)

        except requests.RequestException:
            pass

    def run(self):
        for line in self.proxy_list:
            self.check_proxy(line)