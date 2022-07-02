import pygame as pg
import numpy as np
import pygame.mask

class PhysicsObject(pg.sprite.Sprite):
    def __init__(self, img, init_x, init_y, speed, direction, mass, gravity):
        pg.sprite.Sprite.__init__(self) #initialise sprite class
        self.image = img #assign image of player as the 0th image of the player's image list
        self.rect = self.image.get_rect() #makes a rectangle which fits the dimensions of the player's sprite
        self.mask = pg.mask.from_surface(self.image)

        #physics object class variables
        self.rect.x = init_x
        self.rect.y = init_y
        self.position = pg.math.Vector2(self.rect.center)
        self.velocity = pg.math.Vector2([0, 0])
        self.speed = speed
        self.direction = pg.math.Vector2(direction)
        self.acceleration = pg.math.Vector2(0, 0)
        self.mass = mass
        self.gravity = gravity

    def boundary_collision(self, screen):
        bottom_boundary = screen.get_height()
        #top boundary
        if self.position.y < 0:
            self.direction.y = 0
            self.position.y = 0
        #bottom boundary
        if self.position.y > bottom_boundary - self.rect.height:
            self.direction.y = 0
            self.position.y = bottom_boundary - self.rect.height

    def gravity_calc(self, object2):
        radius = pg.math.Vector2([object2.rect.center[0] - self.rect.center[0], object2.rect.center[1] - self.rect.center[1]])
        distance = pg.math.Vector2.normalize(radius)
        direction = radius / distance
        acceleration_magnitude = object2.mass / distance ** 2 # calculate magnitude of acceleration
        acceleration = pg.math.Vector2([acceleration_magnitude * direction.x, acceleration_magnitude * direction.y])
        return acceleration

    def move(self, dt, gravity=None, gravity_well=None):
        if gravity == True:
            self.acceleration = self.gravity_calc(gravity_well)
        else:
            self.acceleration = 0
        print(self.velocity)
        #self.velocity += self.acceleration * dt
        self.position += self.direction * self.speed * dt
        self.rect.x = round(self.position.x)
        self.rect.y = round(self.position.y)
    #cap speed to maximum value
        """ max_speed = 10
        if self.velocity.x > max_speed:
            self.velocity.x = max_speed
        if self.velocity.y > max_speed:
            self.velocity.y = max_speed """

    def update_position(self):
        self.rect.x = round(self.position.x)
        self.rect.y = round(self.position.y)

    def object_rebound(self, object):
        if self.rect.colliderect(object):
            collision_tolerance = 10
            if abs(object.rect.right - self.rect.left) < collision_tolerance and self.velocity.x < 0:
                self.direction.x *= -1
            if abs(object.rect.left - self.rect.right) < collision_tolerance and self.velocity.x > 0:
                self.direction.x *= -1
            if abs(object.rect.bottom - self.rect.top) < collision_tolerance and self.velocity.y < 0:
                self.direction.y *= -1
            if abs(object.rect.top - self.rect.bottom) < collision_tolerance and self.velocity.y > 0:
                self.direction.y *= -1
    
    def update(self, dt, gravity=None, gravity_well=None):
        self.move(dt, gravity, gravity_well)
