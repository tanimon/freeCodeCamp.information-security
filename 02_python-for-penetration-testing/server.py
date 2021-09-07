#!/usr/bin/env python3

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 444

server_socket.bind((host, port))
server_socket.listen(3)

while True:
    client_socket, addr = server_socket.accept()
    
    message = "Hello! Thank you connecting the server!\n"
    client_socket.send(message.encode())

    client_socket.close()
