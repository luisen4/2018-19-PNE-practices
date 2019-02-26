import socket
import sys
from Seq import Seq

# Configure the Server's IP and PORT
PORT = 8083
IP = "172.20.10.6"
MAX_OPEN_REQUESTS = 5

# A function for validating the sequence
def validsequence(seq):

    valid_aminoacids = ["A", "C", "T", "G"]

    for s in seq:
        if s not in valid_aminoacids:
            return False

    return True

# A function to perform all the required operations.
def operation(seq, function):

    if function == "len":
        return seq.len()
    elif function == "complement":
        return seq.complement()
    elif function == "reverse":
        return seq.reverse()
    elif function[:-1] == "count":
        return seq.count(function[-1])
    elif function[:-1] == "perc":
        return seq.perc(function[-1])

# A function to read the client requests
def client_proccess(clientsocket):

    # Read the message from the client and decode it as a string
    msg = clientsocket.recv(2048).decode("utf-8")
    print("Message from client: {}".format(msg))

    if msg == "\n":
        response = "ALIVE!"
    else:
        msg = msg.split("\n")
        if validsequence(msg[0]):
            response = "OK"
            seq = Seq(msg[0])
            i = 1
            for i in range(len(msg)-1):
                data = operation(seq, msg[i])
                response = response + str(data) + "\n"
        else:
            response = "ERROR"



# MAIN PROGRAM

# Create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Become a server socket
    serversocket.bind((IP, PORT))

    # Configure the server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        # Accept connections from outside
        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (clientsocket, address) = serversocket.accept()

        # Connection received. A new socket is returned for communicating with the client
        print("Attending connections from client: {}".format(address))

        clientsocket.close()

except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()
