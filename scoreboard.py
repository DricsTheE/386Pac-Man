import pygame as pg

class Scoreboard:
    def __init__(self, game):
        self.score = 0
        self.level = 0
        self.highscore = 0

        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.text_color = (200, 200, 200)
        self.font = pg.font.SysFont(None, 48)

        self.score_image = None
        self.score_rect = None
        self.prep_score()

    def increment_score(self):
        self.score += self.settings.ghost_points
        self.prep_score()

    def prep_score(self):
        score_str = str(self.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

    def reset(self):
        self.score = 0
        self.update()

    def update(self):
        self.draw()

    def draw(self):
        self.screen.blit(self.score_image, (500, 20))
