import pygame


def image_colour_changer(image, old_colour, new_colour):
    pygame.PixelArray(image).replace(old_colour, new_colour)
    return image
