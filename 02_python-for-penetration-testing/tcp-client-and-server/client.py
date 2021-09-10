#!/usr/bin/env python3

import socket

host = socket.gethostname()
port = 444

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

message = client_socket.recv(1024)
client_socket.close()

print(message.decode('utf-8'))
