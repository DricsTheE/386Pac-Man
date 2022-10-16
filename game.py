import pygame as pg
from button import Button
from main_menu import MainMenu
from setting import Settings
from player import PacMan
import sys


class Game:
    def __init__(self):
        pg.init()
        self.settings = Settings()
        size = self.settings.screen_width, self.settings.screen_height   # tuple
        self.screen = pg.display.set_mode(size=size)
        pg.display.set_caption("PacMan")

        self.pacman = PacMan(game=self)

        #self.sound = Sound(bg_music="sounds/main_theme.wav")
        #self.scoreboard = Scoreboard(game=self)
        self.game_active = False

    def reset(self):
        pass
        print('Resetting game...')

    def game_over(self):
        pass

    def play(self):
        while True:
            self.screen.fill(self.settings.bg_color)
            self.pacman.update()
            pg.display.flip()


def main():
    g = Game()
    m = MainMenu(game=g)
    m.show()
    g.play()


if __name__ == '__main__':
    main()
