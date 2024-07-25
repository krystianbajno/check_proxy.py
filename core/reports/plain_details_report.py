from core.proxy_details.entities.proxy_details import ProxyDetails
from core.reports.entities.csv_proxy_report import CSVProxyReport

def generate_details_csv_plain_report_data(proxy_details: ProxyDetails) -> None:
    headers=["connection string", "public ip", "port", "type", "safe", "country", "isp", "city", "region_name", "organization", "lat", "lon"]

    return {
        "headers": headers,
        "line": [
            proxy_details.connection_string,
            proxy_details.public_ip,
            proxy_details.port,
            proxy_details.type,
            str(proxy_details.is_safe),
            proxy_details.country,
            proxy_details.isp,
            proxy_details.city,
            proxy_details.region_name,
            proxy_details.organization,
            proxy_details.lat,
            proxy_details.lon
        ]
    }

def append_details_csv_plain_report(plain_csv_report: CSVProxyReport, report_data) -> None:
    if not len(plain_csv_report.headers):
        plain_csv_report.set_headers(report_data["headers"])

    plain_csv_report.append_line(report_data["line"])