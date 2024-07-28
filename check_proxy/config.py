import os
cwd = os.getcwd()

def configuration():
    return {
        "vmess_dist_dir": f"{cwd}/dist/vmess/tools/",
        "vmess_dist": f"{cwd}/dist/vmess/tools/v2ray"
    }
