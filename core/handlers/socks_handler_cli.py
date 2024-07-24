from core.handlers.cli_decorator import on_cli_proxy_check_decorator, on_cli_proxy_found_decorator
from core.handlers.socks_handler import handle as handle_socks

def handle(counter, https_proxies, output_file, num_threads):
    output_list = []
    
    handle_socks(
        https_proxies, 
        output_list,
        on_proxy_found=on_cli_proxy_found_decorator(output_file, counter), 
        on_check=on_cli_proxy_check_decorator(counter),
        num_threads=num_threads
    )
    
    return output_list
