# Server Side Chat Room
import socket, threading


# Define constants to be used
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345
ENCODER = 'utf-8'
BYTESIZE = 1024

# Create a server socket, bind and listen
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

# Create two blank lists to store connected client sockets and their names
client_socket_list = []
client_name_list = []


def broadcast_message(message):
    """Send a message to all clients connected to the server"""
    for client_socket in client_socket_list:
        client_socket.send(message)


def receive_message(client_socket):
    """Receive an incoming message from a specific client and forward the message to be broadcast"""
    while True:
        try:
            # Get the name of the given client
            index = client_socket_list.index(client_socket)
            name = client_name_list[index]

            # Receive message from the client
            message = client_socket.recv(BYTESIZE).decode(ENCODER)
            message = f'\033[1;92m\t{name}: {message}\033[0m'.encode(ENCODER)
            broadcast_message(message)
        except:
            # First find the index of the client socket in out list
            index = client_socket_list.index(client_socket)
            name = client_name_list[index]

            # Remove the client socket and name from the lists
            client_socket_list.remove(client_socket)
            client_name_list.remove(name)

            # Close the client socket
            client_socket.close()

            # Broadcast that the client has left the chat
            broadcast_message(f'\033[5;91m{name} has left the chat!\033[0m'.encode(ENCODER))
            break


def connect_client():
    """Connect an incoming client to the server"""
    while True:
        # Accept any incoming client connection
        client_socket, client_address = server_socket.accept()
        print(f'Connected with {client_address}...')

        # Send a NAME flag to prompt the client for their name
        client_socket.send('NAME'.encode(ENCODER))
        client_name = client_socket.recv(BYTESIZE).decode(ENCODER)

        # add new client socket and client name to the appropriate lists
        client_socket_list.append(client_socket)
        client_name_list.append(client_name)

        # Update the server, individual client, and ALL clients
        print(f'Name of new client is {client_name}\n')
        # Send a message to an individual client
        client_socket.send(f'{client_name}, you have connected to the server!'.encode(ENCODER))
        broadcast_message(f'{client_name} has joined the chat!'.encode(ENCODER))

        # Now that a new client has connected, start a thread
        receive_thread = threading.Thread(target=receive_message, args=(client_socket,))
        receive_thread.start()


# Start the server
print('Server is listening for incoming connections...\n')
connect_client()