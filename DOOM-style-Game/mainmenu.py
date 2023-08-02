from button import Button
import sys
import pygame as pg
from leaderboards import Leaderboard
from profile import ProfileMenu
from settings import *
from sound import Sound


class MainMenu:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.font_renderer = game.font_renderer
        self.buttons = []
        self.initButtons()
        self.mouseDown = False
        self.sound = Sound(self)
        self.sound.loadMenuSounds()
        pg.mixer.music.play(-1)
        self.image = self.get_texture('resources/textures/stranger.jpg', RES)
        self.show_leaderboard = False
        self.show_profile = False
        self.leaderboard = Leaderboard(self)
        self.profile = ProfileMenu(self)
        self.keys = []

    def initButtons(self):
        self.buttons = []
        start = Button(
            self.game,
            20,
            HEIGHT // 2,
            'Start Game', 'white',
            self.start_game)

        leaderboards = Button(
            self.game,
            20,
            HEIGHT // 2 + 100,
            'Leader boards', 'white',
            self.on_leaderboard)

        credits = Button(
            self.game,
            20,
            HEIGHT // 2 + 200,
            'Credits', 'white',
            self.start_game)

        profile = Button(
            self.game,
            WIDTH // 2 - 100,
            20,
            f"Profile - {self.game.name}", 'white',
            self.on_profile)

        self.add_button(leaderboards)
        self.add_button(start)
        self.add_button(credits)
        self.add_button(profile)

    def start_game(self):
        self.game.CUR_MENU = self.game.GAME
        self.game.new_game()

    def on_leaderboard(self):
        self.show_leaderboard = True

    def on_profile(self):
        self.show_profile = True

    def check_events(self):
        self.mouseDown = False
        self.keys = []
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                self.keys.append(event)
            if event.type == pg.QUIT or (
                    event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                self.mouseDown = True

    def update(self):
        self.game.screen.blit(self.image, (0, 0))
        for button in self.buttons:
            button.draw()
            if self.mouseDown:
                button.clicked()

        self.check_events()
        if self.show_leaderboard:
            self.leaderboard.draw()

        if self.show_profile:
            self.profile.draw()

        pg.display.flip()

    def add_button(self, button):
        self.buttons.append(button)

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)
