import argparse
import sys

from core.banner import display_banner
from core.classifiers.classifier_enum import ClassifierEnum
from core.classifiers.proxy_classifier import classify_proxies_by_type, get_len_classified_proxies_total, get_len_of_proxy_class, get_proxies_by_class
from core.counter import create_counter, set_total
from core.file_ops import read_proxies
from core.handlers.socks_handler_cli import handle as handle_socks_cli
from core.handlers.vmess_handler_cli import handle as handle_vmess_cli

def main():
    parser = argparse.ArgumentParser(description='Check proxies from a list.')
    parser.add_argument('input_file', help='Path to the input proxy list file')
    parser.add_argument('output_file', help='Path to the output file')
    parser.add_argument('num_threads', nargs='?', type=int, help='Number of threads', default=100)
    parser.add_argument('--socks-only', help='Check only socks', action="store_true", default=False)

    args = parser.parse_args()
    if args.input_file == args.output_file:
        print("Input and output files must be different.")
        sys.exit(1)
    
    proxies = read_proxies(args.input_file)
    classified_proxies = classify_proxies_by_type(proxies)
    
    print(f"Input file: {args.input_file}")
    print(f"Output file: {args.output_file}")
    print(f"Number of threads: {args.num_threads}")
    print(f"Parsed HTTPS: {get_len_of_proxy_class(classified_proxies, ClassifierEnum.SOCKS)}")
    print(f"Parsed VMESS: {get_len_of_proxy_class(classified_proxies, ClassifierEnum.VMESS)}")
    input(f"[*] Press enter to start!\n")
    
    counter = create_counter()
    set_total(counter, get_len_classified_proxies_total(classified_proxies))
    
    if not args.socks_only:
        handle_vmess_cli(
            counter,
            get_proxies_by_class(
                classified_proxies, 
                ClassifierEnum.VMESS
            ),
            args.output_file
        )

    handle_socks_cli(
        counter, 
        get_proxies_by_class(
            classified_proxies, 
            ClassifierEnum.SOCKS
        ), 
        args.output_file, 
        args.num_threads
    )

if __name__ == "__main__":
    display_banner()
    
    try:
        main()
    except KeyboardInterrupt:
        print("[!] CTRL + C, stopping")
        sys.exit(0)