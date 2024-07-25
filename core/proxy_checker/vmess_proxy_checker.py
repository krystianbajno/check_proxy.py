import requests
import subprocess
import os

from core.proxy_checker.proxy_checker import ProxyChecker
from core.vmess.vmess_converter import VrayConverter

class VmessProxyChecker(ProxyChecker):
    def check(self, proxy):
        try:
            self.on_check(proxy)
            session = requests.Session()
            
            # Connect to VPN here
            # TODO Do something with this string
            if not os.path.exists("./core/vmess/tools/v2ray"):
                raise Exception("Could not find VMESS binary, please install it.")
            
            # Create a new config with the current
            converter = VrayConverter()
            converter.save_local_config_from_string(converter.convert_vmess_to_json(proxy))

            process = subprocess.Popen("./core/vmess/tools/v2ray", shell=True)
            print("Process has been executed")

            response = session.get(self.INTERROGATOR_URL, timeout=8, proxies={ "http": "socks5://127.0.0.1:1080" })

            if self.is_response_not_tampered(response):
                self.on_proxy_found(proxy)

            process.terminate()

        except requests.RequestException as e:
            print(f"Error: {e}")
            pass