from core.proxy_details.entities.proxy_details import ProxyDetails


class Proxy:
    def __init__(self, connection_string, type):
        self.connection_string = connection_string
        self.type = type
        self.is_working = False
        self.is_safe = False
        self.details = None
        
    def set_connection_string(self, connection_string):
        self.connection_string = connection_string
        
    def set_details(self, proxy_details: ProxyDetails):
        self.details = proxy_details
        
    def set_type(self, type):
        self.type = type
        
    def set_is_safe(self, is_safe):
        self.is_safe = is_safe
        
    def set_is_working(self, is_working):
        self.is_working = is_working