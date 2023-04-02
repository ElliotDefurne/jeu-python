class Coordonnees:
    def __init__(self, game = None, x = 0, y = 0):
        self.x = x
        self.y = y
        self.game = game
        self.SCREEN_WIDTH = game.SCREEN_DIMENSIONS[0]
        self.SCREEN_HEIGHT = game.SCREEN_DIMENSIONS[1]

    def move_up(self, y):
        self.y -= y

    def move_down(self, y):
        self.y += y

    def move_right(self, x):
        self.x += x

    def move_left(self, x):
        self.x -= x

    def get_coordinates_center(self, entity):
        return Coordonnees(self.game, entity.coordonnees.x+entity.height//2, entity.coordonnees.y+entity.width//2)

    def on_map(self):
        return (0<=self.x and self.x<=self.game.WORLD_WIDTH) and (0<=self.y and self.y<=self.game.WORLD_HEIGHT)
    
    def tile_visible(self):
        return True
    
    def __repr__(self):
        return f"({self.x}; {self.y})"