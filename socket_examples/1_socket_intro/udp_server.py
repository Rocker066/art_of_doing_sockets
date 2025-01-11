# UDP Server Side
import socket


# Create a server side socket IPV4 (AF_INET) and UDP (SOCK_DGRAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind our new socket to a tuple (IP address, Port address)
ip_addr = socket.gethostbyname(socket.gethostname())
port = 12345

server_socket.bind((ip_addr, port))

# We are not listening or accepting since UDP is a connectionless protocol

message, address = server_socket.recvfrom(1024)
print(message.decode('utf-8'))
print(address)