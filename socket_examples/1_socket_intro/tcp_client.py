# TCP Client Side
import socket


# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to a server located at a given IP and Port
ip_addr = socket.gethostbyname(socket.gethostname())
port = 12345
client_socket.connect((ip_addr, port))

# Receive a message from the server...You must specify the max number of bytes to receive
message = client_socket.recv(1024)
print(message.decode('utf-8'))

# Close the client socket
client_socket.close()