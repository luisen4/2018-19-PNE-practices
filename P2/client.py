from Seq import Seq

import socket

print("Socket created")

PORT = 8085
IP = "212.128.253.110"

while True:

    # We create sockets for communicating with the server, and then we define how we want it to work: as a file.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    s.connect((IP, PORT))

    seq = Seq(input("Please introduce your sequence: "))
    comp = seq.complement()
    rev = seq.reverse()

    # Sending a message from the server
    s.send(str.encode(comp.strbases + "\n" + rev.strbases))

    # Receiving a message from the server
    msg = s.recv(2048).decode("utf-8")
    print("MESSAGE FROM THE SERVER:")
    print(msg)

PRINT("The end")