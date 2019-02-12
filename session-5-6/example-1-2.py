from Bases import count_bases

# Main program

s = input("Please enter a valid sequence of aminoacids: ")
na = count_bases(s)

for k, v in na.items():
    print("The are {} {}s in the sequence".format(v, k))