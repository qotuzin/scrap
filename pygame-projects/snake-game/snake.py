from curses import newpad
import pygame as pg, random
from config import tile_height, tile_width, screen_height, screen_width
from object import Object

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake(Object):
    def __init__(self):
        self.reset()
        self.colour = (255,255,255)
    
    def reset(self):
        self.length = 1
        self.positions = [((screen_width / 2), (screen_height / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
    
    def get_head_position(self):
        return self.positions[0]

    def move(self):
        current_pos = self.positions[0]
        x, y = self.direction
        new_pos = [(current_pos[0] + x*tile_width), (current_pos[1] + y*tile_height)]
        if new_pos[0] >= screen_width:
            new_pos[0] = 0
        if new_pos[0] < 0:
            new_pos[0] = screen_width - tile_width
        if new_pos[1] >= screen_height:
            new_pos[1] = 0
        if new_pos[1] < 0:
            new_pos[1] = screen_height - tile_height
        if self.length > 2 and new_pos in self.positions:
            self.reset()
        else:
            self.positions.insert(0, new_pos)
            if len(self.positions) > self.length:
                self.positions.pop()

    def gain_point(self):
        self.length += 1
    
    def draw_snake(self, screen):
        for pos in self.positions:
            self.draw_rect(screen, pos, self.colour)