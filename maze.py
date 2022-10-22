import pygame as pg
import math
from random import randrange
import random
from settings import Settings
from player import PacMan

mazePath = 'images/maze/'

class Maze:
    def __init__(self, game):
        self.game = game
        self.settings = Settings()
        self.pacman = PacMan(game=game)

    def drawMaze(self):
        self.settings.screen.fill((0,0,0))
        current_tile = 0
        for i in range(3, len(self.settings.gameBoard) - 2):
            for j in range(len(self.settings.gameBoard[0])):
                if self.settings.gameBoard[i][j] == 3:
                    imageName = str(current_tile)
                    if len(imageName) == 1:
                        imageName = '00' + imageName
                    elif len(imageName) == 2:
                        imageName = '0' + imageName
                    imageName = "tile" + imageName + ".png"
                    tileImage = pg.image.load(mazePath + imageName)
                    tileImage = pg.transform.scale(tileImage, (self.settings.square, self.settings.square))
                    
                    
                    self.settings.screen.blit(tileImage, (j * self.settings.square, i * self.settings.square, self.settings.square, self.settings.square))

                elif self.settings.gameBoard[i][j] == 2:
                    pg.draw.circle(self.settings.screen, self.settings.pelletColor, (j * self.settings.square + self.settings.square//2,
                     i * self.settings.square + self.settings.square//2), self.settings.square//4)
                
                elif self.settings.gameBoard[i][j] == 5:
                    pg.draw.circle(self.settings.screen, (0,0,0), (j * self.settings.square + self.settings.square//2, 
                    i * self.settings.square + self.settings.square//2), self.settings.square//2)

                elif self.settings.gameBoard[i][j] == 6:
                    pg.draw.circle(self.settings.screen, self.settings.pelletColor, (j * self.settings.square + self.settings.square//2, 
                    i * self.settings.square + self.settings.square//2), self.settings.square//2)
                
                current_tile += 1

        self.pacman.update()
        pg.display.update()