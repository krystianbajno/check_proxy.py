from check_proxy.config import configuration
from check_proxy.core.classifiers.classifier_enum import ClassifierEnum
from check_proxy.core.entities.proxy import Proxy
from check_proxy.core.events import on_check, on_proxy_found
from check_proxy.core.proxy_checker.vmess_proxy_checker import VmessProxyChecker
from check_proxy.core.utils import check_proxies

def handle(vmess_proxies, output_list, on_proxy_found=on_proxy_found, on_check=on_check):
    proxies = list([Proxy(proxy, ClassifierEnum.VMESS) for proxy in vmess_proxies])

    vmess_checker = VmessProxyChecker(
        configuration()["vmess_dist_dir"],
        on_proxy_found=lambda proxy: on_proxy_found(proxy, output_list), 
        on_check=lambda proxy: on_check(proxy)
    )
    
    return check_proxies(proxies, vmess_checker.check)