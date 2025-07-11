# main.py
import argparse
from port_scanner import scan_ports
from brute_forcer import ssh_brute_force

def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd")

    pscan = sub.add_parser("scan")
    pscan.add_argument("target")
    pscan.add_argument("--start", type=int, default=1)
    pscan.add_argument("--end", type=int, default=1024)

    brut = sub.add_parser("brute")
    brut.add_argument("target")
    brut.add_argument("username")
    brut.add_argument("pwdfile")

    args = parser.parse_args()

    if args.cmd == "scan":
        results = scan_ports(args.target, args.start, args.end)
        print("Open ports:")
        for port, banner in results:
            print(f"{port}: {banner}")
    elif args.cmd == "brute":
        pwd = ssh_brute_force(args.target, args.username, args.pwdfile)
        if pwd:
            print(f"Password found! {args.username}:{pwd}")
        else:
            print("No valid password found.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
