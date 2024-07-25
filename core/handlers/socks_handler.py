import threading
from time import sleep
from core.classifiers.classifier_enum import ClassifierEnum
from core.entities.proxy import Proxy
from core.events import on_check, on_proxy_found
from core.proxy_checker.socks_proxy_checker import SocksProxyChecker
from core.utils import check_proxies, partition

def handle(https_proxies, output_list, on_proxy_found=on_proxy_found, on_check=on_check, num_threads=100):
    proxies = list([Proxy(proxy, ClassifierEnum.SOCKS) for proxy in https_proxies])
    
    divided_proxies = partition(proxies, num_threads)

    socks_checker = SocksProxyChecker(
        on_proxy_found=lambda proxy: on_proxy_found(proxy, output_list), 
        on_check=lambda proxy: on_check(proxy)
    )

    threads = []
    for sublist in divided_proxies:
        thread = threading.Thread(target=check_proxies, args=(sublist, socks_checker.check))
        thread.daemon = True
        threads.append(thread)
        thread.start()

    while any(thread.is_alive() for thread in threads):
        sleep(1)
        
    return output_list