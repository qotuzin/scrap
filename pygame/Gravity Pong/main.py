#  import libraries
import pygame as pg
from game import Game
from menu import Menu
from debug import debug

pg.display.set_caption("Gravity Pong")
icon = pg.image.load('icon.png')
pg.display.set_icon(icon)

# define loop variables
g = Game()
m = Menu(g)

# MAIN LOOP
while g.running:
    m.main_menu()
    g.game_loop()
