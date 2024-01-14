import pygame.draw
from Projectile_Motion_Displacement_Calculator import displacement_calculator
from Projectile_Motion_Menu import projectile_motion_menu
from Classes import *
from Settings import *


def projectile_motion(FPS, WIDTH, HEIGHT, colour_scheme):
    # Adjusts font sizes
    arial_font_title = pygame.font.SysFont('arial', int(WIDTH / 20), 1)
    arial_font_header = pygame.font.SysFont('arial', int(WIDTH / 30), 1)
    arial_font_small_title = pygame.font.SysFont('arial', int(WIDTH / 38), 1)
    arial_font_text = pygame.font.SysFont('arial', int(WIDTH / 36), 0)
    arial_font_type = pygame.font.SysFont('arial', int(WIDTH / 50), 0)
    arial_font_label = pygame.font.SysFont('arial', int(WIDTH / 60), 0)

    # Creates GUI elements
    back_arrow.x_position, back_arrow.y_position, back_arrow.image = 307 * WIDTH / 320, 149 * HEIGHT / 160, pygame.transform.scale(back_arrow.picture, (WIDTH / 40, WIDTH / 40))
    back_arrow.image = image_colour_changer(back_arrow.image, back_arrow.colour, colour_scheme[0])
    back_button = button(153*WIDTH/160, 37*HEIGHT/40, WIDTH/30, WIDTH/30, colour_scheme[0], colour_scheme[2], None, back_arrow.image, None)
    start_icon = image(187 * WIDTH / 216, HEIGHT / 20, WIDTH / 24, HEIGHT / 15, pygame.image.load('start.png'), (0, 0, 0))
    start_icon.x_position, start_icon.y_position, start_icon.image = 187*WIDTH/216, HEIGHT/20, pygame.transform.scale(start_icon.picture, (WIDTH/24, HEIGHT/15))
    start_icon.image = image_colour_changer(start_icon.image, start_icon.colour, colour_scheme[2])
    start_button = button(8*WIDTH/9, HEIGHT/12, WIDTH / 25, WIDTH / 25, colour_scheme[0], colour_scheme[2], None, start_icon.image, True)
    start_button.button.center = (start_button.x_position, start_button.y_position)
    menu_button = button(WIDTH/2, HEIGHT, WIDTH/22, HEIGHT/30, colour_scheme[0], colour_scheme[2], None, None, None)
    menu_button.button.midbottom = menu_button.x_position, menu_button.y_position
    time_slider_button = button(WIDTH/4, HEIGHT / 12, WIDTH/60, WIDTH/30, colour_scheme[0], colour_scheme[2], None, None, None)
    time_slider_button.button.centery = time_slider_button.y_position
    launch_button = button(15*WIDTH/17, 7*HEIGHT/9, WIDTH/10, HEIGHT/15, colour_scheme[0], colour_scheme[2], 'LAUNCH', None, None)
    reset_button = button(13*WIDTH/17, 7*HEIGHT/9, WIDTH/10, HEIGHT/15, colour_scheme[0], colour_scheme[2], 'RESET', None, None)
    launch_angle_box = button(6*WIDTH/48, 7*HEIGHT/9, WIDTH/30, WIDTH/30, colour_scheme[0], colour_scheme[2], '0', None, None)
    launch_velocity_box = button(15*WIDTH/96, 17*HEIGHT/20, WIDTH/25, WIDTH/30, colour_scheme[0], colour_scheme[2], '0', None, None)
    gravity_box = button(5*WIDTH/48, 37*HEIGHT/40, WIDTH/25, WIDTH/30, colour_scheme[0], colour_scheme[2], '0', None, None)
    starting_distance_box = button(66*WIDTH/90, 69*HEIGHT/80, WIDTH/17, WIDTH/30, colour_scheme[0], colour_scheme[2], '0', None, None)
    starting_height_box = button(65*WIDTH/90, 75*HEIGHT/80, WIDTH/17, WIDTH/30, colour_scheme[0], colour_scheme[2], '0', None, None)
    projectile = ball((100, 100, 100), WIDTH/10, 2*HEIGHT/3, WIDTH/10, 2*HEIGHT/3, None, None, None, None, 10)
    floor = block((100, 100, 100), 0, 2*HEIGHT/3, WIDTH, 20)

    # Sets variables
    menu_open = True
    max_height = None
    horizontal_range = None
    time_of_flight = None
    launch_velocity = None
    launch_angle = None
    gravity = None
    launched = None
    pause_time = None
    press_time = None
    program_time = 0
    starting_height = 0
    starting_distance = 0
    running = True
    while running:
        # Resets left click
        left_click = False

        # Resets screen
        screen.fill((255, 255, 255))

        # Gets mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Processes events
        left_click, running, mouse_move, mouse_release, key_down = Events.events(left_click, running)

        # Updates back button
        back_button.button_click(mouse_x, mouse_y, left_click)
        if back_button.active:
            running = False
            back_button.active = False

        # Updates slider button and start button
        time_slider_button.slider_button_click(mouse_x, mouse_y, left_click, mouse_move, mouse_release, WIDTH/4, 11 * WIDTH / 16, not start_button.active)
        if time_slider_button.x_position < 3 * WIDTH / 4:
            start_button.toggle_button_click(mouse_x, mouse_y, left_click)
        else:
            start_button.colour = colour_scheme[0]
            start_button.image = image_colour_changer(start_button.image, colour_scheme[1], colour_scheme[0])

        # Syncs slider with simulation
        if launched:
            if start_button.active:
                program_time = time.time() - press_time - pause_time
                time_slider_button.x_position = (program_time * (7*WIDTH/16) / time_of_flight) + WIDTH/4
            else:
                pause_time = time.time() - press_time - program_time
                program_time = (time_slider_button.x_position - WIDTH/4) * time_of_flight / (7*WIDTH/16)

        # Updates ball and time
        if launched:
            projectile.x_position, projectile.y_position = displacement_calculator(projectile.starting_x_position, projectile.starting_y_position, launch_angle, launch_velocity, program_time, gravity)
            if projectile.y_position >= 2*HEIGHT/3 - projectile.radius:
                start_button.active = False
                time_slider_button.x_position = 11 * WIDTH / 16
        else:
            projectile.starting_x_position, projectile.x_position = int(starting_distance) + WIDTH/10, int(starting_distance) + WIDTH/10
            projectile.starting_y_position, projectile.y_position = 2*HEIGHT/3 - projectile.radius - int(starting_height), 2*HEIGHT/3 - projectile.radius - int(starting_height)

        # Draws simulation
        # Draws starting point
        pygame.draw.circle(screen, colour_scheme[2], (WIDTH/10, 2*HEIGHT/3 - projectile.radius), projectile.radius)

        # Draws projectile
        if -50 < projectile.x_position < WIDTH + 50 and -50 < projectile.y_position < HEIGHT + 50:
            pygame.draw.circle(screen, colour_scheme[1], (projectile.x_position, projectile.y_position), projectile.radius)

        # Draws floor
        pygame.draw.rect(screen, floor.colour, floor.block)

        # Draws Overlay
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 0, WIDTH, HEIGHT/6))
        # Draws text
        draw_text_midleft('Projectile Motion', arial_font_small_title, colour_scheme[0], screen, WIDTH/26, HEIGHT/12)

        # Draws simulation time
        if len(str(round(program_time, 2))) > 8:
            draw_text_centre(f'{str("{:.3e}".format(program_time))} s', arial_font_small_title, colour_scheme[0], screen, 78*WIDTH/100, HEIGHT/12)
        else:
            draw_text_centre(f'{str(round(program_time, 2))} s', arial_font_small_title, colour_scheme[0], screen, 78 * WIDTH / 100, HEIGHT / 12)

        # Draws lines
        pygame.draw.line(screen, colour_scheme[1], (0, 1), (WIDTH, 1), line_thickness)
        pygame.draw.line(screen, colour_scheme[1], (0, HEIGHT/6), (WIDTH, HEIGHT/6), line_thickness)
        pygame.draw.line(screen, colour_scheme[1], (WIDTH / 4, HEIGHT / 12), (11 * WIDTH / 16, HEIGHT / 12), line_thickness)
        # Draws buttons
        pygame.draw.rect(screen, start_button.colour, start_button.button, 2, 3)
        pygame.draw.rect(screen, time_slider_button.colour, time_slider_button.button, 0, 2)

        # Draws icons
        screen.blit(start_icon.image, (start_icon.x_position, start_icon.y_position))

        # Processes menu tab
        starting_distance, starting_height, max_height, horizontal_range, time_of_flight, launch_velocity, launch_angle, gravity, press_time, program_time, pause_time, projectile, left_click, menu_button, menu_open, launched, start_button, time_slider_button = projectile_motion_menu(colour_scheme, starting_distance, starting_height, starting_distance_box, starting_height_box, menu_button, menu_open, start_button, time_slider_button, launch_button, reset_button, launch_angle_box, launch_velocity_box, gravity_box, projectile, WIDTH, HEIGHT, launched, left_click, key_down, mouse_x, mouse_y, press_time, program_time, pause_time, max_height, horizontal_range, time_of_flight, launch_velocity, launch_angle, gravity)

        # Draws back button
        pygame.draw.rect(screen, back_button.colour, back_button.button, 2, 3)
        screen.blit(back_arrow.image, (back_arrow.x_position, back_arrow.y_position))

        pygame.display.update()
        clock.tick(FPS)
