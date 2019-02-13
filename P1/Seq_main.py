from Seq import Seq

# Main program

s1 = Seq("AGTACACTGGT")
s2 = Seq("CGTAAC")

s3 = s1.complement()
s4 = s1.reverse()

sequences = [s1, s2, s3, s4]

for index in range(len(sequences)):
    print("Sequence {}: {}".format(index+1, sequences[index].strbases))
    print("Lenght: {}".format(sequences[index].len()))
    print("Bases count: A:{}, T:{}, C:{}, G:{}".format(sequences[index].count("A"), sequences[index].count("T"), sequences[index].count("C"), sequences[index].count("G")))
    print("Bases percentage: A:{}%, T:{}%, C:{}%, G:{}%".format(sequences[index].perc("A"), sequences[index].perc("T"), sequences[index].perc("C"), sequences[index].perc("G")))
    print("\n")
