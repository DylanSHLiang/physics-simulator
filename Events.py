import pygame
from pygame.locals import *
import sys


def events(left_click, running):
    mouse_release = None
    key_down = None
    mouse_move = None
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_BACKSPACE:
                key_down = 'BACKSPACE'
            else:
                key_down = event.unicode
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                left_click = True
        if event.type == MOUSEBUTTONUP:
            mouse_release = True
        if event.type == MOUSEMOTION:
            mouse_move = True
    return left_click, running, mouse_move, mouse_release, key_down
