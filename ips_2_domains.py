import sys
import socket
from termcolor import colored

def get_domain(ip):
    try:
        domain = socket.gethostbyaddr(ip)[0]
        return domain
    except socket.herror:
        return None

def main(file_path):
    with open(file_path, 'r') as file:
        ip_addresses = file.readlines()

    for ip in ip_addresses:
        ip = ip.strip()
        domain = get_domain(ip)
        if domain:
            print(colored(ip, 'green'), colored(f": {domain}", 'red'))
        else:
            print(colored(ip, 'green'), colored(": Not found", 'red'))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 ip_rev.py <ips_file>")
    else:
        main(sys.argv[1])
