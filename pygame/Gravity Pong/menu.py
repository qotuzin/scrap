import pygame as pg
import gui_classes as gui

class Menu():
    def __init__(self, game):
        self.game = game
        self.font = pg.font.SysFont(None, 50)
        self.BUTTON_LEFT = False

        self.start_button = gui.Button('Click to Start', self.font, (255,255,255), 400, 300, 215, 40)
        self.title_text = gui.Text('Main Menu', self.font, (255, 255, 255), 400, 150)

    def main_menu(self):
        self.game.__init__()  # reset game
        while self.game.running and not self.game.playing:
            # set fps clock
            #self.game.clock.tick(self.game.FPS)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.game.running = False # turns off program
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.game.running = False
                    if event.key == pg.K_RETURN:
                        self.game.screen.fill((100, 100, 100))
                        self.game.playing = True
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.BUTTON_LEFT = True
                if event.type == pg.MOUSEBUTTONUP:
                    self.BUTTON_LEFT = False

            self.game.screen.fill((0, 0, 0))
            self.title_text.draw_text(self.game.screen)
            self.start_button.draw_button(self.game.screen)
            pg.display.update()
            