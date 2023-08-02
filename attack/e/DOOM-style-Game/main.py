import sys

import pygame as pg

from database import getScores, loadScores
from fonts import FontRenderer
from mainmenu import MainMenu
from map import *
from object_handler import *
from object_renderer import *
from pathfinding import *
from player import *
from raycasting import *
from settings import *
from sound import *
from sprite_object import *
from weapon import *


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.font_renderer = FontRenderer(self)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 40)
        self.level = 1
        self.score = 0
        self.enemies = 5

        self.MAIN_MENU = 0
        self.GAME = 1
        self.CUR_MENU = self.MAIN_MENU
        loadScores()
        self.name = 'no name'
        if 'current' in getScores():
            self.name = getScores()['current']

        self.main_menu_scene = MainMenu(self)

    def start_game(self):
        pg.mouse.set_visible(False)
        self.game_started = True
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self)
        self.weapon = Weapon(self)
        self.sound = Sound(self)
        self.sound.loadGameSounds()
        self.pathfinding = PathFinding(self)
        pg.mixer.music.play(-1)
        self.level = 1
        self.score = 0
        self.enemies = 5

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)

    def draw(self):
        self.object_renderer.draw()
        self.weapon.draw()

    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (
                    event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                if self.CUR_MENU == self.GAME:
                    self.CUR_MENU = self.MAIN_MENU
                else:
                    pg.quit()
                    sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True
            self.player.single_fire_event(event)

    def main_menu(self):
        self.main_menu_scene.update()

    def game(self):
        self.check_events()
        self.update()
        self.draw()

    def run(self):
        while True:
            if self.CUR_MENU == self.MAIN_MENU:
                self.main_menu()
            elif self.CUR_MENU == self.GAME:
                self.game()


if __name__ == '__main__':
    game = Game()
    game.run()
