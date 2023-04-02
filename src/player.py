from pile import Pile
from coordonnees import Coordonnees
from entity import Entity
from rectangle import Rectangle

import pygame, os

class Player(Entity):
    def __init__(self, game, movable = True):
        Entity.__init__(self, game)

        self.PLAYER_HEIGHT = game.TILE_SIZE
        self.PLAYER_WIDTH = game.TILE_SIZE
        self.SCREEN_X = game.SCREEN_WIDTH // 2 - self.PLAYER_WIDTH//2
        self.SCREEN_Y = game.SCREEN_HEIGHT // 2 - self.PLAYER_HEIGHT//2

        self.game = game
        self.coordonnees =  Coordonnees(game, 0 ,0)
        self.last_frame_pos = Coordonnees(game, 0 ,0)
        self.solid_area = Rectangle(self.game.TILE_SIZE//4,self.game.TILE_SIZE//2,self.game.TILE_SIZE//2,self.game.TILE_SIZE//2)
        self.movable = movable
        self.direction = "South"
        self.moving_north = False
        self.moving_south = False
        self.moving_west = False
        self.moving_east = False

        self.directions = Pile()

        self.set_default_values()
        self.load_images()

    def set_default_values(self):
        self.coordonnees.x = 0
        self.coordonnees.y = 0
    
    def load_images(self):
        self.front = pygame.transform.scale(pygame.image.load(os.path.join("res",os.path.join("sprite",os.path.join("player","front.png")))).convert_alpha(), (self.PLAYER_HEIGHT,self.PLAYER_WIDTH))
        self.front_walking_1 = pygame.transform.scale(pygame.image.load(os.path.join("res",os.path.join("sprite",os.path.join("player","front_walking_1.png")))).convert_alpha(), (self.PLAYER_HEIGHT,self.PLAYER_WIDTH))
        self.front_walking_2 = pygame.transform.scale(pygame.image.load(os.path.join("res",os.path.join("sprite",os.path.join("player","front_walking_2.png")))).convert_alpha(), (self.PLAYER_HEIGHT,self.PLAYER_WIDTH))
        self.front_walking_3 = pygame.transform.scale(pygame.image.load(os.path.join("res",os.path.join("sprite",os.path.join("player","front_walking_3.png")))).convert_alpha(), (self.PLAYER_HEIGHT,self.PLAYER_WIDTH))
        self.back = pygame.transform.scale(pygame.image.load(os.path.join("res",os.path.join("sprite",os.path.join("player","back.png")))).convert_alpha(), (self.PLAYER_HEIGHT,self.PLAYER_WIDTH))
        self.back_walking_1 = pygame.transform.scale(pygame.image.load(os.path.join("res",os.path.join("sprite",os.path.join("player","back_walking_1.png")))).convert_alpha(), (self.PLAYER_HEIGHT,self.PLAYER_WIDTH))
        self.back_walking_2 = pygame.transform.scale(pygame.image.load(os.path.join("res",os.path.join("sprite",os.path.join("player","back_walking_2.png")))).convert_alpha(), (self.PLAYER_HEIGHT,self.PLAYER_WIDTH))
        self.back_walking_3 = pygame.transform.scale(pygame.image.load(os.path.join("res",os.path.join("sprite",os.path.join("player","back_walking_3.png")))).convert_alpha(), (self.PLAYER_HEIGHT,self.PLAYER_WIDTH))
        self.left = pygame.transform.scale(pygame.image.load(os.path.join("res",os.path.join("sprite",os.path.join("player","left.png")))).convert_alpha(), (self.PLAYER_HEIGHT,self.PLAYER_WIDTH))
        self.left_walking_1 = pygame.transform.scale(pygame.image.load(os.path.join("res",os.path.join("sprite",os.path.join("player","left_walking_1.png")))).convert_alpha(), (self.PLAYER_HEIGHT,self.PLAYER_WIDTH))
        self.left_walking_2 = pygame.transform.scale(pygame.image.load(os.path.join("res",os.path.join("sprite",os.path.join("player","left_walking_2.png")))).convert_alpha(), (self.PLAYER_HEIGHT,self.PLAYER_WIDTH))
        self.left_walking_3 = pygame.transform.scale(pygame.image.load(os.path.join("res",os.path.join("sprite",os.path.join("player","left_walking_3.png")))).convert_alpha(), (self.PLAYER_HEIGHT,self.PLAYER_WIDTH))
        self.right = pygame.transform.scale(pygame.image.load(os.path.join("res",os.path.join("sprite",os.path.join("player","right.png")))).convert_alpha(), (self.PLAYER_HEIGHT,self.PLAYER_WIDTH))
        self.right_walking_1 = pygame.transform.scale(pygame.image.load(os.path.join("res",os.path.join("sprite",os.path.join("player","right_walking_1.png")))).convert_alpha(), (self.PLAYER_HEIGHT,self.PLAYER_WIDTH))
        self.right_walking_2 = pygame.transform.scale(pygame.image.load(os.path.join("res",os.path.join("sprite",os.path.join("player","right_walking_2.png")))).convert_alpha(), (self.PLAYER_HEIGHT,self.PLAYER_WIDTH))
        self.right_walking_3 = pygame.transform.scale(pygame.image.load(os.path.join("res",os.path.join("sprite",os.path.join("player","right_walking_3.png")))).convert_alpha(), (self.PLAYER_HEIGHT,self.PLAYER_WIDTH))


    def move_up(self):
        if self.movable:
            self.coordonnees.move_up(self.SPEED)

    def move_down(self):
        if self.movable:
            self.coordonnees.move_down(self.SPEED)

    def move_left(self):
        if self.movable:
            self.coordonnees.move_left(self.SPEED)

    def move_right(self):
        if self.movable:
            self.coordonnees.move_right(self.SPEED)

    def get_direction(self):
        return self.directions.get_last()
    
    def enlever_doublon(self):
        temp = Pile()
        for elt in self.directions.pile:
            temp.stack(elt)
        if temp.elt_in_list("North") and temp.elt_in_list("South"):
            temp.remove("North")
            temp.remove("South")
        if temp.elt_in_list("West") and temp.elt_in_list("East"):
            temp.remove("West")
            temp.remove("East")
        return temp
    
    def moving(self):
        return not(self.enlever_doublon().is_empty())
    
    def draw_collision(self):
        self.solid_area.draw(self.game)

    def draw_border(self):
        rect = Rectangle(self.SCREEN_X,self.SCREEN_Y, self.PLAYER_WIDTH, self.PLAYER_HEIGHT)
        rect.draw()
    
    def tp_center_on_coordinates(self, coordonnees):
        self.coordonnees.x = coordonnees.x
        self.coordonnees.y = coordonnees.y

    def update(self):
        if self.moving():
            if self.enlever_doublon().get_last() == "North":
                self.direction = "North"
            elif self.enlever_doublon().get_last() == "South":
                self.direction = "South"
            elif self.enlever_doublon().get_last() == "West":
                self.direction = "West"
            elif self.enlever_doublon().get_last() == "East":
                self.direction = "East"

            # Vérifie les collisions

            self.collision_on = False
            try:
                self.game.collisionchecker.check_tile(self)
            except:
                self.game.player.tp_center_on_coordinates(Coordonnees(self.game, self.game.WORLD_WIDTH//2, self.game.WORLD_HEIGHT//2))
            
            # Si la collision est fausse, il peut bouger
            if(self.collision_on == False):
                if(self.direction == "North"): self.move_up()
                elif(self.direction == "West"): self.move_left()
                elif(self.direction == "East"): self.move_right()
                elif(self.direction == "South"): self.move_down()
                
            self.sprite_counter += 1
            if(self.sprite_counter > 10):
                self.sprite_num += 1
                if(self.sprite_num == 4):
                    self.sprite_num = 0
                self.sprite_counter = 0
        else:
            self.sprite_num = 0
        self.draw_collision()
        self.last_frame_pos = Coordonnees(self.game, self.coordonnees.x, self.coordonnees.y)


    def draw(self):
        if self.direction == "North":
            if self.sprite_num == 0:
                self.image = self.back
            elif self.sprite_num == 1:
                self.image = self.back_walking_1
            elif self.sprite_num == 2:
                self.image = self.back_walking_2
            elif self.sprite_num == 3:
                self.image = self.back_walking_3
        if self.direction == "South":
            if self.sprite_num == 0:
                self.image = self.front
            elif self.sprite_num == 1:
                self.image = self.front_walking_1
            elif self.sprite_num == 2:
                self.image = self.front_walking_2
            elif self.sprite_num == 3:
                self.image = self.front_walking_3
        if self.direction == "East":
            if self.sprite_num == 0:
                self.image = self.right
            elif self.sprite_num == 1:
                self.image = self.right_walking_1
            elif self.sprite_num == 2:
                self.image = self.right_walking_2
            elif self.sprite_num == 3:
                self.image = self.right_walking_3
        if self.direction == "West":
            if self.sprite_num == 0:
                self.image = self.left
            elif self.sprite_num == 1:
                self.image = self.left_walking_1
            elif self.sprite_num == 2:
                self.image = self.left_walking_2
            elif self.sprite_num == 3:
                self.image = self.left_walking_3
        
        self.game.screen.blit(self.image, (self.SCREEN_X,self.SCREEN_Y)) # Dessine le sprite