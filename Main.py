from Presets import *
from Advanced_Mechanics import advanced_mechanics
from Settings import settings


def main(FPS, WIDTH, HEIGHT, colour_scheme):
    running = True
    while running:
        # Adjusts font sizes
        arial_font_title = pygame.font.SysFont('arial', int(WIDTH / 20), 1)
        arial_font_header = pygame.font.SysFont('arial', int(WIDTH / 30), 1)
        arial_font_small_title = pygame.font.SysFont('arial', int(WIDTH / 38), 1)
        arial_font_text = pygame.font.SysFont('arial', int(WIDTH / 36), 0)
        arial_font_type = pygame.font.SysFont('arial', int(WIDTH / 50), 0)
        arial_font_label = pygame.font.SysFont('arial', int(WIDTH / 60), 0)

        # Creates GUI elements
        advanced_mechanics_button = button(3*WIDTH/8, 3*HEIGHT/10, WIDTH/4, HEIGHT/7, colour_scheme[0], colour_scheme[2], 'Advanced Mechanics', None, None)
        settings_button = button(3*WIDTH/8, 11*HEIGHT/20, WIDTH/4, HEIGHT/7, colour_scheme[0], colour_scheme[2], 'Settings', None, None)
        exit_button = button(3*WIDTH/8, 4*HEIGHT/5, WIDTH/4, HEIGHT/7, colour_scheme[0], colour_scheme[2], 'Exit', None, None)

        # Resets left click
        left_click = False

        # Resets screen
        screen.fill((255, 255, 255))

        # Gets mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Processes events
        left_click, running, mouse_move, mouse_release, key_down = Events.events(left_click, running)

        # Updates advanced mechanics button
        advanced_mechanics_button.button_click(mouse_x, mouse_y, left_click)
        if advanced_mechanics_button.active:
            advanced_mechanics(FPS, WIDTH, HEIGHT, colour_scheme)
            advanced_mechanics_button.active = False

        # Updates settings button
        settings_button.button_click(mouse_x, mouse_y, left_click)
        if settings_button.active:
            FPS, WIDTH, HEIGHT, colour_scheme = settings(FPS, WIDTH, HEIGHT, colour_scheme)
            settings_button.active = False

        # Updates exit button
        exit_button.button_click(mouse_x, mouse_y, left_click)
        if exit_button.active:
            running = False

        # Draws screen
        # Draws lines
        pygame.draw.line(screen, colour_scheme[1], (0, 1), (WIDTH, 1), line_thickness)
        pygame.draw.line(screen, colour_scheme[1], (0, HEIGHT/6), (WIDTH, HEIGHT/6), line_thickness)

        # Draws buttons
        pygame.draw.rect(screen, advanced_mechanics_button.colour, advanced_mechanics_button.button, corner_roundness, line_thickness)  # Draws advanced mechanics button
        pygame.draw.rect(screen, settings_button.colour, settings_button.button, corner_roundness, line_thickness)  # Draws settings button
        pygame.draw.rect(screen, exit_button.colour, exit_button.button, corner_roundness, line_thickness)  # Draws exit button

        # Draws text
        draw_text_centre('Physics Simulator', arial_font_title, colour_scheme[0], screen, WIDTH / 2, HEIGHT/12)  # Draws title
        draw_text_centre(advanced_mechanics_button.text, arial_font_text, advanced_mechanics_button.colour, screen, WIDTH / 2, 13*HEIGHT/35)  # Draws advanced mechanics label
        draw_text_centre(settings_button.text, arial_font_text, settings_button.colour, screen, WIDTH / 2, 87*HEIGHT/140)  # Draws settings label
        draw_text_centre(exit_button.text, arial_font_text, exit_button.colour, screen, WIDTH / 2, 61*HEIGHT/70)  # Draws exit label

        pygame.display.update()
        clock.tick(FPS)
