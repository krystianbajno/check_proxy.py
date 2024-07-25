from core.proxy_details.proxy_details_factory import create_proxy_details

#todo
def get_proxy_details(proxy):
    if "vmess":
        #todo
        pass
    
    if "socks":
        #todo
        pass

    connection_string = "todo"
    public_ip = "todo"
    port = "todo"
    proxy_type = "todo"
    location = "todo"
    coordinates = "todo"
    
    return create_proxy_details(connection_string, public_ip, port, proxy_type, location, coordinates)
