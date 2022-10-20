import sys
import pygame as pg
from vector import Vector

movement = {pg.K_LEFT: Vector(-.1, 0),   # dictionary to map keys to Vector velocities
            pg.K_RIGHT: Vector(.1, 0),
            pg.K_UP: Vector(0, -.1),
            pg.K_DOWN: Vector(0, .1)
            }

game_active = False


def check_keydown_events(event, settings, pacman):
    key = event.key
    if key in movement.keys(): 
        pacman.vel = settings.PM_SPD * movement[key]
        # print(f'ship now moving at {ship.vel}')

def check_keyup_events(event, pacman):
    key = event.key
    if key == pg.K_ESCAPE: pacman.vel = Vector()   # Note: Escape key stops the ship
    elif key in movement.keys(): pacman.vel = Vector()

def check_events(settings, pacman):
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
        elif event.type == pg.KEYDOWN: check_keydown_events(event=event, settings=settings, pacman=pacman)
        elif event.type == pg.KEYUP: 
            check_keyup_events(event=event, pacman=pacman)
        

def clamp(posn, rect, settings):
    left, top = posn.x, posn.y
    width, height = rect.width, rect.height
    left = max(0, min(left, settings.screen_width - width))
    top = max(0, min(top, settings.screen_height - height))
    return Vector(x=left, y=top), pg.Rect(left, top, width, height)

