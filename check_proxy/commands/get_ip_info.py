import argparse

from check_proxy.core.classifiers.classifier_enum import ClassifierEnum
from check_proxy.core.vmess.vmess_converter import VrayConverter
from check_proxy.geoloc.geoloc_ipapi_client import get_ip_details
from check_proxy.core.classifiers.proxy_classifier import classify_proxy

def main():
    parser = argparse.ArgumentParser(description='Get IP info')
    parser.add_argument('ip', help='IP Address')
    args = parser.parse_args()
    
    ip = args.ip
    
    if classify_proxy(ip) == ClassifierEnum.VMESS:
        data = VrayConverter.get_info_from_vmess(args.ip)
        ip = data["ip"]

    try:
        ip_details = get_ip_details(ip)
        
        print(ip_details)
    except:
        print(f"No result found for {ip}")