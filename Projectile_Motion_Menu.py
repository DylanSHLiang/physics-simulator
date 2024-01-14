from Projectile_Motion_Stats_Calculator import projectile_motion_stats_calculator
from Classes import *
from Presets import *


def projectile_motion_menu(colour_scheme, starting_distance, starting_height, starting_distance_box, starting_height_box, menu_button, menu_open, start_button, time_slider_button, launch_button, reset_button, launch_angle_box, launch_velocity_box,
                           gravity_box, projectile, WIDTH, HEIGHT, launched, left_click, key_down,
                           mouse_x, mouse_y, press_time, program_time, pause_time, max_height, horizontal_range, time_of_flight,
                           launch_velocity, launch_angle, gravity):
    # Adjusts font sizes
    arial_font_title = pygame.font.SysFont('arial', int(WIDTH / 20), 1)
    arial_font_header = pygame.font.SysFont('arial', int(WIDTH / 30), 1)
    arial_font_small_title = pygame.font.SysFont('arial', int(WIDTH / 38), 1)
    arial_font_text = pygame.font.SysFont('arial', int(WIDTH / 36), 0)
    arial_font_type = pygame.font.SysFont('arial', int(WIDTH / 50), 0)
    arial_font_label = pygame.font.SysFont('arial', int(WIDTH / 60), 0)

    # Updates menu button
    if menu_open:
        menu_button.x_position = WIDTH/2
        menu_button.y_position = 3*HEIGHT/4
        menu_button.button.midtop = menu_button.x_position, menu_button.y_position
        menu_button.button_click(mouse_x, mouse_y, left_click)
        if menu_button.active:
            menu_open = False
            menu_button.x_position = WIDTH/2
            menu_button.y_position = HEIGHT
            menu_button.button.midbottom = (menu_button.x_position, menu_button.y_position)
            menu_button.active = False

        # Updates launch button
        if launch_angle_box.text and launch_angle_box.text != '.' and launch_angle_box.text != '0' and launch_velocity_box.text and launch_velocity_box.text != '.' and launch_velocity_box.text != '0' and gravity_box.text and gravity_box.text != '.' and gravity_box.text != '0':
            launch_button.one_time_button_click(mouse_x, mouse_y, left_click)
        if launch_button.active:
            if not launched:
                press_time = time.time()
                launched = True
                time_slider_button.x_position = WIDTH/4
                time_slider_button.button.centerx = time_slider_button.x_position
                launch_angle = math.radians(float(launch_angle_box.text))
                launch_velocity = float(launch_velocity_box.text)
                gravity = float(gravity_box.text)
                max_height, horizontal_range, time_of_flight = projectile_motion_stats_calculator(launch_velocity, launch_angle, gravity, projectile, WIDTH, HEIGHT)

        # Updates reset button
        reset_button.button_click(mouse_x, mouse_y, left_click)
        if reset_button.active:
            start_button.active = True
            launch_button.active = False
            launched = False
            program_time = 0
            pause_time = 0
            projectile = ball((100, 100, 100), WIDTH/10, 2*HEIGHT/3 - projectile.radius, WIDTH/10, 2*HEIGHT/3 - projectile.radius, None, None, None, None, 10)
            time_slider_button.x_position = WIDTH/4
            reset_button.active = False

        # Updates input buttons
        launch_angle = launch_angle_box.input_button_click(mouse_x, mouse_y, left_click, key_down, [launch_velocity_box, gravity_box, starting_distance_box, starting_height_box], launch_angle, 3)
        if launch_angle_box.text and launch_angle_box.text != '.':
            if float(launch_angle_box.text) > 90:
                launch_angle_box.text = str(90)
        launch_velocity_box.input_button_click(mouse_x, mouse_y, left_click, key_down, [launch_angle_box, gravity_box, starting_distance_box, starting_height_box], launch_velocity, 4)
        gravity_box.input_button_click(mouse_x, mouse_y, left_click, key_down, [launch_angle_box, launch_velocity_box, starting_distance_box, starting_height_box], gravity, 4)
        if not launched:
            starting_distance = starting_distance_box.input_button_click(mouse_x, mouse_y, left_click, key_down, [launch_angle_box, launch_velocity_box, gravity_box, starting_height_box], starting_distance, 6)
            starting_height = starting_height_box.input_button_click(mouse_x, mouse_y, left_click, key_down, [launch_angle_box, launch_velocity_box, gravity_box, starting_distance_box], starting_height, 6)
        else:
            starting_distance_box.input_button_click(mouse_x, mouse_y, left_click, key_down, [launch_angle_box, launch_velocity_box, gravity_box, starting_height_box], starting_distance, 6)
            starting_height_box.input_button_click(mouse_x, mouse_y, left_click, key_down, [launch_angle_box, launch_velocity_box, gravity_box, starting_distance_box], starting_height, 6)

        # Draws menu overlay
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, WIDTH, 3*HEIGHT/4, HEIGHT))
        # Draw menu open buttons
        pygame.draw.rect(screen, menu_button.colour, menu_button.button, 0, 1)  # Draws menu button
        pygame.draw.rect(screen, launch_button.colour, launch_button.button, 1)  # Draws launch button
        pygame.draw.rect(screen, reset_button.colour, reset_button.button, 1)  # Draws reset button
        pygame.draw.rect(screen, launch_angle_box.colour, launch_angle_box.button, 1)  # Draws launch angle box
        pygame.draw.rect(screen, launch_velocity_box.colour, launch_velocity_box.button, 1)  # Draws launch velocity box
        pygame.draw.rect(screen, gravity_box.colour, gravity_box.button, 1)  # Draws gravity box
        pygame.draw.rect(screen, starting_distance_box.colour, starting_distance_box.button, 1)  # Draws gravity box
        pygame.draw.rect(screen, starting_height_box.colour, starting_height_box.button, 1)  # Draws gravity box

        # Draw line
        pygame.draw.line(screen, colour_scheme[0], (0, 3*HEIGHT/4), (WIDTH, 3*HEIGHT/4), line_thickness)
        pygame.draw.line(screen, colour_scheme[0], (2*WIDTH/9, 3*HEIGHT/4), (2*WIDTH/9, HEIGHT), line_thickness)  # Draws menu line
        pygame.draw.line(screen, colour_scheme[0], (10*WIDTH/17, 3*HEIGHT/4), (10*WIDTH/17, HEIGHT), line_thickness)

        # Draw text
        draw_text_centre(launch_button.text, arial_font_small_title, launch_button.colour, screen, 317*WIDTH/340, 73*HEIGHT/90)  # Draws launch button label
        draw_text_centre(reset_button.text, arial_font_small_title, reset_button.colour, screen, 277*WIDTH/340, 73*HEIGHT/90)  # Draws reset button label
        draw_text_midleft('max height:', arial_font_small_title, colour_scheme[0], screen, 3*WIDTH/13, 87*HEIGHT/108)
        draw_text_midleft('horizontal range:', arial_font_small_title, colour_scheme[0], screen, 3*WIDTH/13, 95*HEIGHT/108)
        draw_text_midleft('time of flight:', arial_font_small_title, colour_scheme[0], screen, 3*WIDTH/13, 103*HEIGHT/108)
        if launched:
            if len(str(round(max_height, 2))) > 8:
                draw_text_midleft(f'{str("{:.3e}".format(max_height))}m', arial_font_small_title, colour_scheme[0], screen, 71*WIDTH/200, 87*HEIGHT/108)  # Draws max height
            else:
                draw_text_midleft(f'{round(max_height, 2)}m', arial_font_small_title, colour_scheme[0], screen, 71*WIDTH/200, 87*HEIGHT/108)  # Draws max height
            if len(str(round(horizontal_range, 2))) > 8:
                draw_text_midleft(f'{str("{:.3e}".format(horizontal_range))}m', arial_font_small_title, colour_scheme[0], screen, 41*WIDTH/100, 95*HEIGHT/108)  # Draws max height
            else:
                draw_text_midleft(f'{round(horizontal_range, 2)}m', arial_font_small_title, colour_scheme[0], screen, 41*WIDTH/100, 95*HEIGHT/108)  # Draws max height
            if len(str(round(time_of_flight, 2))) > 8:
                draw_text_midleft(f'{str("{:.3e}".format(time_of_flight))}m', arial_font_small_title, colour_scheme[0], screen, 37*WIDTH/100, 103*HEIGHT/108)  # Draws max height
            else:
                draw_text_midleft(f'{round(time_of_flight, 2)}m', arial_font_small_title, colour_scheme[0], screen, 37*WIDTH/100, 103*HEIGHT/108)  # Draws max height

        screen.blit(arial_font_type.render(launch_angle_box.text, True, colour_scheme[0]), (launch_angle_box.x_position + launch_angle_box.width/8, launch_angle_box.y_position + launch_angle_box.width/8))  # Draws launch angle number
        draw_text_midleft('Launch Angle(°):', arial_font_label, colour_scheme[0], screen, WIDTH/150, 87*HEIGHT/108)  # Draws launch angle text

        screen.blit(arial_font_type.render(launch_velocity_box.text, True, colour_scheme[0]), (launch_velocity_box.x_position + launch_angle_box.width/8, launch_velocity_box.y_position + launch_angle_box.width/8))  # Draws launch velocity number
        draw_text_midleft('Launch Velocity(ms-1):', arial_font_label, colour_scheme[0], screen, WIDTH/150, 95*HEIGHT/108)  # Draws launch velocity text

        screen.blit(arial_font_type.render(gravity_box.text, True, colour_scheme[0]), (gravity_box.x_position + launch_angle_box.width/8, gravity_box.y_position + launch_angle_box.width/8))  # Draws gravity number
        draw_text_midleft('Gravity(ms-2):', arial_font_label, colour_scheme[0], screen, WIDTH/150, 103*HEIGHT/108)  # Draws gravity text

        screen.blit(arial_font_type.render(starting_distance_box.text, True, colour_scheme[0]), (starting_distance_box.x_position + launch_angle_box.width/8, starting_distance_box.y_position + launch_angle_box.width/8))  # Draws gravity number
        draw_text_midleft('Initial Distance (m)', arial_font_label, colour_scheme[0], screen, 33*WIDTH/54, 71*HEIGHT/80)  # Draws gravity text

        screen.blit(arial_font_type.render(starting_height_box.text, True, colour_scheme[0]), (starting_height_box.x_position + launch_angle_box.width/8, starting_height_box.y_position + launch_angle_box.width/8))  # Draws gravity number
        draw_text_midleft('Initial Height (m)', arial_font_label, colour_scheme[0], screen, 33*WIDTH/54, 77*HEIGHT/80)  # Draws gravity text
    else:

        # Menu closed display
        menu_button.button_click(mouse_x, mouse_y, left_click)
        if menu_button.active:
            menu_open = True
            menu_button.active = False
        pygame.draw.rect(screen, menu_button.colour, menu_button.button, 0, 1)
        pygame.draw.line(screen, colour_scheme[0], (0, HEIGHT - 3), (WIDTH, HEIGHT - 3), line_thickness)

    # Returns values
    if launched:
        return starting_distance, starting_height, max_height, horizontal_range, time_of_flight, launch_velocity, launch_angle, gravity, press_time, program_time, pause_time, projectile, left_click, menu_button, menu_open, launched, start_button, time_slider_button
    else:
        return starting_distance, starting_height, 0, 0, 0, launch_velocity, launch_angle, gravity, 0, 0, 0, projectile, left_click, menu_button, menu_open, launched, start_button, time_slider_button
