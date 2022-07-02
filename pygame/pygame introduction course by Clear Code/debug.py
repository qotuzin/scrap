import pygame
import numpy

pygame.init()
font = pygame.font.Font(None,20)

def debug(info, y=10, x=10):
    # create some text
    display_surf = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, 'white')
    # create a rectangle in a position
    debug_rect = debug_surf.get_rect(topleft = (x, y))
    # blit everything
    display_surf.blit(debug_surf, debug_rect)

def kinematics_info(object, screen, arrows=False):
        debug("Position = {}".format(object.position), object.position[1] + 25, object.position[0])
        debug("Velocity = {}".format(object.velocity), object.position[1] + 40, object.position[0])
        debug("Acceleration = {}".format(object.acceleration), object.position[1] + 55, object.position[0])

        if arrows:
            draw_vector_arrow(object.acceleration, object, screen, (255,255,0), 50)
            draw_vector_arrow(object.velocity, object, screen, (0, 255, 0), 50)

def draw_vector_arrow(vector, object, screen, colour, multiplier):
    direction = vector / numpy.linalg.norm(vector)
    pygame.draw.line(screen, colour, (object.rect.x + 12, object.rect.y + 12),(multiplier * direction[0] + object.rect.x,multiplier * direction[1] + object.rect.y), 6)
