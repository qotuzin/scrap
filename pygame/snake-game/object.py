import pygame as pg
from config import tile_height, tile_width

class Object(object):
    def __init__(self):
        pass

    def draw_rect(self, surf, pos, colour):
        rect = pg.rect.Rect(pos[0], pos[1], tile_width, tile_height)
        pg.draw.rect(surf, colour, rect)