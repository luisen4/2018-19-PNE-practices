import socket
import termcolor

IP = "212.128.253.106"
PORT = 8085
MAX_OPEN_REQUESTS = 5


# A function to read the content from the HTML file.
def read_html(filename):

    # Read the HTTP response message. It has the following lines
    # Status line
    # header
    # blank line
    # Body (content to send)

    # This new contents are written in HTML language and imported from the index file
    if filename == "":
        filename = "index.html"
    else:
        filename = filename + ".html"

    with open(filename, "r") as f:
        html = f.read()
        return html


def process_client(cs):

    """Process the client request.
    Parameters:  cs: socket for communicating with the client"""

    # Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")

    # Print the received message, for debugging
    print()
    print("Request message: ")
    termcolor.cprint(msg, 'green')

    # Split the message into three parts: 1) GET  2) /  3) More information
    # And the split it again to get the required command for choosing the html page

    msg = msg.partition("/")
    msg = msg[-1].partition(" ")

    if msg[0] == "blue":
        contents = read_html(msg[0])
    elif msg[0] == "pink":
        contents = read_html(msg[0])
    elif msg[0] == "":
        contents = read_html(msg[0])
    else:
        contents = read_html("error")

    # -- Everything is OK
    status_line = "HTTP/1.1 200 OK\r\n"

    # -- Build the header
    header = "Content-Type: text/html\r\n"
    header += "Content-Length: {}\r\n".format(len(str.encode(contents)))

    # -- Build the message by joining together all the parts
    response_msg = str.encode(status_line + header + "\r\n" + contents)
    cs.send(response_msg)

    # Close the socket
    cs.close()


# MAIN PROGRAM

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and PORT
serversocket.bind((IP, PORT))

# Configure the server sockets
# MAX_OPEN_REQUESTS connect requests before refusing outside connections
serversocket.listen(MAX_OPEN_REQUESTS)

print("Socket ready: {}".format(serversocket))

while True:
    # accept connections from outside
    # The server is waiting for connections
    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Connection received. A new socket is returned for communicating with the client
    print("Attending connections from client: {}".format(address))

    # Service the client
    process_client(clientsocket)
