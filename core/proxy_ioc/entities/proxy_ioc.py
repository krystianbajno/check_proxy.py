
class ProxyIoc:
    def __init__(self):
        self.public_ip = None
        
    def set_public_ip(self, public_ip):
        self.public_ip = public_ip
    
    def __str__(self):
        return self.public_ip