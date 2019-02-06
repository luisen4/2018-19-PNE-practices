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

    def count(base):
        c = self.strbase.count("base")
        return c

    def perc(base):

        if lenght > 0:
            perc = (round(100.0 * c / lenght, 1))
            return perc
        else:
            perc = 0
            return perc