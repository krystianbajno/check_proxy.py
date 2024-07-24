from core.colors import Colors
from core.counter import add_progress, add_working, print_progress
from core.file_ops import write_proxy
from core.handlers.socks_handler import handle as handle_socks
from core.events import on_check, on_proxy_found

def on_cli_proxy_found_decorator(output_file, counter):
    def decorated_func(proxy, output_list):
        write_proxy(output_file, proxy)
        print(f"[{Colors.GREEN}+{Colors.RESET}] {Colors.YELLOW}{proxy}{Colors.RESET} is a {Colors.GREEN}valid{Colors.RESET} proxy! Saving.")
        add_working(counter)
        return on_proxy_found(proxy, output_list)
        
    return decorated_func

def on_cli_proxy_check_decorator(counter):
        def decorated_func(proxy):
            add_progress(counter)
            print_progress(counter, proxy)
            return on_check(proxy)
        
        return decorated_func

def handle(counter, https_proxies, output_file, num_threads):
    handle_socks(
        https_proxies, 
        [],
        on_proxy_found=on_cli_proxy_found_decorator(output_file, counter), 
        on_check=on_cli_proxy_check_decorator(counter),
        num_threads=num_threads
    )
