import pygame as pg


class Button:
    def __init__(self, game, x, y, text, color, action=None):
        self.game = game
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.action = action
        (texture, rect) = game.font_renderer.fontLarge.render(
            self.text, fgcolor=self.color)

        (textureHighlighted, rect) = game.font_renderer.fontLarge.render(
            self.text, fgcolor='red')
        self.texture = texture
        self.textureHighlighted = textureHighlighted
        self.surface = texture
        self.w = rect.width
        self.h = rect.height
        self.mouseOver = False

    def draw(self):
        pos = pg.mouse.get_pos()
        self.game.screen.blit(self.surface, (self.x, self.y))
        if self.x < pos[0] < self.x + \
                self.w and self.y < pos[1] < self.y + self.h:
            self.mouseOver = True
            self.surface = self.textureHighlighted
        else:
            self.mouseOver = False
            self.surface = self.texture

    def clicked(self):
        if self.mouseOver and self.action is not None:
            self.action()
