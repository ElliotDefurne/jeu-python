import pygame, time

from audio import Audio
from player import Player
from coordonnees import Coordonnees
from game import Game
from tilemanager import TileManager
from tile import Tile


pygame.init()

game = Game()
game.tilemanager.load_map()

timer = 0
delta = 0
count = 0
interval = 1000000000 / game.FPS
last_time = time.time_ns()
current_time = None

while game.running:
    current_time = time.time_ns()
    delta += (current_time - last_time) / interval
    timer += (current_time - last_time)
    last_time = current_time

    if(delta >= 1):
        
        game.update()

        delta = 0
        count += 1
        
    if(timer >= 1000000000):
        print(f"FPS : {count}")
        print(f"({game.player.coordonnees.x};{game.player.coordonnees.y})")
        count = 0
        timer = 0

    #DRAW

    game.draw()
    pygame.display.update()
    
pygame.quit()