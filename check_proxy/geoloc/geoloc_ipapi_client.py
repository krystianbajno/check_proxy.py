import requests

from check_proxy.geoloc.ip_api_factory import create_ip_api_response 

base_url = "http://ip-api.com/json/"

def get_ip_details(query_ip: str):
    response = requests.get(f"{base_url}{query_ip}")
    
    return create_ip_api_response(response.json())