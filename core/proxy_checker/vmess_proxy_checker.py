import requests
import subprocess
import os

from core.proxy_checker.proxy_checker import ProxyChecker
from core.vmess.vmess_converter import VrayConverter

class VmessProxyChecker(ProxyChecker):
    def __init__(self, v2ray_exec, on_proxy_found, on_check):
        self.v2ray_exec = v2ray_exec

        super().__init__(
            on_proxy_found,
            on_check
        )

    def check(self, proxy):
        try:
            self.on_check(proxy)
            session = requests.Session()
            
            # Connect to VPN here
            if not os.path.exists(self.v2ray_exec):
                raise Exception("Could not find VMESS binary, please install it.")
            
            # Create a new config with the current
            converter = VrayConverter()
            converter.save_local_config_from_string(converter.convert_vmess_to_json(proxy))

            process = subprocess.Popen(self.v2ray_exec, shell=True)
            print("Process has been executed")

            response = session.get(self.INTERROGATOR_URL, timeout=8, proxies={ "http": "socks5://127.0.0.1:1080" })

            is_proxy_safe = False
            if response is not None and self.is_response_not_tampered(response):
                is_proxy_safe = True

            self.on_proxy_found(proxy, is_proxy_safe)

            process.terminate()

        except requests.RequestException as e:
            print(f"Error: {e}")
            pass