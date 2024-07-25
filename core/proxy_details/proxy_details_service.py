import re
from core.classifiers.classifier_enum import ClassifierEnum
from core.classifiers.proxy_classifier import classify_proxy
from core.proxy_details.proxy_details_factory import create_proxy_details
from geoloc.geoloc_ipapi_client import get_ip_details


def get_proxy_details(proxy):
    proxy_class = classify_proxy(proxy)
    connection_string = proxy

    public_ip = None
    port = None

    if proxy_class == ClassifierEnum.VMESS:
        pass

    else:
        ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
        port_pattern = r':(\d+)'

        ip_match = re.search(ip_pattern, proxy)    
        port_match = re.search(port_pattern, proxy)

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
        proxy_type, 
        country, 
        isp, 
        city, 
        region_name, 
        organization, 
        lat, 
        lon
    )
