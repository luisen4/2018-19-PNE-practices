sequence = input("Please enter a valid sequence of aminoacids: ").upper()

counters = [0, 0, 0, 0]
#counters storages information about the number of aminoacids A, C, G, T in this order.
letters = ["A", "C", "G", "T"]

for s in sequence:
    if s == "A":
        counters[0] += 1
    elif s == "C":
        counters[1] += 1
    elif s == "G":
        counters[2] += 1
    else:
        counters[3] += 1

print("The lenght of the sequence is:", len(sequence))
info = zip(letters, counters)
for l, c in info:
    print("The letter", l, "appears: ", c, "times.")