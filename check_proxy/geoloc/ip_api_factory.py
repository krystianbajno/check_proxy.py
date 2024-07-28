
from check_proxy.geoloc.entities.ip_api_response import IpApiResponse

def create_ip_api_response(res_json):
    ip_api_response = IpApiResponse()

    ip_api_response.set_status(res_json["status"])
    ip_api_response.set_query(res_json["query"])

    if res_json["status"] == "fail":
        ip_api_response.set_retrievable_fields("Unknown")
    else:
        ip_api_response.set_org(res_json["org"])
        ip_api_response.set_longitude(str(res_json["lon"]))
        ip_api_response.set_latitude(str(res_json["lat"]))
        ip_api_response.set_isp(res_json["isp"])
        ip_api_response.set_country(res_json["country"])
        ip_api_response.set_country_code(res_json["countryCode"])
        ip_api_response.set_city(res_json["city"])
        ip_api_response.set_as(res_json["as"])
        ip_api_response.set_region(res_json["region"])
        ip_api_response.set_region_name(res_json["regionName"])


    return ip_api_response