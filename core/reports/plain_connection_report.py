from core.file_ops import write_proxy

def append_connection_plain_report(output_file, proxy: str) -> None:
    write_proxy(output_file, proxy)