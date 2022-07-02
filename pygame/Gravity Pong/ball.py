import pygame
from physics_object import PhysicsObject

class Ball(PhysicsObject):
    def goal_collision(self, screen, game):
        if self.rect.x < 0:
            self.position[0] = 700
            self.position[1] = 100
            self.velocity[0] = 4
            self.velocity[1] = 4
            game.rplayer_score += 1
        if self.rect.x > screen.get_width():
            self.position[0] = (screen.get_width() / 2) - 12.5
            self.position[1] = 100
            self.velocity[0] = -4
            game.lplayer_score += 4

    def ball_bounce(self, screen):
        bottom_boundary = screen.get_height()
        # top boundary
        if self.rect.top <= 0 or self.rect.bottom >= bottom_boundary:
            self.direction.y *= -1
