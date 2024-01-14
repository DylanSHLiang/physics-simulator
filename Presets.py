import pygame
import math
from Draw_Text import *
import sys
import Events
import time
from Classes import *

WIDTH, HEIGHT = 1280, 720
FPS = 60
colour_scheme = [(0, 0, 0), (0, 0, 0), (155, 155, 155)]

# Asset Presets
Icon = pygame.image.load('physics_icon.png')
back_arrow = image(307 * WIDTH / 320, 149 * HEIGHT / 160, WIDTH / 40, WIDTH / 40, pygame.image.load('back arrow.png'), (0, 0, 0))
start_icon = image(187*WIDTH/216, HEIGHT/20, WIDTH/24, HEIGHT/15, pygame.image.load('start.png'), (155, 155, 155))
cross_icon = image(WIDTH / 30, HEIGHT / 16.875, 50, 40, pygame.image.load('cross.jpg'), colour_scheme[0])
projectile_motion_icon = image(5*WIDTH/32, 2*HEIGHT/8, HEIGHT/3, HEIGHT/3, pygame.image.load('projectile.PNG'), colour_scheme[0])
circular_motion_icon = image(171*WIDTH/256, 23*HEIGHT/84, 8*HEIGHT/27, 8*HEIGHT/27, pygame.image.load('circular.PNG'), colour_scheme[0])
banked_tracks_icon = image(5*WIDTH/32, 7*HEIGHT/11, HEIGHT/3, HEIGHT/3, pygame.image.load('banked tracks.PNG'), colour_scheme[0])
gravity_in_space_icon = image(87*WIDTH/128, 53*HEIGHT/80, HEIGHT/4, HEIGHT/4, pygame.image.load('gravity in space.PNG'), colour_scheme[0])
line_thickness = 4
corner_roundness = 4

# Screen Presets
pygame.init()
pygame.display.set_caption('Physics Simulator')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_icon(Icon)

# Font Presets
arial_font_title = pygame.font.SysFont('arial', int(WIDTH / 20), 1)
arial_font_header = pygame.font.SysFont('arial', int(WIDTH / 30), 1)
arial_font_small_title = pygame.font.SysFont('arial', int(WIDTH / 38), 1)
arial_font_text = pygame.font.SysFont('arial', int(WIDTH / 36), 0)
arial_font_type = pygame.font.SysFont('arial', int(WIDTH / 50), 0)
arial_font_label = pygame.font.SysFont('arial', int(WIDTH / 60), 0)
