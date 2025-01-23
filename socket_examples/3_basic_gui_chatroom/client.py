# Client Side GUI Chat Room
import tkinter as tk
import socket, threading
from tkinter import DISABLED, VERTICAL

# Define window
root = tk.Tk()
root.title('Chat Client')
root.iconbitmap('message_icon.ico')
root.geometry('600x600')
root.resizable(0, 0)

# Define fonts and colors
my_font = ('SimSun', 14)
black = '#010101'
light_green = '#1fc742'
root.config(bg=black)


# Define functions
def connect():
    """Connect to a server at a given IP/Port address"""
    pass


def verify_connection():
    """Verify that the server connection is valid and pass required information"""
    pass


def disconnect():
    """Disconnect from the server"""
    pass


def send_message():
    """Send a message to the server to be broadcast"""
    pass


def receive_message():
    """Receive an incoming message from the server"""
    pass


# Define GUI Layout
info_frame = tk.Frame(root, bg=black)
output_frame = tk.Frame(root, bg=black)
input_frame = tk.Frame(root, bg=black)
info_frame.pack()
output_frame.pack(pady=10)
input_frame.pack()

# Info Frame Layout
name_label = tk.Label(info_frame, text='Client Name:', font=my_font, fg=light_green, bg=black)
name_entry = tk.Entry(info_frame, borderwidth=3, font=my_font)
ip_label = tk.Label(info_frame, text='Host IP:', font=my_font, fg=light_green, bg=black)
ip_entry = tk.Entry(info_frame, borderwidth=3, font=my_font)
port_label = tk.Label(info_frame, text='Port Num:', font=my_font, fg=light_green, bg=black)
port_entry = tk.Entry(info_frame, borderwidth=3, font=my_font, width=10)
# Connect/disconnect button
connect_button = tk.Button(info_frame, text='Connect', font=my_font, bg=light_green,
                           borderwidth=5, width=10)
disconnect_button = tk.Button(info_frame, text='Disconnect', font=my_font, bg=light_green,
                              borderwidth=5, width=10, state=DISABLED)

# Output Frame Layout
my_scrollbar = tk.Scrollbar(output_frame, orient=VERTICAL)
my_list_box = tk.Listbox(output_frame, height=20, width=55, borderwidth=3, bg=black, fg=light_green, font=my_font,
                         yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list_box.yview)
my_list_box.grid(row=0, column=0)
my_scrollbar.grid(row=0, column=1, sticky='NS')

# Input Frame Layout
input_entry = tk.Entry(input_frame, width=45, borderwidth=3, font=my_font)
send_button = tk.Button(input_frame, text='Send', borderwidth=5, width=10, font=my_font, bg=light_green, state=DISABLED)
input_entry.grid(row=0, column=0, padx=5, pady=5)
send_button.grid(row=0, column=1, padx=5, pady=5)

# Grid the Info frame labels and buttons
name_label.grid(row=0, column=0, padx=2, pady=10)
name_entry.grid(row=0, column=1, padx=2, pady=10)
port_label.grid(row=0, column=2, padx=2, pady=10)
port_entry.grid(row=0, column=3, padx=2, pady=10)
ip_label.grid(row=1, column=0, padx=2, pady=5)
ip_entry.grid(row=1, column=1, padx=2, pady=5)
connect_button.grid(row=1, column=2, padx=4, pady=5)
disconnect_button.grid(row=1, column=3, padx=4, pady=5)



# Run the root window's mainloop
root.mainloop()