import http.server
import socketserver
import termcolor

# Define the Server's port
PORT = 8004


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # Open the file

        if self.path == "/":
            with open("form_ex_2.html", "r") as f:
                contents = f.read()
                f.close()
        elif "msg" in self.path:
            with open("echo2.html", "r") as f:
                echo_message = self.path[self.path.find("=")+1:self.path.find("&")]
                if "chk" in self.path:
                    echo_message = echo_message.upper()
                contents = f.read().format(echo_message)
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
