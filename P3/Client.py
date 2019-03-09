import socket

# Server IP, PORT
PORT = 8084
IP = "172.20.10.6"

# Before connecting to the server, ask the user for the string
message = "ACTG" + "\n" + "reverse"

# We create sockets for communicating with the server, and then we define how we want it to work: as a file.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
s.connect((IP, PORT))

# Send the request message to the server
s.send(str.encode(message))

# We receive the information from the server, and then we print it
response = s.recv(2048).decode("utf-8")

# Print server response
print("Response: {}".format(response))
