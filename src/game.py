from tilemanager import TileManager
from player import Player
from collisionchecker import Collisionchecker

import pygame, math

class Game:
    def __init__(self):
        self.K_Z = pygame.key.key_code("z")
        self.K_Q = pygame.key.key_code("q")
        self.K_S = pygame.key.key_code("s")
        self.K_D = pygame.key.key_code("d")

        self.ORIGINALE_TILE_SIZE = 64
        self.SCALE = 1
        self.TILE_SIZE = self.ORIGINALE_TILE_SIZE * self.SCALE
        self.SCREEN_HEIGHT = 720
        self.SCREEN_WIDTH = 1280
        self.MAX_SCREEN_COL = math.ceil(self.SCREEN_WIDTH // self.TILE_SIZE)
        self.MAX_SCREEN_ROW = math.ceil(self.SCREEN_HEIGHT // self.TILE_SIZE)
        self.SCREEN_DIMENSIONS = [self.SCREEN_WIDTH,self.SCREEN_HEIGHT]
        self.FPS = 60
        self.running = True

        self.screen = pygame.display.set_mode(self.SCREEN_DIMENSIONS)
        self.tilemanager = TileManager(self)
        self.MAX_WORLD_ROW , self.MAX_WORLD_COL = self.tilemanager.load_map()
        self.WORLD_WIDTH = self.TILE_SIZE * self.MAX_WORLD_COL
        self.WORLD_HEIGHT = self.TILE_SIZE * self.MAX_WORLD_ROW
        self.player = Player(self)
        self.collisionchecker = Collisionchecker(self)

        

    def update(self):
        keys = pygame.key.get_pressed()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == self.K_Z:
                    self.player.moving_north = True
                    self.player.directions.stack("North")
                if event.key == self.K_S:
                    self.player.moving_south = True
                    self.player.directions.stack("South")
                if event.key == self.K_Q:
                    self.player.moving_west = True
                    self.player.directions.stack("West")
                if event.key == self.K_D:
                    self.player.moving_east = True
                    self.player.directions.stack("East")
            if event.type == pygame.KEYUP:
                if event.key == self.K_Z:
                    self.player.moving_north = False
                    self.player.directions.remove("North")
                if event.key == self.K_S:
                    self.player.moving_south = False
                    self.player.directions.remove("South")
                if event.key == self.K_Q:
                    self.player.moving_west = False
                    self.player.directions.remove("West")
                if event.key == self.K_D:
                    self.player.moving_east = False
                    self.player.directions.remove("East")
        self.player.update()

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.tilemanager.draw()
        self.player.draw()