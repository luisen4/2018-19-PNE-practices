def count_bases(seq):
    """Counting the number of bases in the string"""
    count_a = seq.count("A")
    count_t = seq.count("T")
    count_c = seq.count("C")
    count_g = seq.count("G")

    seq_dict = {"A": count_a, "T":count_t, "C": count_c, "G": count_g}
    return seq_dict