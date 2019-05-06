import http.client
import json
from Seq import Seq

#Port and server
PORT = 8004
SERVER = 'rest.ensembl.org'

conn = http.client.HTTPConnection(SERVER, PORT)

conn.request("GET", "/homology/symbol/human/FRAT1?content-type=application/json")
r1 = conn.getresponse()
print("Response received!: {} {}\n".format(r1.status, r1.reason))

information = r1.read().decode("utf-8")

response = json.loads(information)

id=response['data'][0]['id']

conn.request("GET", "/sequence/id/"+id+"?content-type=application/json")
r1 = conn.getresponse()

information=r1.read().decode("utf-8")

response = json.loads(information)
print(response)

seq=response['seq']

s1= Seq(seq)

# Get the total number of basis
print("The number of the total T bases in the sequence is:", len(seq))


# Get the number of T nucleotids
print ("Number of bases of T:", s1.count('T'))

# Get the most repeated DNA base and its percentage
if s1.count('A')>s1.count('T') and s1.count('A')>s1.count('G') and s1.count('A')>s1.count('C'):
    print("A is the most abundant nucleotid, which appears: ",s1.count('A')," times and his percentage is",s1.perc('A'),"%")
elif s1.count('C')>s1.count('T') and s1.count('C')>s1.count('G') and s1.count('C')>s1.count('A'):
    print("C is the most abundant nucleotid, which appears: ",s1.count('C'),"times and his percentage is",s1.perc('C'),"%")
elif s1.count('T')>s1.count('A') and s1.count('T')>s1.count('G') and s1.count('T')>s1.count('C'):
    print("T is the most abundant nucleotid, which appears: ",s1.count('T'),"times and his percentage is",s1.perc('T'),"%")
elif s1.count('G')>s1.count('T') and s1.count('G')>s1.count('A') and s1.count('G')>s1.count('C'):
    print("G is the most abundant nucleotid, which appears: ",s1.count('G'),"times and his percentage is",s1.perc('G'),"%")


#Percentage al nucleotids
print ("Percentage of T nucleotids: ", s1.perc('T'),"%")
print ("Percentage of A nucleotids: ", s1.perc('A'),"%")
print ("Percentage of C nucleotids: ", s1.perc('C'),"%")
print ("Percentage of G nucleotids: ", s1.perc('G'),"%")