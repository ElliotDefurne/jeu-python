from coordonnees import Coordonnees

class Object:
    def __init__(self, game):
        self.image = None
        self.game = game
        self.name = ""
        self.boolean = False
        self.coordonnees = Coordonnees()