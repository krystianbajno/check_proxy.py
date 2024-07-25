from core.proxy_details.entities.proxy_details import ProxyDetails
from core.reports.entities.csv_proxy_report import CSVProxyReport

def generate_details_csv_plain_report_data(proxy_details: ProxyDetails) -> None:
    headers=["Connection string", "Public IP", "Port", "Type", "Coordinates", "Location"]

    return {
        "headers": headers,
        "line": [proxy_details.connection_string, proxy_details.public_ip, proxy_details.port, proxy_details.type, proxy_details.coordinates, proxy_details.location]
    }

def append_details_csv_plain_report(plain_csv_report: CSVProxyReport, report_data) -> None:
    if not len(plain_csv_report.headers):
          plain_csv_report.set_headers(report_data["headers"])

    plain_csv_report.append_line(report_data["line"])