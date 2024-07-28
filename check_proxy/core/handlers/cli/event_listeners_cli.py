from check_proxy.core.colors import Colors
from check_proxy.core.counter import add_progress, add_working as ctr_add_working, print_progress
from check_proxy.core.entities.proxy import Proxy
from check_proxy.core.events import on_check, on_proxy_found
from check_proxy.core.file_ops import append_proxy_report, write_proxy_report
from check_proxy.core.proxy_details.proxy_details_service import generate_proxy_details
from check_proxy.core.reports.connection_string_report import append_connection_string_report
from check_proxy.core.reports.details_csv_report import append_details_csv_report, generate_details_csv_report_data
from check_proxy.core.reports.details_report import append_details_report
from check_proxy.core.reports.entities.csv_proxy_report import CSVProxyReport

def on_cli_proxy_found_decorator(output_file, counter, csv_report: CSVProxyReport):
    def decorated_func(proxy: Proxy, output_list):
        print(f"[{Colors.GREEN}+{Colors.RESET}] {Colors.YELLOW}{proxy.connection_string[:64]}{Colors.RESET} is a {Colors.GREEN}valid{Colors.RESET} proxy! Saving.")

        # Update counter
        ctr_add_working(counter)

        # Append proxy to working proxy list outfile
        append_proxy_report(output_file, append_connection_string_report(proxy))
        
        # Get proxy details via various APIs
        proxy.set_details(generate_proxy_details(proxy))
        
        details_report = append_details_report(proxy)
        print(details_report)

        append_proxy_report(
            output_file + "_details",
            details_report
        )

        # Update CSV detailed report
        report_data = generate_details_csv_report_data(proxy)
        append_details_csv_report(csv_report, report_data)

        # Save the CSV detailed report
        write_proxy_report(
             output_file + "_details.csv",
             csv_report.get_report_view()
        )

        return on_proxy_found(proxy, output_list)
        
    return decorated_func

def on_cli_proxy_check_decorator(counter):
        def decorated_func(proxy: Proxy):
            add_progress(counter)
            print_progress(counter, proxy.connection_string)
            return on_check(proxy)
        
        return decorated_func
    