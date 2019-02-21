# Programming our first client

import socket

print("Socket created")

PORT = 8095
IP = "212.128.253.96"

while True:

    #Before connecting to the server, ask the usser for the string
    message = input("Please enter your message: ")

    if len(message) == 0:
        message = "empty"

    # We create sockets for communicating with the server, and then we define how we want it to work: as a file.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    s.connect((IP, PORT))

    #Send the request message to the server
    s.send(str.encode(message))

    # We receive the information from the server, and then we print it
    response = s.recv(2048).decode("utf-8")

    # Print server response
    print("Response: {}".format(response))

    s.close()

print("The end")
