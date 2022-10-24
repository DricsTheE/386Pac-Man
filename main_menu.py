from decimal import HAVE_CONTEXTVAR
import imghdr
import pygame as pg
import sys

import pygame.display

from button import Button

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (130, 130, 130)
INDIGO = (88, 90, 139)
RED = (255, 0 , 0)
LAVENDER = (255, 184, 255)
AQUA = (0, 255, 255)
ORANGE = (255, 184, 82)


class MainMenu:
    def __init__(self, game):
        self.screen = game.screen
        self.main_menu_finished = False
        self.screen_rect = self.screen.get_rect()
        self.font = pg.font.SysFont(None, 48)
        self.headder = pg.font.SysFont(None, 190)
        self.subheadder = pg.font.SysFont(None, 110)
        self.play_button = Button(self.screen, "PLAY GAME", ul=(240, 800))
        self.clock = pg.time.Clock()
        self.run = True
        self.value = 0

        self.image = pg.image.load('images/characters/blinky_right3.png')
        self.image = pg.transform.scale(self.image, (128,128))

        self.image_rect = self.image.get_rect()
        self.screen.blit(self.image, self.image_rect)

    def get_score(self):
        with open('score.txt', 'r') as s:
            score = s.read()
            s.close()
            return str(score)

    def check_events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                sys.exit()
            if e.type == pg.KEYUP and e.key == pg.K_p:
                self.main_menu_finished = True
            elif e.type == pg.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pg.mouse.get_pos()
                if self.play_button.rect.collidepoint(mouse_x, mouse_y):
                    self.main_menu_finished = True

    def update(self):
        self.draw()

    def show(self):
        while not self.main_menu_finished:
            self.update()
            self.draw()
            self.check_events()

    def draw_texts(self):
        PacMan = "PAC-MAN"
        self.title = self.headder.render(PacMan, True, WHITE)
        self.screen.blit(self.title, (40, 50))

        Blinky = " - BLINKY"
        self.title = self.subheadder.render(Blinky, True, RED)
        self.screen.blit(self.title, (150, 200))

        Pinky = " - PINKY"
        self.title = self.subheadder.render(Pinky, True, LAVENDER)
        self.screen.blit(self.title, (150, 350))

        Inky = " - INKY"
        self.title = self.subheadder.render(Inky, True, AQUA)
        self.screen.blit(self.title, (150, 500))

        Clyde = " - CLYDE"
        self.title = self.subheadder.render(Clyde, True, ORANGE)
        self.screen.blit(self.title, (150, 650))

        high_score = "HIGH SCORE : 0"
        self.title = self.font.render(high_score, True, WHITE)
        self.screen.blit(self.title, (100, 750))

    def draw(self):
        self.screen.fill(BLACK)
        self.draw_texts()
        #self.draw_score()
        self.play_button.draw()

        blinky_temp1 = pg.transform.scale(pg.image.load('images/characters/blinky_right3.png'), (128, 128))
        blinky_temp2 = pg.transform.scale(pg.image.load('images/characters/blinky_right4.png'), (128, 128))
        blinky = [blinky_temp1, blinky_temp2]

        pinky_temp1 = pg.transform.scale(pg.image.load('images/characters/pinky_right3.png'), (128,128))
        pinky_temp2 = pg.transform.scale(pg.image.load('images/characters/pinky_right4.png'), (128,128))
        pinky = [pinky_temp1, pinky_temp2]

        inky_temp1 = pg.transform.scale(pg.image.load('images/characters/inky_right3.png'), (128, 128))
        inky_temp2 = pg.transform.scale(pg.image.load('images/characters/inky_right4.png'), (128, 128))
        inky = [inky_temp1, inky_temp2]

        clyde_temp1 = pg.transform.scale(pg.image.load('images/characters/clyde_right3.png'), (128, 128))
        clyde_temp2 = pg.transform.scale(pg.image.load('images/characters/clyde_right4.png'), (128, 128))
        clyde = [clyde_temp1, clyde_temp2]

        self.clock.tick(3)
        if self.value >= len(pinky):
            self.value = 0
        blinky_image = blinky[self.value]
        pinky_image = pinky[self.value]
        inky_image = inky[self.value]
        clyde_image = clyde[self.value]

        self.screen.blit(blinky_image, (40, 150))
        self.screen.blit(pinky_image, (40, 300))
        self.screen.blit(inky_image, (40, 450))
        self.screen.blit(clyde_image, (40, 600))
        pygame.display.update()
        self.value +=1

        pg.display.flip()


