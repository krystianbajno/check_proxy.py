import re
import requests

class VmessProxyChecker:
    UNTAMPERED_PROXY_REGEX = re.compile(r"<HTML><HEAD><TITLE>Success</TITLE></HEAD><BODY>Success</BODY></HTML>$")
    INTERROGATOR_URL = "https://captive.apple.com/"

    def __init__(self, on_proxy_found, on_check):
        self.on_proxy_found = on_proxy_found
        self.on_check = on_check

    def check(self, proxy):
        try:
            self.on_check(proxy)
            session = requests.Session()
            
            # Connect to VPN here

            response = session.get(self.INTERROGATOR_URL, timeout=8)

            if self.UNTAMPERED_PROXY_REGEX.match(response.text):
                self.on_proxy_found(proxy)

        except requests.RequestException:
            pass