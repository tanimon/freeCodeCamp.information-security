#!/usr/bin/env python3

import socket

def get_banner(ip: str, port: int) -> bytes:
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except Exception as e:
        print(e)
        return b''

def main():
    ip = input("Please enter the IP address: ")
    port = int(input("Please enter the port number: "))
    banner = get_banner(ip, port)
    print(banner)

if __name__ == "__main__":
    main()
