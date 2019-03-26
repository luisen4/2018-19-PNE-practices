# Example of getting information about the weather of
# a location

import http.client
import json

# -- API information
HOSTNAME = "api.icndb.com"
ENDPOINTS = ["/jokes/count", "/categories", "/jokes/random"]

METHOD = "GET"


# -- Here we can define special headers if needed
headers = {'User-Agent': 'http-client'}

# -- Connect to the server
# -- NOTICE it is an HTTPS connection!
# -- If we do not specify the port, the standar one
# -- will be used
conn = http.client.HTTPSConnection(HOSTNAME)

text_json = []

for ep in ENDPOINTS:

    # -- Send the request. No body (None)
    # -- Use the defined headers
    conn.request(METHOD, ep, None, headers)

    # -- Wait for the server's response
    r = conn.getresponse()

    # -- Print the status
    print()
    print("Response received: ", end='')
    print(r.status, r.reason)

    # -- Read the response's body and close
    # -- the connection
    read_json = r.read().decode("utf-8")
    text_json.append(read_json)
    conn.close()

# -- Generate the object from the json file
number_jokes = json.loads(text_json[0])
categories = json.loads(text_json[1])
random_joke = json.loads(text_json[2])

# -- Get some data
totaljk = number_jokes['value']
name_categories = categories['value']
number_categories = len(name_categories)
joke = random_joke['value']['joke']

print()
print("Number of jokes: {}".format(totaljk))
print("Name of the categories: {}".format(','.join(n for n in name_categories)))
print("Number of different categories: {}".format(number_categories))
print("Random joke: {}".format(joke))