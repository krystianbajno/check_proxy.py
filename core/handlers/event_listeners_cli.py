from core.colors import Colors
from core.counter import add_progress, add_working as ctr_add_working, print_progress
from core.events import on_check, on_proxy_found
from core.proxy_details.proxy_details_service import get_proxy_details
from core.proxy_ioc.proxy_ioc_service import get_ioc_from_proxy_details
from core.reports.plain_connection_report import append_connection_plain_report
from core.reports.plain_ioc_report import append_ioc_plain_report
from core.reports.plain_details_report import append_details_plain_report

def on_cli_proxy_found_decorator(output_file, counter):
    def decorated_func(proxy, output_list):
        print(f"[{Colors.GREEN}+{Colors.RESET}] {Colors.YELLOW}{proxy}{Colors.RESET} is a {Colors.GREEN}valid{Colors.RESET} proxy! Saving.")
        ctr_add_working(counter)
        append_connection_plain_report(output_file, proxy)
        
        proxy_details = get_proxy_details(proxy)
        
        append_details_plain_report(
            output_file + "_details",
            proxy_details
        )
        
        ioc = get_ioc_from_proxy_details(proxy_details)
        
        append_ioc_plain_report(
            output_file + "_ioc",
            ioc
        )
        
        return on_proxy_found(proxy, output_list)
        
    return decorated_func

def on_cli_proxy_check_decorator(counter):
        def decorated_func(proxy):
            add_progress(counter)
            print_progress(counter, proxy)
            return on_check(proxy)
        
        return decorated_func