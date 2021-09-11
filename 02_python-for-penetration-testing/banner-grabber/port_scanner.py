#!/usr/bin/env python3

import socket

def scan_port(ip: str, port: int):
    """
    Scan a port on a host
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)
    try:
        sock.connect((ip, port))
        print(f"{ip}:{port} is open")
    except socket.error:
        print(f"{ip}:{port} is closed")
    finally:
        sock.close()

if __name__ == '__main__':
    host = input("Enter IP address: ")
    ip = int(input("Enter IP address: "))
    scan_port(host, ip)
