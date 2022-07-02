import pygame as pg, sys
from config import *
from ball import Ball

pg.init()

screen = pg.display.set_mode(screen_size)
background = pg.surface.Surface(screen_size)
background.fill(background_colour)

clock = pg.time.Clock()

ball = Ball(ball_speed)

GAME_RUN = True
if __name__ == '__main__':
    while GAME_RUN:
        for event in pg.event.get():
            if event.type == pg.QUIT: pg.quit(); sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE: pg.quit(); sys.exit()

        ball.check_boundary_collision()
        ball.update()

        screen.blit(background, (0,0))
        ball.draw_ball(screen)

        pg.display.update()

        clock.tick(FPS)



