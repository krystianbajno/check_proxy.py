import requests

from core.proxy_checker.proxy_checker import ProxyChecker

class SocksProxyChecker(ProxyChecker):
    def check(self, proxy):
        try:
            self.on_check(proxy)
            session = requests.Session()

            proxies = {
                "http": f"socks5://{proxy}",
                "https": f"socks5://{proxy}",
                "http": f"socks4://{proxy}",
                "https": f"socks4://{proxy}",
                "http": proxy,
                "https": proxy
            }

            response = session.get(self.INTERROGATOR_URL, proxies=proxies, timeout=8)

            if self.is_response_not_tampered(response):
                self.on_proxy_found(proxy)

        except requests.RequestException:
            pass