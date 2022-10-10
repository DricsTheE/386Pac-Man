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
        self.play_button = Button(self.screen, "PLAY GAME", ul=(450, 650))

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
        PacMan = "PACMAN"
        invaders = "Invaders"
        tenPoints = "= 10 PTS"
        twentyPoints = "= 20 PTS"
        thirtyPoints = "= 30 PTS"
        qPoints = "= ???"

        self.invaders_img = self.subheadder.render(invaders, True,  BLACK, INDIGO)
        self.space_img = self.headder.render(PacMan, True, BLACK, INDIGO)
        self.ten_img = self.font.render(tenPoints, True, WHITE, INDIGO)
        self.twen_img = self.font.render(twentyPoints, True, WHITE, INDIGO)
        self.thir_img = self.font.render(thirtyPoints, True, WHITE, INDIGO)
        self.q_img = self.font.render(qPoints, True, WHITE, INDIGO)

        self.screen.blit(self.space_img, (400, 50))
        self.screen.blit(self.invaders_img, (440, 182))
        self.screen.blit(self.ten_img, (535, 370))
        self.screen.blit(self.twen_img, (535, 430))
        self.screen.blit(self.thir_img, (535, 500))
        self.screen.blit(self.q_img, (535, 570))

    """
    def draw_score(self):
        score = "Highscore: "
        score += self.get_score()
        self.score_img = self.font.render(score, True, BLACK, GREY)
        self.screen.blit(self.score_img, (20,20))
    """

    def draw(self):
        self.screen.fill(BLACK)
        self.draw_texts()
        #self.draw_score()
        self.play_button.draw()
        pg.display.flip()
