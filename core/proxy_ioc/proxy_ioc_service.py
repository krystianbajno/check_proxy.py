from core.proxy_details.entities.proxy_details import ProxyDetails
from core.proxy_ioc.entities.proxy_ioc import ProxyIoc

def get_ioc_from_proxy_details(proxy_details: ProxyDetails):
    proxy_ioc = ProxyIoc()
    proxy_ioc.set_public_ip(proxy_details.public_ip)
    
    return proxy_ioc