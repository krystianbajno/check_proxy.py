from core.entities.proxy import Proxy
from core.handlers.cli.event_listeners_cli import on_cli_proxy_check_decorator, on_cli_proxy_found_decorator
from core.handlers.socks_handler import handle as handle_socks
from core.reports.entities.csv_proxy_report import CSVProxyReport

def handle(csv_report: CSVProxyReport, counter, https_proxies: list[Proxy], output_file, num_threads: int):
    output_list = []
    
    handle_socks(
        https_proxies, 
        output_list,
        on_proxy_found=on_cli_proxy_found_decorator(output_file, counter, csv_report), 
        on_check=on_cli_proxy_check_decorator(counter),
        num_threads=num_threads
    )
    
    return output_list
