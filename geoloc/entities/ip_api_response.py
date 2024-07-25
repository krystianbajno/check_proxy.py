
class IpApiResponse:
    def __init__(self):
        self.query = None
        self.status = None 
        self.country = None
        self.country_code = None 
        self.region = None
        self.region_name = None
        self.city = None
        self.zip = None
        self.latidude = None
        self.longitude = None
        self.timezone = None
        self.isp = None
        self.org = None
        self.f_as = None

    def set_country(self, country):
        self.country = country

    def set_query(self, query):
        self.query = query

    def set_status(self, status):
        self.status = status

    def set_country_code(self, country_code):
        self.country_code = country_code

    def set_region(self, region):
        self.region = region

    def set_region_name(self, region_name):
        self.region_name = region_name

    def set_city(self, city):
        self.city = city

    def set_zip(self, zip):
        self.zip = zip

    def set_latitude(self, lat):
        self.latitude = lat

    def set_longitude(self, lon):
        self.longitude = lon

    def set_timezone(self, timezone):
        self.timezone = timezone

    def set_isp(self, isp):
        self.isp = isp

    def set_org(self, org):
        self.org = org 

    def set_as(self, asf):
        self.f_as = asf