class ProxyDetails:
    def __init__(self):
        self.connection_string = None
        self.public_ip = None
        self.port = None 
        self.type = None
        self.country = None
        self.is_safe = None
        self.isp = None
        self.city = None
        self.region_name = None
        self.organization = None
        self.lat = None
        self.lon = None
        
    def set_connection_string(self, connection_string: str):
        self.connection_string = connection_string
    
    def set_public_ip(self, public_ip: str):
        self.public_ip = public_ip
        
    def set_is_safe(self, is_proxy_safe):
        self.is_proxy_safe = is_proxy_safe

    def set_port(self, port: str):
        self.port = port
        
    def set_type(self, type: str):
        self.type = type

    def set_country(self, country):
        self.country = country

    def set_isp(self, isp):
        self.isp = isp

    def set_city(self, city):
        self.city = city 

    def set_region_name(self, region_name):
        self.region_name = region_name

    def set_organization(self, organization):
        self.organization = organization

    def set_lat(self, lat):
        self.lat = lat

    def set_lon(self, lon):
        self.lon = lon
    
    def __str__(self) -> str:
        return f"""
🛜  Connection string: {self.connection_string}
🛜  Public ip: {self.public_ip}
🛜  Port: {self.port}
🛜  Type: {self.type}
🛜  Safe: {str(self.is_safe)}
🌎  Country: {self.country}
🌎  ISP: {self.isp}
🌎  City: {self.city}
🌎  Region Name: {self.region_name}
🌎  Organization: {self.organization}
🌎  Latitude: {self.lat}
🌎  Longitude: {self.lon}
        """
    