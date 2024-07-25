from core.entities.proxy import Proxy
from core.reports.entities.csv_proxy_report import CSVProxyReport

def generate_details_csv_report_data(proxy: Proxy) -> None:
    headers=["connection string", "public ip", "port", "type", "safe", "country", "isp", "city", "region_name", "organization", "lat", "lon"]

    return {
        "headers": headers,
        "line": [
            proxy.details.connection_string,
            proxy.details.public_ip,
            proxy.details.port,
            proxy.details.type,
            str(proxy.details.is_safe),
            proxy.details.country,
            proxy.details.isp,
            proxy.details.city,
            proxy.details.region_name,
            proxy.details.organization,
            proxy.details.lat,
            proxy.details.lon
        ]
    }

def append_details_csv_report(plain_csv_report: CSVProxyReport, report_data) -> None:
    if not len(plain_csv_report.headers):
        plain_csv_report.set_headers(report_data["headers"])

    plain_csv_report.append_line(report_data["line"])