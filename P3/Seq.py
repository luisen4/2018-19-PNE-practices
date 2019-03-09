# An object class for the aminoacid sequences with several operations and calculations


class Seq:

    def __init__(self, strbases):

        self.strbases = strbases

    def len(self):
        lenght = len(self.strbases)
        return lenght

    def complement(self):

        dict_comp = {"A": "T", "C": "G", "G": "C", "T": "A"}
        comp = ""
        for i in self.strbases:
            comp += dict_comp[i]
        return Seq(comp)

    def reverse(self):
        r = self.strbases[::-1]
        return Seq(r)

    def count(self, base):
        c = self.strbases.count(base)
        return c

    def perc(self, base):

        if self.len() > 0:
            perc = (round(100.0 * self.strbases.count(base) / self.len(), 1))
            return perc
        else:
            perc = 0
            return perc
