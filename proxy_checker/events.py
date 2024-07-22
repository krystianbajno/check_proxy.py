from proxy_checker.counter import add_progress, add_working, print_progress
from proxy_checker.file_ops import write_proxy
from proxy_checker.colors import Colors

def on_proxy_found(proxy, counter, output_file):
    print(f"[{Colors.GREEN}+{Colors.RESET}] {Colors.YELLOW}{proxy}{Colors.RESET} is a {Colors.GREEN}valid{Colors.RESET} proxy! Saving.")
    add_working(counter)
    write_proxy(output_file, proxy)

def on_check(proxy, counter):
    add_progress(counter)
    print_progress(counter, proxy)
