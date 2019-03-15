# An object class for the aminoacid sequences with several operations and calculations


class Seq:

    def __init__(self, strbases):

        self.strbases = strbases

    def len(self):
        lenght = len(self.strbases)
        return lenght

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
