#Programming our client

import socket


print("Socket created")

PORT = 8083
IP = "212.128.253.110"



while True:
    # We create sockets for communicating with the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the server
    s.connect((IP, PORT))
    send_msg = input("Please enter your message: ")
    s.send(str.encode(send_msg))

    #Receiving a message from the server
    msg = s.recv(2048).decode("utf-8")
    print("MESSAGE FROM THE SERVER:")
    print(msg)

print("The end")