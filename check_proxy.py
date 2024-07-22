import argparse
import sys
import threading
from time import sleep

from proxy_checker.banner import display_banner
from proxy_checker.events import on_check, on_proxy_found
from proxy_checker.file_ops import read_proxies
from proxy_checker.proxy_checker import ProxyChecker
from proxy_checker.counter import create_counter, set_total
from proxy_checker.utils import check_proxies, partition

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

    socks_checker = ProxyChecker(
        on_proxy_found=lambda proxy: on_proxy_found(proxy, args.output_list, counter), 
        on_check=lambda proxy: on_check(proxy, counter)
    )

    threads = []
    for sublist in divided_proxies:
        thread = threading.Thread(target=check_proxies, args=(sublist, socks_checker.check))
        thread.daemon = True
        threads.append(thread)
        thread.start()

    while any(thread.is_alive() for thread in threads):
        sleep(1)
 
if __name__ == "__main__":
    display_banner()
    
    try:
        main()
    except KeyboardInterrupt:
        print("[!] CTRL + C, stopping")
        sys.exit(0)