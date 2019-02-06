from Bases import count_bases

# Main program

s1 = input("Enter the sequence 1: ")
s2 = input("Enter the sequence 2: ")
sequences = [s1, s2]


for i in range(len(sequences)):
    base_dict = count_bases(sequences[i])
    for k, v in base_dict.items():
        print("The are {} {}s in the sequence".format(v, k))
    tl = len(sequences[i])
    print("This sequence", i+1 ,"is {} bases in length".format(tl))
