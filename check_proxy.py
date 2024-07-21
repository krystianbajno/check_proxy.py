import argparse
import sys
import threading
from time import sleep

from proxy_checker.banner import display_banner
from proxy_checker.file_ops import read_proxies, write_proxy
from proxy_checker.proxy_checker import ProxyChecker
from proxy_checker.counter import add_progress, create_counter, set_total, add_working, print_progress
from proxy_checker.utils import partition
from proxy_checker.colors import Colors

def on_proxy_found(proxy, output_file, counter):
    print(f"[{Colors.GREEN}+{Colors.RESET}] {Colors.YELLOW}{proxy}{Colors.RESET} is a {Colors.GREEN}valid{Colors.RESET} proxy! Saving.")
    add_working(counter)
    write_proxy(output_file, proxy)

def on_progress(counter, proxy):
    add_progress(counter)
    print_progress(counter, proxy)
    pass

def main():
    parser = argparse.ArgumentParser(description='Check proxies from a list.')
    parser.add_argument('proxy_list', help='Path to the proxy list file')
    parser.add_argument('output_list', help='Path to the output file')
    parser.add_argument('num_threads', type=int, help='Number of threads')

    args = parser.parse_args()

    if args.proxy_list == args.output_list:
        print("Input and output files must be different.")
        sys.exit(1)

    proxies = read_proxies(args.proxy_list)
    divided_proxies = partition(proxies, args.num_threads)

    print(f"[*] {len(proxies)} proxies divided into {args.num_threads} threads and sublists (approx. {len(divided_proxies[0])} each)")
    print(f"Input file: {args.proxy_list}")
    print(f"Output file: {args.output_list}")
    input(f"[*] Press enter to start!\n")

    counter = create_counter()
    set_total(counter, len(proxies))

    threads = []
    for sublist in divided_proxies:
        checker = ProxyChecker(sublist, on_proxy_found=lambda proxy: on_proxy_found(proxy, args.output_list, counter), on_progress=lambda proxy: on_progress(counter, proxy))
        thread = threading.Thread(target=checker.run)
        thread.daemon = True
        threads.append(thread)
        thread.start()

    try:
        while any(thread.is_alive() for thread in threads):
            sleep(1)
    except KeyboardInterrupt:
        print("[*] Stopping")
        sys.exit(0)

if __name__ == "__main__":
    display_banner()
    main()