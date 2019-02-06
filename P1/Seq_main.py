from Seq import Seq

# Main program

s1 = Seq("AGTACACTGGT")
s2 = Seq("CGTAAC")

s3 = s1.complement()
s4 = s1.reverse()

sequences = [s1, s2, s3, s4]

for index in range (len(sequences)):
    pass