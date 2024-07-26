import argparse

from check_proxy.core.vmess.vmess_converter import VrayConverter

def main():
    parser = argparse.ArgumentParser(description='Get VMESS config json')
    parser.add_argument('vmess_connection_string', help='vmess:// connection string')
    args = parser.parse_args()
    
    converter = VrayConverter()
    
    try:
        json = converter.convert_vmess_to_json(args.vmess_connection_string)
        print(json)
    except:
        print("VMESS connection string is not valid")