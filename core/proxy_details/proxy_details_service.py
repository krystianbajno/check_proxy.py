import re
from core.classifiers.classifier_enum import ClassifierEnum
from core.entities.proxy import Proxy
from core.proxy_details.proxy_details_factory import create_proxy_details
from geoloc.geoloc_ipapi_client import get_ip_details


def generate_proxy_details(proxy: Proxy):
    proxy_class = proxy.type.name
    connection_string = proxy.connection_string
    is_proxy_safe = proxy.is_safe

    public_ip = None
    port = None

    if proxy_class == ClassifierEnum.VMESS:
        pass

    else:
        ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
        port_pattern = r':(\d+)'

        ip_match = re.search(ip_pattern, proxy.connection_string)    
        port_match = re.search(port_pattern, proxy.connection_string)

        public_ip = ip_match.group() if ip_match else None
        port = port_match.group(1) if port_match else None
        proxy_type = ClassifierEnum.SOCKS.name

    details = get_ip_details(public_ip)

    country = details.country
    isp = details.isp
    city = details.city
    region_name = details.region_name
    organization = details.org
    lat = details.latitude
    lon = details.longitude
        
    return create_proxy_details(
        connection_string,
        public_ip, 
        port,
        is_proxy_safe,
        proxy_type, 
        country, 
        isp, 
        city, 
        region_name, 
        organization, 
        lat, 
        lon
    )
