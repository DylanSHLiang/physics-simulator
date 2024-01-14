from Classes import *
import pygame.draw
from Presets import *
from Gravity_In_Space_Menu import gravity_in_space_menu


def gravity_in_space(FPS, WIDTH, HEIGHT, colour_scheme):
    arial_font_title = pygame.font.SysFont('arial', int(WIDTH / 20), 1)
    arial_font_header = pygame.font.SysFont('arial', int(WIDTH / 30), 1)
    arial_font_small_title = pygame.font.SysFont('arial', int(WIDTH / 38), 1)
    arial_font_text = pygame.font.SysFont('arial', int(WIDTH / 36), 0)
    arial_font_type = pygame.font.SysFont('arial', int(WIDTH / 50), 0)
    arial_font_label = pygame.font.SysFont('arial', int(WIDTH / 60), 0)
    # Creates buttons
    back_arrow.x_position, back_arrow.y_position, back_arrow.image = 307 * WIDTH / 320, 149 * HEIGHT / 160, pygame.transform.scale(back_arrow.picture, (WIDTH / 40, WIDTH / 40))
    back_arrow.image = image_colour_changer(back_arrow.image, back_arrow.colour, colour_scheme[0])
    back_button = button(153*WIDTH/160, 37*HEIGHT/40, WIDTH/30, WIDTH/30, colour_scheme[0], colour_scheme[2], None, back_arrow.image, None)
    start_icon = image(187 * WIDTH / 216, HEIGHT / 20, WIDTH / 24, HEIGHT / 15, pygame.image.load('start.png'), (0, 0, 0))
    start_icon.x_position, start_icon.y_position, start_icon.image = 187 * WIDTH / 216, HEIGHT / 20, pygame.transform.scale(start_icon.picture, (WIDTH / 24, HEIGHT / 15))
    start_icon.image = image_colour_changer(start_icon.image, start_icon.colour, colour_scheme[2])
    start_button = button(8*WIDTH/9, HEIGHT/12, WIDTH / 25, WIDTH / 25, colour_scheme[0], colour_scheme[2], None, start_icon.image, True)
    start_button.button.center = (start_button.x_position, start_button.y_position)
    menu_button = button(WIDTH/2, HEIGHT, WIDTH/22, HEIGHT/30, colour_scheme[0], colour_scheme[2], None, None, None)
    menu_button.button.midbottom = menu_button.x_position, menu_button.y_position

    # Creates menu buttons
    reset_button = button(19*WIDTH/24, 17*HEIGHT/20, WIDTH/12, HEIGHT/18, colour_scheme[0], colour_scheme[2], 'RESET', None, None)
    radius_box = button(18*WIDTH/100, 86*HEIGHT/100, WIDTH/34, WIDTH/34, colour_scheme[0], colour_scheme[2], '0', None, None)
    mass_box = button(52*WIDTH/100, 86*HEIGHT/100, 21*WIDTH/320, WIDTH/34, colour_scheme[0], colour_scheme[2], '0', None, None)

    #
    planet_array = []

    # Sets variables
    menu_open = True
    radius = 0
    mass = 0
    start_time = time.time()
    program_time = 0
    pause_time = 0
    running = True
    while running:

        # Resets left click
        left_click = False

        # Resets screen
        screen.fill((255, 255, 255))

        # Gets position of mouse
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Processes events that occur
        left_click, running, mouse_move, mouse_release, key_down = Events.events(left_click, running)

        back_button.button_click(mouse_x, mouse_y, left_click)
        if back_button.active:
            running = False
            back_button.active = False

        # Updates left click
        if menu_open:
            if HEIGHT/6 < mouse_y < 3*HEIGHT/4 and 0 < mouse_x < WIDTH and mass != 0:
                if left_click:
                    body = planet(colour_scheme[1], mouse_x, mouse_y, 0, 0, radius, mass * (10 ** 10))
                    planet_array.append(body)
        else:
            if HEIGHT/6 < mouse_y < HEIGHT and 0 < mouse_x < WIDTH and mass != 0:
                if left_click:
                    body = planet(colour_scheme[1], mouse_x, mouse_y, 0, 0, radius, mass * (10 ** 10))
                    planet_array.append(body)

        # Updates start button
        start_button.toggle_button_click(mouse_x, mouse_y, left_click)

        # Processes collisions against boundaries
        for body in planet_array:
            if body.x_position + radius < 0 or body.x_position - radius > WIDTH:
                if body in planet_array:
                    planet_array.remove(body)
            if body.y_position + radius < HEIGHT/12 or body.y_position - radius > HEIGHT:
                if body in planet_array:
                    planet_array.remove(body)

        if start_button.active:
            old_time = program_time
            program_time = time.time() - start_time - pause_time
            time_increment = program_time - old_time

            # Calculates acceleration
            for body in planet_array:
                planet_array = body.calculate_stats(planet_array)
                body.calculate_position(time_increment)
                planet_array = body.calculate_collision(planet_array)

        else:
            pause_time = time.time() - start_time - program_time

        # Draws simulation
        for body in planet_array:
            pygame.draw.circle(screen, body.colour, (body.x_position, body.y_position), body.radius)

        # Draws Overlay
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 0, WIDTH, HEIGHT/6))
        # Draws text
        draw_text_midleft('Gravity In Space', arial_font_small_title, colour_scheme[0], screen, WIDTH/26, HEIGHT/12)

        # Draws buttons
        pygame.draw.rect(screen, start_button.colour, start_button.button, 2, 3)

        # Draws icons
        screen.blit(start_icon.image, (start_icon.x_position, start_icon.y_position))

        # Draws lines
        pygame.draw.line(screen, colour_scheme[1], (0, HEIGHT/6), (WIDTH, HEIGHT/6), line_thickness)
        pygame.draw.line(screen, colour_scheme[1], (0, 1), (WIDTH, 1), line_thickness)

        # Processes menu
        planet_array, radius, mass, left_click, menu_button, menu_open, start_button = gravity_in_space_menu(colour_scheme, planet_array, menu_button, menu_open, start_button, reset_button, radius_box, mass_box, WIDTH, HEIGHT, left_click, key_down, mouse_x, mouse_y, radius, mass)

        # Draws back button
        pygame.draw.rect(screen, back_button.colour, back_button.button, 2, 3)
        screen.blit(back_arrow.image, (back_arrow.x_position, back_arrow.y_position))

        pygame.display.update()
        clock.tick(FPS)
