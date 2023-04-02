import pygame

class Rectangle:
    def __init__(self, x = None, y = None, width = None, height = None):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
    def draw(self, game):
        rect = pygame.Rect(self.x,self.y, self.width, self.height)
        color = (0,0,0)
        pygame.draw.rect(game.screen, color, rect, 2)