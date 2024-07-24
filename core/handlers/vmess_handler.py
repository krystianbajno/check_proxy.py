from core.events import on_check, on_proxy_found
from core.proxy_checker.vmess_proxy_checker import VmessProxyChecker
from core.utils import check_proxies

def handle(vmess_proxies, output_list, on_proxy_found=on_proxy_found, on_check=on_check):
    vmess_checker = VmessProxyChecker(
        on_proxy_found=lambda proxy: on_proxy_found(proxy, output_list), 
        on_check=lambda proxy: on_check(proxy)
    )
    
    return check_proxies(vmess_proxies, vmess_checker.check)