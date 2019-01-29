with open("CPLX2.txt", "r") as f:
    seq = ""
    for line in f:
        if ">" in line:
            print(line)
            continue
        else:
            seq = seq + line
    f.close()

print("The number of A aminoacids is: ", seq.count("A"))
print("The number of C aminoacids is: ", seq.count("C"))
print("The number of G aminoacids is: ", seq.count("G"))
print("The number of T aminoacids is: ", seq.count("T"))
