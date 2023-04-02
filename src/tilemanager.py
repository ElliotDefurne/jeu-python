from tile import Tile
from coordonnees import Coordonnees

import os, pygame

class TileManager:
    def __init__(self, game):
        self.game = game
        self.tile = []
        self.map_tile_num = []
        self.path = path = os.path.join("res",os.path.join("map","map1.txt"))
        self.get_tile_images()
        print(self.load_file())


    def get_tile_images(self):

        image0 = pygame.transform.scale(pygame.image.load(os.path.join("res",os.path.join("tiles","dirt.png"))).convert_alpha(), (self.game.TILE_SIZE,self.game.TILE_SIZE))
        self.tile += [Tile("dirt", image0)]

        image1 = pygame.transform.scale(pygame.image.load(os.path.join("res",os.path.join("tiles","grass.png"))).convert_alpha(), (self.game.TILE_SIZE,self.game.TILE_SIZE))
        self.tile += [Tile("grass", image1)]

        image2 = pygame.transform.scale(pygame.image.load(os.path.join("res",os.path.join("tiles","water.png"))).convert_alpha(), (self.game.TILE_SIZE,self.game.TILE_SIZE))
        self.tile += [Tile("water", image2, True)]
        

        image3 = pygame.transform.scale(pygame.image.load(os.path.join("res",os.path.join("tiles","bricks.png"))).convert_alpha(), (self.game.TILE_SIZE,self.game.TILE_SIZE))
        self.tile += [Tile("bricks", image1, True)]

    def load_file(self):
        with open(self.path) as file:
            tab = []
            for lines in file.readlines():
                line = []
                for caracter in lines:
                    if caracter.isdigit():
                        line += [int(caracter)]
                tab += [line]
        return tab
    
    def load_map(self):
        file = self.load_file()
        max_world_col = len(file)
        max_world_row = len(file[0])
        self.map_tile_num = file
        return max_world_row, max_world_col

    def draw(self):
        world_col = 0
        world_row = 0
        for lines in self.map_tile_num:
            for num in lines:
                num = int(num)
                world_x = world_col * self.game.TILE_SIZE
                world_y = world_row * self.game.TILE_SIZE
                screen_x = world_x - self.game.player.coordonnees.x + self.game.player.SCREEN_X
                screen_y = world_y - self.game.player.coordonnees.y + self.game.player.SCREEN_Y

                coordonnees = Coordonnees(self.game, screen_x, screen_y)
                if coordonnees.tile_visible():
                    image = self.tile[num].image
                    self.game.screen.blit(image,(screen_x, screen_y))
                world_col += 1
            world_col = 0
            world_row += 1
