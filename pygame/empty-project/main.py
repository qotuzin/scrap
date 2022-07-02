import sys
import pygame as pg
pg.init()

GAME_RUN = True
screen_size = width, height = 320, 240

screen = pg.display.set_mode(screen_size)


while GAME_RUN:
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
        
        pg.display.flip()
