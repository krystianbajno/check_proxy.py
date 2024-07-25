from core.proxy_details.entities.proxy_details import ProxyDetails

def create_proxy_details(connection_string, public_ip, port, proxy_type, location, coordinates):
    proxy_details = ProxyDetails()
    
    proxy_details.set_connection_string(connection_string)
    proxy_details.set_coordinates(coordinates)
    proxy_details.set_location(location)
    proxy_details.set_port(port)
    proxy_details.set_public_ip(public_ip)
    proxy_details.set_type(proxy_type)
    
    return proxy_details