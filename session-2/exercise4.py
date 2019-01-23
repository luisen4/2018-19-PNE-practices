seq = input("Please introduce a valid sequence of aminoacids: ").upper()

count_letters= [0, 0, 0, 0]
# The counter stores information about the aminoacids A, C, T, G in that order
letters = ["A", "C", "T", "G"]

for s in seq:
    if s == "A":
        count_letters[0] += 1
    elif s == "C":
        count_letters[1] += 1
    elif s == "T":
        count_letters[2] += 1
    else:
        count_letters[3] += 1

print("The total lenght is:", len(seq))

results = zip(letters, count_letters)
for l, c in results:
    print("The letter", l, "appears: ", c, "times")