from core.file_ops import write_proxy
from core.proxy_ioc.entities.proxy_ioc import ProxyIoc

def append_ioc_plain_report(output_file, proxy_ioc: ProxyIoc) -> None:
    write_proxy(output_file, str(proxy_ioc))