def read_proxies(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file]

def write_proxies(file_path, lines):
    with open(file_path, "a") as file:
        for line in lines:
            file.write(line + "\n")
        
def write_proxy(file_path, line):
    with open(file_path, "a") as file:
        file.write(line + "\n")