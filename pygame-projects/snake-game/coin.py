import random
from object import Object
from config import grid_size, tile_width, tile_height, number_of_rocks
from rock import Rock

class Coin(Object):
    def __init__(self):
        self.colour = (255,255,0)
        self.position = [(random.randint(0, grid_size) * tile_width), (random.randint(0, grid_size) * tile_height)]

    
    def spawn_coin(self, rocks):
        self.position = [(random.randint(0, grid_size) * tile_width), (random.randint(0, grid_size) * tile_height)]
        rocks_pos = []
        for rock in rocks:
            rocks_pos.append(rock.position)
        if self.position in rocks_pos:
            self.spawn_coin(rocks)
    
    def hit_coin(self, snake, rocks):
        if self.position == snake.get_head_position():
            snake.gain_point()
            self.spawn_coin(rocks)
            for i in range(snake.length):
                rocks.append(Rock())
            for rock in rocks:
                rock.spawn_rock()
            

    def draw_coin(self, screen):
        self.draw_rect(screen, self.position, self.colour)