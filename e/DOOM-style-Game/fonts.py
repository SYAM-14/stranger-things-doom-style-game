import pygame as pg
from settings import *


class Text:
    def __init__(self, screen, text, pos, color, size, ttl):
        self.screen = screen
        self.color = color
        self.size = size
        self.text = text
        self.pos = pos
        self.timeToLive = ttl


class FontRenderer:
    def __init__(self, game):
        self.screen = game.screen
        self.fontSmall = pg.freetype.Font(
            "resources/fonts/AmazDooMLeft.ttf", 20)
        self.fontMedium = pg.freetype.Font(
            "resources/fonts/AmazDooMLeft.ttf", 40)
        self.fontLarge = pg.freetype.Font(
            "resources/fonts/AmazDooMLeft.ttf", 80)
        self.timeTexts = []

    def render(self, text, pos, size, color=(255, 255, 255)):
        if size == 0:
            self.fontSmall.render_to(self.screen, pos, text, color)
        elif size == 1:
            self.fontMedium.render_to(self.screen, pos, text, color)
        elif size == 2:
            self.fontLarge.render_to(self.screen, pos, text, color)

    def addTimeText(self, text, pos, size, color, ttl):
        self.timeTexts.append(
            Text(
                self.screen,
                text,
                pos,
                color,
                size,
                ttl))

    def drawTimeTexts(self):
        for text in self.timeTexts:
            self.render(text.text, text.pos, text.size, text.color)
            text.timeToLive -= 1
        self.timeTexts = [
            text for text in self.timeTexts if text.timeToLive > 0]
