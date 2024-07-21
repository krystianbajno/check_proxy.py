def read_proxies(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file]

def write_proxy(file_path, line):
    with open(file_path, "a") as file:
        file.write(line + "\n")