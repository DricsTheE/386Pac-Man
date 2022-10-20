import pygame as pg
from pygame.sprite import Sprite, Group
from timer import Timer

class Ghost(Sprite):
    ghost_blinky = [pg.transform.rotozoom(pg.image.load(f'images/blinky_right{3}.png'), 0, 0.7) for n in range(2)]
    ghost_pinky = [pg.transform.rotozoom(pg.image.load(f'images/pinky_right{3}.png'), 0, 0.7) for n in range(2)]
    ghost_inky = [pg.transform.rotozoom(pg.image.load(f'images/inky_right{3}.png'), 0, 0.7) for n in range(2)]
    ghost_clyde = [pg.transform.rotozoom(pg.image.load(f'images/clyde_right{3}.png'), 0, 0.7) for n in range(2)]


    def __init__(self, game):
        self.screen = game.screen
        self.settings = game.settings
        self.image = pg.image.load('images/blinky_right3.png')
        self.rect = self.image_get_rect()
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)


    def update(self):
        settings = self.settings
        self.draw()

    def draw(self):
        image = self.timer.image()
        rect = image.get_rect()
        rect.left = rect.top = self.rect.left, self.rect.top
        self.screen.blit(image, rect)
