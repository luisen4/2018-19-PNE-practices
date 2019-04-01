# Example of getting information stored in github

import http.client
import json

# -- API information
HOSTNAME = "api.github.com"
ENDPOINT_1 = "/users/"
ENDPOINT_2 = "/repos"
ENDPOINT_3 = "/stats/contributors"
GITHUB_ID = input("Please choose the user you want to look for: ")
METHOD = "GET"

# -- Here we can define special headers if needed
headers = {'User-Agent': 'http-client'}


def get_name(GITHUB_ID):

    # -- Connect to the server
    # -- NOTICE it is an HTTPS connection!
    # -- If we do not specify the port, the standar one
    # -- will be used
    conn = http.client.HTTPSConnection(HOSTNAME)

    # -- Send the request. No body (None)
    # -- Use the defined headers
    conn.request(METHOD, ENDPOINT_1 + GITHUB_ID, None, headers)

    # -- Wait for the server's response
    r1 = conn.getresponse()

    # -- Print the status
    print()
    print("Response received: ", end='')
    print(r1.status, r1.reason)

    # -- Read the response's body and close
    # -- the connection
    text_json_1 = r1.read().decode("utf-8")
    conn.close()

    return text_json_1


def get_repos(GITHUB_ID):

    # -- Connect to the server
    # -- NOTICE it is an HTTPS connection!
    # -- If we do not specify the port, the standar one
    # -- will be used
    conn = http.client.HTTPSConnection(HOSTNAME)

    # -- Send the request. No body (None)
    # -- Use the defined headers
    conn.request(METHOD, ENDPOINT_1 + GITHUB_ID + ENDPOINT_2, None, headers)

    # -- Wait for the server's response
    r2 = conn.getresponse()

    # -- Print the status
    print()
    print("Response received: ", end='')
    print(r2.status, r2.reason)

    # -- Read the response's body and close
    # -- the connection
    text_json_2 = r2.read().decode("utf-8")
    conn.close()

    return text_json_2


def get_commits(GITHUB_ID):

    REPO_NAME = "/2018-19-PNE-practices"
    # -- Connect to the server
    # -- NOTICE it is an HTTPS connection!
    # -- If we do not specify the port, the standar one
    # -- will be used
    conn = http.client.HTTPSConnection(HOSTNAME)

    # -- Send the request. No body (None)
    # -- Use the defined headers
    conn.request(METHOD, ENDPOINT_2 + "/" + GITHUB_ID + REPO_NAME + ENDPOINT_3, None, headers)

    # -- Wait for the server's response
    r3 = conn.getresponse()

    # -- Print the status
    print()
    print("Response received: ", end='')
    print(r3.status, r3.reason)

    # -- Read the response's body and close
    # -- the connection
    text_json_3 = r3.read().decode("utf-8")
    conn.close()

    return text_json_3


text_json_1 = get_name(GITHUB_ID)
text_json_2 = get_repos(GITHUB_ID)
text_json_3 = get_commits(GITHUB_ID)

# -- Generate the object from the json file
user_name = json.loads(text_json_1)
user_repos = json.loads(text_json_2)
user_commits = json.loads(text_json_3)

# -- Collect the name of all the repositories
repository_names = []
for dicts in user_repos:
    repository_names.append(dicts['name'])

# -- Get some data
commits = ""
for dicts in user_commits:
    commits = dicts['total']

name = user_name['name']

print("Name: {}".format(name))
print("Repositories: {}".format(','.join(n for n in repository_names)))
print("Total commits in 2018-19-PNE-practices: {}".format(commits))
