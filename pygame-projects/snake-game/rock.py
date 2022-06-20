import random
from object import Object
from config import grid_size, tile_width, tile_height

class Rock(Object):
    def __init__(self):
        self.colour = (255,0,255)
        self.position = [0,0]
        self.spawn_rock()
    
    def spawn_rock(self):
        self.position = [(random.randint(0, grid_size) * tile_width), (random.randint(0, grid_size) * tile_height)]
    
    def hit_rock(self, snake, coin, rocks):
        if self.position == snake.get_head_position():
            snake.reset()
            self.spawn_rock()
            coin.spawn_coin(rocks)
            

    def draw_rock(self, screen):
        self.draw_rect(screen, self.position, self.colour)