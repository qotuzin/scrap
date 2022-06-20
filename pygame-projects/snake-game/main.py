import sys, pygame as pg
from numpy import number
from config import *
from snake import Snake
from coin import Coin
from rock import Rock
pg.init() # initialise pygame


fps_clock = pg.time.Clock()

GAME_RUN = True
screen = pg.display.set_mode(screen_size)
background = pg.surface.Surface(screen_size)
background.fill(background_colour)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def game_reset():
    screen.fill(background_colour)
    snake.reset()


snake = Snake()
coin = Coin()
rocks = []
for i in range(snake.length):
    rocks.append(Rock())

# GAME LOOP
if __name__ == '__main__':
    while GAME_RUN:
        # EVENT LOOP
        for event in pg.event.get():
            if event.type == pg.QUIT: pg.quit(); sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE: pg.quit(); sys.exit()
                #Check for player movement input
                if event.key == pg.K_UP:
                    snake.direction = UP
                if event.key == pg.K_DOWN:
                    snake.direction = DOWN
                if event.key == pg.K_LEFT:
                    snake.direction = LEFT
                if event.key == pg.K_RIGHT:
                    snake.direction = RIGHT
                if event.key == pg.K_r:
                    game_reset()
                if event.key == pg.K_EQUALS:
                    snake.gain_point()

        # UPDATE CYCLE
        snake.move()

        coin.hit_coin(snake, rocks)

        # DRAW CYCLE
    # Draw everything to screen
        screen.blit(background, (0,0))

        snake.draw_snake(screen)
        coin.draw_coin(screen)
        for rock in rocks:
            rock.draw_rock(screen)
            rock.hit_rock(snake, coin, rocks)

        pg.display.update()

        fps_clock.tick(FPS) # set fps
