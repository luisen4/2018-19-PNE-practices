import http.server
import socketserver
import termcolor
from Seq import Seq

# Define the Server's port
PORT = 8004

# A function to validate the aminoacid sequence


def validsequence(seq):

    valid_aminoacids = ["A", "C", "T", "G"]

    for s in seq.upper():
        if s not in valid_aminoacids:
            return False
    if len(seq) == 0:
        return False

    return True
# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # Open the file

        if self.path == "/" or self.path == "/seq":
            with open("index.html", "r") as f:
                contents = f.read()
                f.close()
        elif "msg" in self.path:

            msg = self.path[self.path.find("=") + 1:self.path.find("&")]

            if validsequence(msg):
                with open("sequence.html", "r") as f:

                    seq = Seq(msg.upper())
                    base = self.path[self.path.find("base=")+5]
                    operation = self.path[self.path.find("operation=")+10:]

                    if operation == "count":
                        results = seq.count(base)
                    else:
                        base = str(base)
                        results = seq.perc(base)

                    if "chk" in self.path:
                        lenght = seq.len()
                        contents = f.read().format(msg, lenght, operation, base, results)

                    else:
                        contents = f.read().format(msg, "", operation, base, results)

                    f.close()
            else:
                with open("errorsequence.html", "r") as f:
                    contents = f.read()
                    f.close()
        else:
            with open("error.html", "r") as f:
                contents = f.read()
                f.close()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()

print("")
print("Server Stopped")
