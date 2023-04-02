from entity import Entity

class Collisionchecker:
    def __init__(self, game):
        self.game = game
    def check_tile(self, entity):
        assert -1*(entity.solid_area.height//2) < entity.coordonnees.x and -1*(entity.solid_area.width//2) < entity.coordonnees.y, "Les coordonnées doivent être positive."

        entity_left_world_x = entity.coordonnees.x + entity.solid_area.x
        entity_right_world_x = entity.coordonnees.x + entity.solid_area.x + entity.solid_area.width
        entity_top_world_y = entity.coordonnees.y + entity.solid_area.y
        entity_bottom_world_y = entity.coordonnees.y + entity.solid_area.y + entity.solid_area.height

        entity_left_col = entity_left_world_x//self.game.TILE_SIZE
        entity_right_col = entity_right_world_x//self.game.TILE_SIZE
        entity_top_row = entity_top_world_y//self.game.TILE_SIZE
        entity_bottom_row = entity_bottom_world_y//self.game.TILE_SIZE

        tile_num_1 = None
        tile_num_2 = None

        if(entity.direction == "North"):
            entity_top_row = (entity_top_world_y - entity.SPEED)//self.game.TILE_SIZE
            tile_num_1 = self.game.tilemanager.map_tile_num[entity_top_row][entity_right_col]
            tile_num_2 = self.game.tilemanager.map_tile_num[entity_top_row][entity_left_col]
            if(self.game.tilemanager.tile[tile_num_1].collision == True or self.game.tilemanager.tile[tile_num_2].collision == True):
                entity.collision_on = True

        elif(entity.direction == "West"):
            entity_left_col = (entity_left_world_x - entity.SPEED)//self.game.TILE_SIZE
            tile_num_1 = self.game.tilemanager.map_tile_num[entity_top_row][entity_left_col]
            tile_num_2 = self.game.tilemanager.map_tile_num[entity_bottom_row][entity_left_col]
            if(self.game.tilemanager.tile[tile_num_1].collision == True or self.game.tilemanager.tile[tile_num_2].collision == True):
                entity.collision_on = True

        elif(entity.direction == "East"):
            entity_right_col = (entity_right_world_x + entity.SPEED)//self.game.TILE_SIZE
            tile_num_1 = self.game.tilemanager.map_tile_num[entity_top_row][entity_right_col]
            tile_num_2 = self.game.tilemanager.map_tile_num[entity_bottom_row][entity_right_col]
            if(self.game.tilemanager.tile[tile_num_1].collision == True or self.game.tilemanager.tile[tile_num_2].collision == True):
                entity.collision_on = True

        elif(entity.direction == "South"):
            entity_bottom_row = (entity_bottom_world_y + entity.SPEED)//self.game.TILE_SIZE
            tile_num_1 = self.game.tilemanager.map_tile_num[entity_bottom_row][entity_right_col]
            tile_num_2 = self.game.tilemanager.map_tile_num[entity_bottom_row][entity_left_col]
            if(self.game.tilemanager.tile[tile_num_1].collision == True or self.game.tilemanager.tile[tile_num_2].collision == True):
                entity.collision_on = True
