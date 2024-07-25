class ProxyDetails:
    def __init__(self):
        self.connection_string = None
        self.public_ip = None
        self.port = None 
        self.type = None
        self.location = None
        self.coordinates = None
        
    def set_connection_string(self, connection_string: str):
        self.connection_string = connection_string
    
    def set_public_ip(self, public_ip: str):
        self.public_ip = public_ip
        
    def set_port(self, port: str):
        self.port = port
        
    def set_type(self, type: str):
        self.type = type
        
    def set_location(self, location: str):
        self.location = location
    
    def set_coordinates(self, coordinates: str):
        self.coordinates = coordinates
        
    def __str__(self) -> str:
        return f"""
            Connection string: {self.connection_string}
            Public ip: {self.public_ip}
            Port: {self.port}
            Type: {self.type}
            Coordinates: {self.coordinates}
            Location: {self.location}
        """
    