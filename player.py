import pygame as pg
from pygame.sprite import Sprite
from game_functions import clamp
from vector import Vector


class PacMan(Sprite):
    pacman = pg.image.load('images/pacman0.png')
    def __init__(self, game):
        #super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.image = pg.image.load('images/pacman0.png')
        self.rect = self.image.get_rect()
        self.screen_rect = game.screen.get_rect()
        self.vel = Vector()
        self.posn = self.center()

        self.dying = self.dead = False

    def center(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        return Vector(self.rect.left, self.rect.top)

    def update(self):
        self.posn += self.vel
        self.posn, self.rect = clamp(self.posn, self.rect, self.settings)
        self.draw()

    def draw(self):
        image = self.image
        rect = image.get_rect()
        rect.left, rect.top = self.rect.left, self.rect.top
        self.screen.blit(image,rect)