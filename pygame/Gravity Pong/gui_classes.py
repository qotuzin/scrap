import pygame as pg

class UserInterface(pg.sprite.Sprite):
    def __init__(self, img):
        pg.sprite.Sprite.__init__(self)
        self.image = img

class Text():
    def __init__(self, text, font, colour, x, y):
        self.text = text
        self.font = font
        self.colour = colour
        self.textobj = font.render(text, 1, colour)
        self.textrect = self.textobj.get_rect()
        self.textrect.topleft = (x, y)

    def draw_text(self, surface):
        self.textobj = self.font.render(self.text, 1, self.colour)
        surface.blit(self.textobj, self.textrect)

class TextBox():
    def __init__(self):
        pass

class Button():
    def __init__(self, button_text, font, text_colour, x, y, width, height):
        self.rect = pg.Rect(x, y, width, height)
        self.text = Text(button_text, font, text_colour, x, y)
        self.font = font
        self.text_colour = text_colour
        self.MOUSE_BUTTON_LEFT = False

    def draw_button(self, surface):
        colour = (100, 100, 100)
        point = pg.mouse.get_pos()
        self.collide = self.rect.collidepoint(point)
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                self.MOUSE_BUTTON_LEFT = True
                if self.collide:
                    if self.MOUSE_BUTTON_LEFT:
                        colour = (200, 200, 0)
                    else:
                        colour = (200, 200, 200)
                else:
                    colour = (100, 100, 100)


        pg.draw.rect(surface, colour, self.rect)
        self.text.draw_text(surface)