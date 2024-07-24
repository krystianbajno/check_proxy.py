from core.counter import add_progress, add_working, print_progress
from core.colors import Colors

def on_proxy_found(proxy, counter, working_arr):
    print(f"[{Colors.GREEN}+{Colors.RESET}] {Colors.YELLOW}{proxy}{Colors.RESET} is a {Colors.GREEN}valid{Colors.RESET} proxy! Saving.")
    add_working(counter)
    working_arr.append(proxy)

def on_check(proxy, counter):
    add_progress(counter)
    print_progress(counter, proxy)
