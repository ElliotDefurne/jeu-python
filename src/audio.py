import pygame

class Audio:
    def __init__(self, game, path):
        #Instantiate mixer
        pygame.mixer.init()
        pygame.mixer.music.set_volume(game.GAME_VOLUME)
        self.son = pygame.mixer.Sound(path)
    def stop(self):
        self.son.stop()
    def play(self):
        self.son.play()
