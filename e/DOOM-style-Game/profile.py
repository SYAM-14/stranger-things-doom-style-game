from button import Button
import sys
import pygame as pg
from database import addScore, getScores, loadScores
from settings import *


class ProfileMenu:
    def __init__(self, mainmenu):
        game = mainmenu.game
        self.mainmenu = mainmenu
        self.game = game
        self.screen = game.screen
        self.font_renderer = game.font_renderer
        self.mouseDown = False
        self.surface = pg.Surface((800, 300))
        self.x = (WIDTH - 800) // 2
        self.y = (HEIGHT - 600) // 2
        self.surface.fill((0, 0, 0))
        self.initButtons()
        self.text = game.name

    def initButtons(self):
        self.buttons = []
        back = Button(
            self.game,
            20 + self.x,
            20 + self.y,
            'X', 'yellow',
            self.back)

        save = Button(
            self.game,
            400 + self.x,
            200 + self.y,
            'Save', 'Green',
            self.save)

        self.add_button(back)
        self.add_button(save)

    def add_button(self, button):
        self.buttons.append(button)

    def back(self):
        self.mainmenu.show_profile = False

    def save(self):
        self.mainmenu.game.name = self.text
        addScore(self.text, 0)
        self.mainmenu.initButtons()
        self.back()

    def draw(self):
        self.surface.fill((0, 0, 0))
        for key in self.mainmenu.keys:
            if key.key == pg.K_BACKSPACE:
                self.text = self.text[:-1]
            elif key.key == pg.K_RETURN:
                self.back()
                break
            elif len(self.text) < 12:
                self.text += key.unicode
        for button in self.buttons:
            button.draw()
            self.surface.blit(
                button.surface, (button.x - self.x, button.y - self.y))
            if self.mainmenu.mouseDown:
                button.clicked()

        (texture, rect) = self.font_renderer.fontLarge.render(
            self.text, fgcolor='white')
        self.surface.blit(texture, (200, 100))
        self.screen.blit(self.surface, (self.x, self.y))
