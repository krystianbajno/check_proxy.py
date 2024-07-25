from core.handlers.event_listeners_cli import on_cli_proxy_check_decorator, on_cli_proxy_found_decorator
from core.handlers.vmess_handler import handle as handle_vmess
from core.reports.entities.csv_proxy_report import CSVProxyReport

def handle(csv_report: CSVProxyReport, counter, vmess_proxies, output_file):
    output_list = []
    
    handle_vmess(
        vmess_proxies, 
        output_list,
        on_proxy_found=on_cli_proxy_found_decorator(output_file, counter, csv_report), 
        on_check=on_cli_proxy_check_decorator(counter),
    )
    
    return output_list