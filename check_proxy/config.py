import os

base_dir = os.path.dirname(os.path.abspath(__file__))

def configuration():
    return {
        "vmess_dist_dir": f"{base_dir}/dist/vmess/tools",
        "vmess_dist": f"{base_dir}/dist/vmess/tools/v2ray"
    }
