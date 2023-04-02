from coordonnees import Coordonnees
from rectangle import Rectangle

class Entity:
    def __init__(self, game):
        self.coordonnees =  Coordonnees(game, 0 ,0)
        self.HEIGHT = game.TILE_SIZE
        self.WIDTH = game.TILE_SIZE
        self.SPEED = 5
        self.direction = None
        self.sprite_counter = 0
        self.sprite_num = 0
        self.image = None
        self.solid_area = Rectangle()
        self.collision_on = False