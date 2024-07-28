import re
from check_proxy.core.classifiers.classifier_enum import ClassifierEnum
from check_proxy.core.entities.proxy import Proxy
from check_proxy.core.proxy_details.proxy_details_factory import create_proxy_details
from check_proxy.core.vmess.vmess_converter import VrayConverter
from check_proxy.geoloc.geoloc_ipapi_client import get_ip_details
import socket



def generate_proxy_details(proxy: Proxy):
    proxy_class = proxy.type.name
    connection_string = proxy.connection_string
    is_proxy_safe = proxy.is_safe

    public_ip = None
    port = None

    if proxy_class == ClassifierEnum.VMESS.name:
        vmess_config = VrayConverter.get_info_from_vmess(connection_string)
        public_ip = vmess_config["ip"]
        port = str(vmess_config["port"])
        proxy_type = ClassifierEnum.VMESS.name
        
        ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
        ip_match = re.search(ip_pattern, public_ip) 

        try: 
            if not ip_match:
                public_ip = socket.gethostbyname(public_ip)
        except:
            pass

    else:
        ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
        port_pattern = r':(\d+)'

        ip_match = re.search(ip_pattern, proxy.connection_string)    
        port_match = re.search(port_pattern, proxy.connection_string)

        if not ip_match:
            try:  
                public_ip = socket.gethostbyname(public_ip)
            except:
                pass
            port = port_match.group(1) if port_match else None
        else:  
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
