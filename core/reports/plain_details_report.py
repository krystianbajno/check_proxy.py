from core.file_ops import write_proxy
from core.proxy_details.entities.proxy_details import ProxyDetails

def append_details_plain_report(output_file, proxy_details: ProxyDetails) -> None:
    write_proxy(output_file, str(proxy_details))