import pygame as pg


class UIRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.font_renderer = game.font_renderer
        self.buttons = []

    def update(self):
        pos = pg.mouse.get_pos()
        for button in self.buttons:
            button.draw()
            button.clicked(pos)

    def add_button(self, button):
        self.buttons.append(button)
