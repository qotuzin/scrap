from object import Object
import pygame as pg
from config import screen_height, screen_width, ball_radius

class Ball(Object):
    def __init__(self, speed):
        self.position = (screen_width/2,screen_height/2)
        self.speed = speed
        self.direction = [1,1]
    
    def check_boundary_collision(self):
        if self.position[0] + ball_radius >= screen_width or self.position[0] - ball_radius <= 0:
            self.direction[0] *= -1
        if self.position[1] + ball_radius >= screen_height or self.position[1] - ball_radius <= 0:
            self.direction[1] *= -1

    def update(self):
        self.position += self.speed * pg.Vector2(self.direction)
        print(self.position)

    def draw_ball(self, surf):
        pg.draw.circle(surf, (255,0,0), self.position, ball_radius)
