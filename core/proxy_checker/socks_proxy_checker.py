import requests

from core.proxy_checker.proxy_checker import ProxyChecker

class SocksProxyChecker(ProxyChecker):
    def check(self, proxy_url):
        try:
            self.on_check(proxy_url)
            session = requests.Session()

            if "://" in proxy_url:
                proxy = proxy_url.split("://")[1]
            else:
                proxy = proxy_url
            
            proxies = [
                {
                    "version": "socks5",
                    "http": f"socks5://{proxy}",
                    "https": f"socks5://{proxy}"
                },
                {
                    "version": "socks4",
                    "http": f"socks4://{proxy}",
                    "https": f"socks4://{proxy}"
                },
                {
                    "version": "https",
                    "http": proxy,
                    "https": proxy
                }
            ]

            response = None
            current_version = None

            for proxy_dict in proxies:
                try:
                    current_version = proxy_dict["version"]
                    response = session.get(self.INTERROGATOR_URL, proxies=proxy_dict, timeout=8)
                    break
                except Exception as e:
                    continue

       
            if response is not None and self.is_response_not_tampered(response):
                self.on_proxy_found(current_version + "://" + proxy)

        except requests.RequestException:
            pass

        except Exception as e:
            print(e)