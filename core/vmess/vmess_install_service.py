import os
import requests
import sys
import zipfile

class VmessInstallService:

    def __init__(self, directory="./tools/"):
        self.directory = directory

    def check_exists(self):
        if os.path.isfile(os.path.join(self.directory, "v2ray")):
            return True
        return False

    def detect_os(self):
        os_map = {
            "linux": "linux-64",
            "win32": "windows-64",
            "darwin": "macos-arm64-v8a"
        }

        platform = sys.platform

        if platform in os_map:
            return os_map[platform]
        
        raise Exception("Error: Could not find OS type")

    def install(self):
        # Create the installation directory
        os.makedirs(self.directory, exist_ok=True)
        
        # Download the binary
        os_type = self.detect_os()
        binary = requests.get(f"https://github.com/v2fly/v2ray-core/releases/download/v5.16.1/v2ray-{os_type}.zip")

        zip_file_path = os.path.join(self.directory, "v2ray.zip")

        with open(zip_file_path, "wb") as fh:
            fh.write(binary.content)

        # Unzip the release
        with zipfile.ZipFile(zip_file_path) as zip_fh:
            zip_fh.extractall(self.directory)

if __name__ == "__main__":
    installer = VmessInstallService()
    installer.install()