from Presets import *
from Circular_Motion_Menu import circular_motion_menu
from Circular_Motion_Stats_Calculator import circular_motion_stats_calculator
from Classes import *


def circular_motion(FPS, WIDTH, HEIGHT, colour_scheme):
    #Adjusts font sizes
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
    start_icon.x_position, start_icon.y_position, start_icon.image = 187 * WIDTH / 216, HEIGHT / 20, pygame.transform.scale(start_icon.picture, (WIDTH / 24, HEIGHT / 15))
    start_icon.image = image_colour_changer(start_icon.image, start_icon.colour, colour_scheme[2])
    start_button = button(8*WIDTH/9, HEIGHT/12, WIDTH / 25, WIDTH / 25, colour_scheme[0], colour_scheme[2], None, start_icon.image, True)
    start_button.button.center = (start_button.x_position, start_button.y_position)
    menu_button = button(WIDTH/2, HEIGHT, WIDTH/22, HEIGHT/30, colour_scheme[0], colour_scheme[2], None, None, None)
    menu_button.button.midbottom = menu_button.x_position, menu_button.y_position
    show_path_button = button(WIDTH/4, HEIGHT/18, WIDTH/8, HEIGHT/15, colour_scheme[0], colour_scheme[2], "Show Path", None, None)
    force_slider_button_min = button(WIDTH/6, 87*HEIGHT/108, WIDTH/17, WIDTH/34, colour_scheme[0], colour_scheme[2], '0', None, None)
    force_slider_button_min.button.centery = force_slider_button_min.y_position
    force_slider_button = button(2*WIDTH/6, 87*HEIGHT/108, WIDTH/60, WIDTH/30, colour_scheme[0], colour_scheme[2], None, None, None)
    force_slider_button.button.centery = force_slider_button.y_position
    force_slider_button_max = button(3*WIDTH/6, 87*HEIGHT/108, WIDTH/17, WIDTH/34, colour_scheme[0], colour_scheme[2], '0', None, None)
    force_slider_button_max.button.centery = force_slider_button_max.y_position
    mass_slider_button_min = button(WIDTH/6, 95*HEIGHT/108, WIDTH/17, WIDTH/34, colour_scheme[0], colour_scheme[2], '0', None, None)
    mass_slider_button_min.button.centery = mass_slider_button_min.y_position
    mass_slider_button = button(2*WIDTH/6, 95*HEIGHT/108, WIDTH/60, WIDTH/30, colour_scheme[0], colour_scheme[2], None, None, None)
    mass_slider_button.button.centery = mass_slider_button.y_position
    mass_slider_button_max = button(3*WIDTH/6, 95*HEIGHT/108, WIDTH/17, WIDTH/34, colour_scheme[0], colour_scheme[2], '0', None, None)
    mass_slider_button_max.button.centery = mass_slider_button_max.y_position
    speed_slider_button_min = button(WIDTH/6, 103*HEIGHT/108, WIDTH/17, WIDTH/34, colour_scheme[0], colour_scheme[2], '0', None, None)
    speed_slider_button_min.button.centery = speed_slider_button_min.y_position
    speed_slider_button = button(2*WIDTH/6, 103*HEIGHT/108, WIDTH/60, WIDTH/30, colour_scheme[0], colour_scheme[2], None, None, None)
    speed_slider_button.button.centery = speed_slider_button.y_position
    speed_slider_button_max = button(3*WIDTH/6, 103*HEIGHT/108, WIDTH/17, WIDTH/34, colour_scheme[0], colour_scheme[2], '0', None, None)
    speed_slider_button_max.button.centery = speed_slider_button_max.y_position
    circle = ball(colour_scheme[2], WIDTH/2, HEIGHT/2, WIDTH/2, HEIGHT/2, 0, 0, 0, 0, 10)

    # Sets variables
    menu_open = True
    force_min = 0
    force_max = 0
    mass_min = 0
    mass_max = 0
    speed_min = 0
    speed_max = 0
    radius = 0
    period = 0
    angular_speed = 0
    force = 0
    mass = 0
    speed = 0
    pause_time = 0
    start_time = time.time()
    program_time = 0
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

        # Updates start button
        start_button.toggle_button_click(mouse_x, mouse_y, left_click)

        # Updates show path button
        show_path_button.toggle_button_click(mouse_x, mouse_y, left_click)

        if show_path_button.active:
            pygame.draw.circle(screen, colour_scheme[0], (WIDTH/2, HEIGHT/2), math.sqrt(radius) * 10, 2)

        # Updates ball and time
        if force and mass and speed:
            if start_button.active:
                program_time = time.time() - start_time - pause_time
                radius, period, angular_speed = circular_motion_stats_calculator(force, mass, speed)
                angle = 2 * math.pi * (program_time % period) / period
                circle.x_acceleration = math.cos(angle) * force / mass
                circle.y_acceleration = math.sin(angle) * force / mass
                circle.x_velocity = math.cos(angle)
                circle.y_velocity = math.sin(angle)
                circle.x_position = WIDTH/2 - math.cos(angle) * math.sqrt(radius) * 10
                circle.y_position = HEIGHT/2 - math.sin(angle) * math.sqrt(radius) * 10
                if 0 < circle.x_position < WIDTH and 0 < circle.y_position < HEIGHT:
                    pygame.draw.circle(screen, colour_scheme[1], (circle.x_position, circle.y_position), circle.radius)
            else:
                pause_time = time.time() - start_time - program_time
                if 0 < circle.x_position < WIDTH and 0 < circle.y_position < HEIGHT:
                    pygame.draw.circle(screen, colour_scheme[1], (circle.x_position, circle.y_position), circle.radius)

        else:
            pygame.draw.circle(screen, colour_scheme[1], (WIDTH/2, HEIGHT/2), circle.radius)

        # Draws Overlay
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 0, WIDTH, HEIGHT/6))
        # Draws text
        draw_text_midleft('Circular Motion', arial_font_small_title, colour_scheme[0], screen, WIDTH/26, HEIGHT/12)
        draw_text_centre(show_path_button.text, arial_font_small_title, show_path_button.colour, screen, 5*WIDTH/16, 11*HEIGHT/120)

        # Draws buttons
        pygame.draw.rect(screen, start_button.colour, start_button.button, 2, 3)
        pygame.draw.rect(screen, show_path_button.colour, show_path_button.button, 2)

        # Draws icons
        screen.blit(start_icon.image, (start_icon.x_position, start_icon.y_position))

        # Draws lines
        pygame.draw.line(screen, colour_scheme[1], (0, HEIGHT/6), (WIDTH, HEIGHT/6), line_thickness)
        pygame.draw.line(screen, colour_scheme[1], (0, 1), (WIDTH, 1), line_thickness)

        # Processes menu
        force_min, force_max, mass_min, mass_max, speed_min, speed_max, radius, period, angular_speed, force, mass, speed, left_click, menu_button, menu_open, start_button, program_time, pause_time, circle = circular_motion_menu(colour_scheme, force_min, force_max, mass_min, mass_max, speed_min, speed_max, menu_button, menu_open, start_button, force_slider_button_min, force_slider_button, force_slider_button_max, mass_slider_button_min, mass_slider_button, mass_slider_button_max, speed_slider_button_min, speed_slider_button, speed_slider_button_max, WIDTH, HEIGHT, left_click, mouse_move, mouse_release, key_down, mouse_x, mouse_y, radius, period, angular_speed, force, mass, speed, program_time, pause_time, circle)

        # Draws back button
        pygame.draw.rect(screen, back_button.colour, back_button.button, 2, 3)
        screen.blit(back_arrow.image, (back_arrow.x_position, back_arrow.y_position))

        pygame.display.update()
        clock.tick(FPS)
