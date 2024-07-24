from core.file_ops import write_proxy
from core.handlers.socks_handler import handle as handle_socks
from core.events import on_proxy_found

def on_cli_proxy_found_decorator(output_file):
    def decorated_func(proxy, counter, output_list):
        write_proxy(output_file, proxy)
        return on_proxy_found(proxy, counter, output_list)
        
    return decorated_func

def handle(counter, https_proxies, output_file, num_threads):   
    found_arr = []
    
    handle_socks(
        counter, 
        https_proxies, 
        found_arr,
        on_proxy_found=on_cli_proxy_found_decorator(output_file), 
        num_threads=num_threads
    )
