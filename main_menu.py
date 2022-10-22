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


class MainMenu:

    def __init__(self, game):
        self.screen = game.screen
        self.main_menu_finished = False
        self.screen_rect = self.screen.get_rect()
        self.font = pg.font.SysFont(None, 48)
        self.headder = pg.font.SysFont(None, 190)
        self.subheadder = pg.font.SysFont(None, 110)
        self.play_button = Button(self.screen, "PLAY GAME", ul=(240, 650))

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


    def draw(self):
        self.screen.fill(BLACK)
        self.draw_texts()
        #self.draw_score()
        self.play_button.draw()
        pg.display.flip()
