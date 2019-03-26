# Example of getting information about the weather of
# a location

import http.client
import json

# -- API information
HOSTNAME = "www.metaweather.com"
ENDPOINT = "/api/location/"

# -- For the location we have to use the
# -- Were on earth identifier
PLACE = input("Please enter the name of the city you're looking for: ")
METHOD = "GET"

def woeid_lookup(PLACE):

    # -- API information
    HOSTNAME = "www.metaweather.com"
    ENDPOINT = "/api/location/search/?query="

    # -- Here we can define special headers if needed
    headers = {'User-Agent': 'http-client'}

    # -- Connect to the server
    # -- NOTICE it is an HTTPS connection!
    # -- If we do not specify the port, the standar one
    # -- will be used
    conn = http.client.HTTPSConnection(HOSTNAME)

    # -- Send the request. No body (None)
    # -- Use the defined headers
    conn.request(METHOD, ENDPOINT + PLACE , None, headers)
    # -- Wait for the server's response
    r1 = conn.getresponse()

    # -- Read the response's body and close
    # -- the connection
    text_json = r1.read().decode("utf-8")
    conn.close()

    # -- Generate the object from the json file
    search_woeid = json.loads(text_json)

    if len(search_woeid) == 0:
        return False

    else:
        LOCATION_WOEID = str(search_woeid[0]['woeid'])

        return LOCATION_WOEID

if woeid_lookup(PLACE):

    LOCATION_WOEID = woeid_lookup(PLACE)

    # -- Here we can define special headers if needed
    headers = {'User-Agent': 'http-client'}

    # -- Connect to the server
    # -- NOTICE it is an HTTPS connection!
    # -- If we do not specify the port, the standar one
    # -- will be used
    conn = http.client.HTTPSConnection(HOSTNAME)

    # -- Send the request. No body (None)
    # -- Use the defined headers
    conn.request(METHOD, ENDPOINT + LOCATION_WOEID + '/', None, headers)

    # -- Wait for the server's response
    r1 = conn.getresponse()

    # -- Print the status
    print()
    print("Response received: ", end='')
    print(r1.status, r1.reason)

    # -- Read the response's body and close
    # -- the connection
    text_json = r1.read().decode("utf-8")
    conn.close()

    # -- Optionally you can print the
    # -- received json file for testing
    # print(text_json)

    # -- Generate the object from the json file
    weather = json.loads(text_json)

    # -- Get the data
    time = weather['time']

    temp0 = weather['consolidated_weather'][0]
    sunset = weather['sun_set']
    temp = temp0['the_temp']
    place = weather['title']

    print()
    print("Place: {}".format(place))
    print("Time: {}".format(time))
    print("Sunset time: {}".format(sunset))
    print("Current temp: {} degrees".format(temp))

else:
    print("ERROR")
