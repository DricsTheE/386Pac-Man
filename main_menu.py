from decimal import HAVE_CONTEXTVAR
import imghdr
import pygame as pg
import sys
from button import Button
#from stats import Stats

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

    def draw(self):
        self.screen.fill(BLACK)
        self.draw_texts()
        #self.draw_score()
        self.play_button.draw()

        image = self.image
        self.screen.blit(image, (40,150))

        pinky = pg.image.load('images/characters/pinky_right3.png')
        pinky = pg.transform.scale(pinky, (128,128))
        self.screen.blit(pinky, (40, 300))

        inky = pg.image.load('images/characters/inky_right3.png')
        inky = pg.transform.scale(inky, (128,128))
        self.screen.blit(inky, (40, 450))

        clyde = pg.image.load('images/characters/clyde_right3.png')
        clyde = pg.transform.scale(clyde, (128,128))
        self.screen.blit(clyde, (40, 600))

        pg.display.flip()


