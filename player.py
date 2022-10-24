from asyncio import events
import pygame as pg
from pygame.sprite import Sprite
from game_functions import clamp
from vector import Vector
from settings import Settings
from game_functions import movement


class PacMan(Sprite):
    pacman = pg.image.load('images/characters/pacman2.png')
    def __init__(self, game):
        super().__init__()
        self.settings = Settings
        self.game = game
        self.settings = game.settings
        self.screen = self.settings.screen
        self.image = pg.image.load('images/characters/pacman2.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.settings.screen.get_rect()
        self.vel = Vector()
        self.posn = self.center()

        self.dying = self.dead = False

    def reset(self): 
        self.vel = Vector()
        self.posn = self.center()
        self.rect.left, self.rect.top = self.posn.x, self.posn.y    

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
        self.screen.blit(self.image,self.rect)
        pg.display.update()

    def getValidKey(self,event):
        key = event.key
        if key == pg.K_LEFT: PacMan.vel = Vector()

