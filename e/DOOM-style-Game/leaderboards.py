from button import Button
import sys
import pygame as pg
from database import getScores, loadScores, sortScores
from settings import *


class Leaderboard:
    def __init__(self, mainmenu):
        game = mainmenu.game
        self.mainmenu = mainmenu
        self.game = game
        self.screen = game.screen
        self.font_renderer = game.font_renderer
        self.buttons = []
        self.mouseDown = False
        self.surface = pg.Surface((800, 600))
        self.x = (WIDTH - 800) // 2
        self.y = (HEIGHT - 600) // 2
        self.surface.fill((0, 0, 0))
        self.initButtons()
        self.load_leaderboard()

    def load_leaderboard(self):
        loadScores()
        data = sortScores()
        i = 0
        for name, score in data.items():
            print(name, score)
            (texture, rect) = self.font_renderer.fontMedium.render(
                f'{i + 1}. {name} - {score}', fgcolor='yellow')
            self.surface.blit(texture, (20, 200 + i * 50))
            i += 1

    def initButtons(self):
        back = Button(
            self.game,
            20 + self.x,
            20 + self.y,
            'X', 'white',
            self.back)

        self.add_button(back)

    def add_button(self, button):
        self.buttons.append(button)

    def back(self):
        self.mainmenu.show_leaderboard = False

    def draw(self):
        for button in self.buttons:
            button.draw()
            self.surface.blit(
                button.surface, (button.x - self.x, button.y - self.y))
            if self.mainmenu.mouseDown:
                button.clicked()
        self.screen.blit(self.surface, (self.x, self.y))
