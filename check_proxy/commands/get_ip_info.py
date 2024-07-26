import argparse

from check_proxy.geoloc.geoloc_ipapi_client import get_ip_details

def main():
    parser = argparse.ArgumentParser(description='Get IP info')
    parser.add_argument('ip', help='IP Address')
    args = parser.parse_args()
    
    try:
        ip_details = get_ip_details(args.ip)
        
        print(ip_details)
    except:
        print(f"No result found for {args.ip}")
        

if __name__ == "__main__":
    main()