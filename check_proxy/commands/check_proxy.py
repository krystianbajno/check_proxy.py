import argparse
import sys

from check_proxy.config import configuration
from check_proxy.core.banner import display_banner
from check_proxy.core.classifiers.classifier_enum import ClassifierEnum
from check_proxy.core.classifiers.proxy_classifier import classify_proxies_by_type, get_len_classified_proxies_total, get_len_of_proxy_class, get_proxies_by_class
from check_proxy.core.cleaner.proxy_cleaner import clean_proxies
from check_proxy.core.counter import create_counter, set_total
from check_proxy.core.file_ops import read_proxies
from check_proxy.core.handlers.cli.hoc.socks_handler_cli_hoc import handle as handle_socks_cli
from check_proxy.core.handlers.cli.hoc.vmess_handler_cli_hoc import handle as handle_vmess_cli
from check_proxy.core.reports.entities.csv_proxy_report import CSVProxyReport
from check_proxy.core.vmess.vmess_install_service import VmessInstallService


def main():
    display_banner()
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
    proxies = clean_proxies(proxies)
    
    classified_proxies = classify_proxies_by_type(proxies)
    
    print(f"Input file: {args.input_file}")
    print(f"Output file: {args.output_file}")
    print(f"Number of threads: {args.num_threads}")
    print(f"Parsed HTTPS: {get_len_of_proxy_class(classified_proxies, ClassifierEnum.SOCKS)}")
    print(f"Parsed VMESS: {get_len_of_proxy_class(classified_proxies, ClassifierEnum.VMESS)}")
    input(f"[*] Press enter to start!\n")
    
    installer = VmessInstallService(configuration()["vmess_dist_dir"])
    
    if get_len_of_proxy_class(classified_proxies, ClassifierEnum.VMESS) > 0 and not installer.check_exists():
        choice = input("Do you want to install utility tools for V2Ray VMESS proxy?")
        if "y" in choice.lower():
            installer.install()

    counter = create_counter()
    csv_report = CSVProxyReport.create_report()

    set_total(counter, get_len_classified_proxies_total(classified_proxies))
    
    if not args.socks_only:
        handle_vmess_cli(
            csv_report,
            counter,
            get_proxies_by_class(
                classified_proxies, 
                ClassifierEnum.VMESS
            ),
            args.output_file
        )

    handle_socks_cli(
        csv_report,
        counter,
        get_proxies_by_class(
            classified_proxies, 
            ClassifierEnum.SOCKS
        ), 
        args.output_file, 
        args.num_threads
    )
