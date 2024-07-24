import requests

from core.proxy_checker.proxy_checker import ProxyChecker

class VmessProxyChecker(ProxyChecker):
    def check(self, proxy):
        try:
            self.on_check(proxy)
            session = requests.Session()
            
            # Connect to VPN here
            

            response = session.get(self.INTERROGATOR_URL, timeout=8)

            if self.is_response_not_tampered(response):
                self.on_proxy_found(proxy)

        except requests.RequestException as e:
            print(f"Error: {e}")
            pass