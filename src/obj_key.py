from object import Object

import pygame, os

class OBJ_Key(Object):
    def __init__(self, game):
        Object.__init__(self, game)
        self.name = "Key"
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("res",os.path.join("sprite",os.path.join("player","back_walking_1.png")))).convert_alpha(), (self.PLAYER_HEIGHT,self.PLAYER_WIDTH))