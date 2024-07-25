from core.colors import Colors
from core.counter import add_progress, add_working as ctr_add_working, print_progress
from core.events import on_check, on_proxy_found
from core.file_ops import append_proxy_report, write_proxy_report
from core.proxy_details.proxy_details_service import get_proxy_details
from core.reports.entities.csv_proxy_report import CSVProxyReport
from core.reports.plain_connection_report import append_connection_plain_report
from core.reports.plain_details_report import append_details_csv_plain_report, generate_details_csv_plain_report_data

def on_cli_proxy_found_decorator(output_file, counter, csv_report: CSVProxyReport):
    def decorated_func(proxy, output_list):
        print(f"[{Colors.GREEN}+{Colors.RESET}] {Colors.YELLOW}{proxy}{Colors.RESET} is a {Colors.GREEN}valid{Colors.RESET} proxy! Saving.")

        # Update counter
        ctr_add_working(counter)

        # Append proxy to working proxy list outfile
        append_proxy_report(output_file, append_connection_plain_report(proxy))
        
        # Get proxy details via various APIs
        proxy_details = get_proxy_details(proxy)

        # Update CSV detailed report
        report_data = generate_details_csv_plain_report_data(proxy_details)
        append_details_csv_plain_report(csv_report, report_data)

        # Save the CSV detailed report
        write_proxy_report(
             output_file + "_details.csv",
             csv_report.get_report_view()
        )

        # Middle forward
        return on_proxy_found(proxy, output_list)
        
    return decorated_func

def on_cli_proxy_check_decorator(counter):
        def decorated_func(proxy):
            add_progress(counter)
            print_progress(counter, proxy)
            return on_check(proxy)
        
        return decorated_func