import requests

from core.entities.proxy import Proxy
from core.proxy_checker.proxy_checker import ProxyChecker

class SocksProxyChecker(ProxyChecker):
    def check(self, proxy: Proxy):
        try:
            self.on_check(proxy)
            session = requests.Session()
            
            proxy_url = proxy.connection_string

            if "://" in proxy_url:
                proxy_url = proxy_url.split("://")[1]
            
            proxies = [
                {
                    "version": "socks5",
                    "http": f"socks5://{proxy_url}",
                    "https": f"socks5://{proxy_url}"
                },
                {
                    "version": "socks4",
                    "http": f"socks4://{proxy_url}",
                    "https": f"socks4://{proxy_url}"
                },
                {
                    "version": "https",
                    "http": proxy_url,
                    "https": proxy_url
                }
            ]

            response = None
            current_version = None

            for proxy_dict in proxies:
                try:
                    current_version = proxy_dict["version"]
                    response = session.get(self.INTERROGATOR_URL, proxies=proxy_dict, timeout=8)
                    break
                except requests.RequestException as e:
                    continue

            if response is not None:
                if self.is_response_not_tampered(response):
                    proxy.set_is_safe(True)
                    
                proxy.set_connection_string(current_version + "://" + proxy_url)
                self.on_proxy_found(proxy)

        except requests.RequestException:
            pass