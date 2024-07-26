import json
import base64
import os

from check_proxy.core.colors import Colors

vmscheme = "vmess://"

TPL = {}
TPL["CLIENT"] = """
{
  "log": {
    "access": "",
    "error": "",
    "loglevel": "error"
  },
  "inbounds": [],
  "outbounds": [
    {
      "protocol": "vmess",
      "settings": {
        "vnext": [
          {
            "address": "host.host",
            "port": 1234,
            "users": [
              {
                "email": "user@v2ray.com",
                "id": "",
                "alterId": 0,
                "security": "auto"
              }
            ]
          }
        ]
      },
      "streamSettings": {
        "network": "tcp"
      },
      "mux": {
        "enabled": true
      },
      "tag": "proxy"
    },
    {
      "protocol": "freedom",
      "tag": "direct",
      "settings": {
        "domainStrategy": "UseIP"
      }
    }
  ],
  "dns": {
    "servers": [
      "1.0.0.1",
      "localhost"
    ]
  },
  "routing": {
    "domainStrategy": "IPIfNonMatch",
    "rules": [
      {
        "type": "field",
        "ip": [
          "geoip:private",
          "geoip:cn"
        ],
        "outboundTag": "direct"
      },
      {
        "type": "field",
        "domain": [
          "geosite:cn"
        ],
        "outboundTag": "direct"
      }
    ]
  }
}
"""


class VrayConverter:
    def convert_vmess_to_json(self, vmess_string):
        if not vmess_string.startswith(vmscheme):
            raise ValueError("Invalid vmess link")

        base64_str = vmess_string[len(vmscheme):]
        padding = len(base64_str) % 4
        if padding > 0:
            base64_str += "=" * (4 - padding)
        
        decoded_str = base64.b64decode(base64_str).decode()
        vmess_data = json.loads(decoded_str)

        config = json.loads(TPL["CLIENT"])
        outbound = config["outbounds"][0]
        vnext = outbound["settings"]["vnext"][0]

        vnext["address"] = vmess_data["add"]
        vnext["port"] = int(vmess_data["port"])
        vnext["users"][0]["id"] = vmess_data["id"]
        vnext["users"][0]["alterId"] = int(vmess_data["aid"])

        outbound["streamSettings"]["network"] = vmess_data["net"]

        if vmess_data.get("tls") == "tls":
            outbound["streamSettings"]["security"] = "tls"
            outbound["streamSettings"]["tlsSettings"] = {"allowInsecure": True}
            if vmess_data.get("host"):
                outbound["streamSettings"]["tlsSettings"]["serverName"] = vmess_data["host"]
        
        return json.dumps(config)

    def save_local_config_from_string(self, vmess_string, config_path="./core/vmess/tools/config.json"):
        config = self.convert_vmess_to_json(vmess_string)

        os.makedirs(os.path.dirname(config_path), exist_ok=True)

        with open(config_path, "w") as config_handle:
            config_handle.write(
                config
            )
        print(f"[{Colors.GREEN}+{Colors.RESET}] Config saved to {config_path}")