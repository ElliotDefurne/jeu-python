class Pile:
    def __init__(self):
        self.pile = []

    def __repr__(self):
        return str(self.pile)
    
    def is_empty(self):
        return self.pile == []
    
    def stack(self, elt):
        self.pile += [elt]

    def unstack(self):
        return self.pile.pop()
    
    def remove(self, elt):
        if elt in self.pile:
            self.pile.remove(elt)

    def get_last(self):
        return self.pile[-1]
    
    def elt_in_list(self, elt):
        return elt in self.pile