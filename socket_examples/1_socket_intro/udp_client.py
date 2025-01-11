# UDP Client Side
import socket


# Create a UDP IPV4 socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send some information via a connectionless protocol
ip_addr = socket.gethostbyname(socket.gethostname())
port = 12345
client_socket.sendto('Hello server world!!!'.encode('utf-8'), (ip_addr, port))