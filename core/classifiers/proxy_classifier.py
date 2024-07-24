def classify_proxies_by_type(proxies):
    out = {
        "vmess": [],
        "socks": []
    }
    
    __split_by(lambda proxy: "vmess" in proxy, proxies, out["vmess"])
    __split_by(lambda proxy: "vmess" not in proxy, proxies, out["socks"])
    
    return out

def __split_by(callback, in_array, out_array):
    for item in in_array:
        if callback(item): out_array.append(item)