# port_scanner.py
import socket
from utils import validate_ip, banner_grab
from tqdm import tqdm

def scan_ports(target, start_port, end_port):
    if not validate_ip(target):
        raise ValueError("Invalid IP address")
    open_ports = []
    for port in tqdm(range(start_port, end_port + 1)):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            if s.connect_ex((target, port)) == 0:
                banner = banner_grab(target, port)
                open_ports.append((port, banner))
    return open_ports
