import socket

# Server IP, PORT
PORT = 8083
IP = "172.20.10.6"

while True:
    # Before connecting to the server, ask the user for the string
    message = ""
    instruction = input("-")

    # Creating a loop to ask the user for all the operations
    while len(instruction) > 0:

        message = message + instruction + '\n'
        instruction = input("-")

    # Creating a control for checking if the server is ALIVE.
    if len(instruction) == 0:
        message = "\n"

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

