import pygame
from physics_object import PhysicsObject

class Player(PhysicsObject):
    def __init__(self, img, init_x, init_y, init_dx, init_dy, mass, gravity, speed):
        PhysicsObject.__init__(self, img, init_x, init_y, init_dx, init_dy, mass, gravity)
        self.speed = speed  # how many pixels moved each update (tick)

    def control_player(self, UP_KEY, DOWN_KEY, LEFT_KEY=None, RIGHT_KEY=None):
        if LEFT_KEY:
            self.direction.x = -1
        elif RIGHT_KEY:
            self.direction.x = 1
        elif UP_KEY:
            self.direction.y = -1
        elif DOWN_KEY:
            self.direction.y = 1
        else:
            self.direction.x = 0
            self.direction.y = 0