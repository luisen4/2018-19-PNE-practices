def count_bases(seq):
    """Counting the number of bases in the string"""
    count_a = seq.count("A")
    count_t = seq.count("T")
    count_c = seq.count("C")
    count_g = seq.count("G")

    seq_dict = {"A": count_a, "T":count_t, "C": count_c, "G": count_g}
    return seq_dict

def calc_perc(dict):
    for k, v in dict.items():
        if v > 0:
            perc = (round(100.0 * v / tl, 1))
        else:
            perc = 0

        print("Base", k)
        print("Counter: ", v)
        print("Percentage: ", perc)

s = input("Enter the sequence: ")
base_dict = count_bases(s)
tl = len(s)

print("This sequence is {} bases in length".format(tl))
calc_perc(base_dict)