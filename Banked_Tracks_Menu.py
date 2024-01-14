# Setting up Presets
from Presets import *
from Classes import *


def banked_tracks_menu(min_speed, max_speed, colour_scheme, lower_limit, upper_limit, speed_min, speed_max, mass_min, mass_max, gravity_min, gravity_max, mouse_move, mouse_release, menu_button, menu_open, start_button, friction_button, speed_slider_button_min, speed_slider_button, speed_slider_button_max, mass_slider_button_min, mass_slider_button, mass_slider_button_max, gravity_slider_button_min, gravity_slider_button, gravity_slider_button_max, track_angle_slider_button, friction_slider_button, WIDTH, HEIGHT, left_click, key_down, mouse_x, mouse_y, radius, period, angular_speed, speed, mass, gravity, track_angle, friction):
    arial_font_title = pygame.font.SysFont('arial', int(WIDTH / 20), 1)
    arial_font_header = pygame.font.SysFont('arial', int(WIDTH / 30), 1)
    arial_font_small_title = pygame.font.SysFont('arial', int(WIDTH / 38), 1)
    arial_font_text = pygame.font.SysFont('arial', int(WIDTH / 36), 0)
    arial_font_type = pygame.font.SysFont('arial', int(WIDTH / 50), 0)
    arial_font_label = pygame.font.SysFont('arial', int(WIDTH / 60), 0)
    # Menu button function
    if menu_open:
        menu_button.x_position = WIDTH/2
        menu_button.y_position = 2*HEIGHT/3
        menu_button.button.midtop = menu_button.x_position, menu_button.y_position
        menu_button.button_click(mouse_x, mouse_y, left_click)
        if menu_button.active:
            menu_open = False
            menu_button.x_position = WIDTH/2
            menu_button.y_position = HEIGHT
            menu_button.button.midbottom = (menu_button.x_position, menu_button.y_position)
            menu_button.active = False

        # Updates friction button and slider button
        friction_button.toggle_button_click(mouse_x, mouse_y, left_click)
        friction_slider_button.slider_button_click(mouse_x, mouse_y, left_click, mouse_move, mouse_release, WIDTH/4, 12*WIDTH/25, friction_slider_button.active)
        # friction button function
        if not friction_button.active:
            friction = (friction_slider_button.x_position - WIDTH/4) / (23*WIDTH/100)
            if track_angle:
                lower_limit = int((math.degrees(math.atan2(friction, 1)) * (23*WIDTH/100) / 90) + WIDTH/4) + 1
                upper_limit = int((math.degrees(math.atan2(1, friction)) * (23*WIDTH/100) / 90) + WIDTH/4)
        else:
            friction = 0

        # Updates input buttons
        speed_min = speed_slider_button_min.input_button_click(mouse_x, mouse_y, left_click, key_down, [speed_slider_button_max, mass_slider_button_min, mass_slider_button_max, gravity_slider_button_min, gravity_slider_button_max], speed_min, 6)
        speed_max = speed_slider_button_max.input_button_click(mouse_x, mouse_y, left_click, key_down, [speed_slider_button_min, mass_slider_button_min, mass_slider_button_max, gravity_slider_button_min, gravity_slider_button_max], speed_max, 6)
        mass_min = mass_slider_button_min.input_button_click(mouse_x, mouse_y, left_click, key_down, [speed_slider_button_min, speed_slider_button_max, mass_slider_button_max, gravity_slider_button_min, gravity_slider_button_max], mass_min, 6)
        mass_max = mass_slider_button_max.input_button_click(mouse_x, mouse_y, left_click, key_down, [speed_slider_button_min, speed_slider_button_max, mass_slider_button_min, gravity_slider_button_min, gravity_slider_button_max], mass_max, 6)
        gravity_min = gravity_slider_button_min.input_button_click(mouse_x, mouse_y, left_click, key_down, [speed_slider_button_min, speed_slider_button_max, mass_slider_button_min, mass_slider_button_max, gravity_slider_button_max], gravity_min, 6)
        gravity_max = gravity_slider_button_max.input_button_click(mouse_x, mouse_y, left_click, key_down, [speed_slider_button_min, speed_slider_button_max, mass_slider_button_min, mass_slider_button_max, gravity_slider_button_min], gravity_max, 6)

        speed = ((float(speed_max) - float(speed_min)) * (speed_slider_button.x_position - WIDTH/4) / (23*WIDTH/100)) + float(speed_min)
        mass = ((float(mass_max) - float(mass_min)) * (mass_slider_button.x_position - WIDTH/4) / (23*WIDTH/100)) + float(mass_min)
        gravity = ((float(gravity_max) - float(gravity_min)) * (gravity_slider_button.x_position - WIDTH/4) / (23*WIDTH/100)) + float(gravity_min)

        # Updates slider buttons
        speed_slider_button.slider_button_click(mouse_x, mouse_y, left_click, mouse_move, mouse_release, WIDTH/4, 12*WIDTH/25, speed_slider_button.active)
        mass_slider_button.slider_button_click(mouse_x, mouse_y, left_click, mouse_move, mouse_release, WIDTH/4, 12*WIDTH/25, mass_slider_button.active)
        gravity_slider_button.slider_button_click(mouse_x, mouse_y, left_click, mouse_move, mouse_release, WIDTH/4, 12*WIDTH/25, gravity_slider_button.active)
        if friction and track_angle:
            if friction == 1:
                track_angle_slider_button.button.centerx = 73*WIDTH/200
                track_angle_slider_button.x_position = 73*WIDTH/200
            elif lower_limit and upper_limit:
                track_angle_slider_button.slider_button_click(mouse_x, mouse_y, left_click, mouse_move, mouse_release, lower_limit, upper_limit, track_angle_slider_button.active)
                if track_angle_slider_button.x_position > upper_limit:
                    track_angle_slider_button.x_position = upper_limit
                elif track_angle_slider_button.x_position < lower_limit:
                    track_angle_slider_button.x_position = lower_limit
        else:
            track_angle_slider_button.slider_button_click(mouse_x, mouse_y, left_click, mouse_move, mouse_release, WIDTH/4, 12*WIDTH/25, track_angle_slider_button.active)
        track_angle = 90 * (track_angle_slider_button.x_position - WIDTH/4) / (23*WIDTH/100)

        # Draws menu overlay
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 2*HEIGHT/3, WIDTH, HEIGHT))
        if not friction_button.active:
            pygame.draw.circle(screen, colour_scheme[0], (54*WIDTH/100, 96*HEIGHT/100), 10)
        # Draws input buttons
        pygame.draw.rect(screen, speed_slider_button_min.colour, speed_slider_button_min.button, 1)  # Draws translational speed box
        pygame.draw.rect(screen, speed_slider_button_max.colour, speed_slider_button_max.button, 1)  # Draws translational speed box
        pygame.draw.rect(screen, mass_slider_button_min.colour, mass_slider_button_min.button, 1)  # Draws mass box
        pygame.draw.rect(screen, mass_slider_button_max.colour, mass_slider_button_max.button, 1)  # Draws mass box
        pygame.draw.rect(screen, gravity_slider_button_min.colour, gravity_slider_button_min.button, 1)  # Draws gravity box
        pygame.draw.rect(screen, gravity_slider_button_max.colour, gravity_slider_button_max.button, 1)  # Draws gravity box

        pygame.draw.rect(screen, menu_button.colour, menu_button.button, 0, 1)  # Draws menu button

        # Draw lines
        pygame.draw.line(screen, colour_scheme[0], (WIDTH/4, 72*HEIGHT/100), (12*WIDTH/25, 72*HEIGHT/100), line_thickness)
        pygame.draw.line(screen, colour_scheme[0], (WIDTH/4, 78*HEIGHT/100), (12*WIDTH/25, 78*HEIGHT/100), line_thickness)
        pygame.draw.line(screen, colour_scheme[0], (WIDTH/4, 84*HEIGHT/100), (12*WIDTH/25, 84*HEIGHT/100), line_thickness)
        pygame.draw.line(screen, colour_scheme[0], (WIDTH/4, 90*HEIGHT/100), (12*WIDTH/25, 90*HEIGHT/100), line_thickness)
        if friction and track_angle and lower_limit and upper_limit:
            pygame.draw.line(screen, (200, 10, 10), (WIDTH/4, 90*HEIGHT/100), (lower_limit, 90*HEIGHT/100), line_thickness)
            pygame.draw.line(screen, (200, 00, 00), (upper_limit, 90*HEIGHT/100), (12*WIDTH/25, 90*HEIGHT/100), line_thickness)
        pygame.draw.line(screen, colour_scheme[0], (WIDTH/4, 96*HEIGHT/100), (12*WIDTH/25, 96*HEIGHT/100), line_thickness)
        pygame.draw.line(screen, colour_scheme[0], (11*WIDTH/70, 2 * HEIGHT / 3), (11*WIDTH/70, HEIGHT), line_thickness)
        pygame.draw.line(screen, colour_scheme[0], (37*WIDTH/64, 2 * HEIGHT / 3), (37*WIDTH/64, HEIGHT), line_thickness)
        pygame.draw.line(screen, colour_scheme[0], (0, 2 * HEIGHT / 3), (WIDTH, 2 * HEIGHT / 3), line_thickness)  # Draws menu line

        # Draw menu open buttons
        pygame.draw.rect(screen, speed_slider_button.colour, speed_slider_button.button, 0, 2)
        pygame.draw.rect(screen, mass_slider_button.colour, mass_slider_button.button, 0, 2)
        pygame.draw.rect(screen, gravity_slider_button.colour, gravity_slider_button.button, 0, 2)
        pygame.draw.rect(screen, track_angle_slider_button.colour, track_angle_slider_button.button, 0, 2)
        pygame.draw.rect(screen, friction_slider_button.colour, friction_slider_button.button, 0, 2)
        pygame.draw.rect(screen, friction_button.colour, friction_button.button, 2, 2)

        # Draw text
        screen.blit(arial_font_type.render(speed_slider_button_min.text, True, colour_scheme[0]), (speed_slider_button_min.x_position + speed_slider_button_min.width/8, speed_slider_button_min.y_position - speed_slider_button_min.height/3))  # Draws launch angle number
        screen.blit(arial_font_type.render(speed_slider_button_max.text, True, colour_scheme[0]), (speed_slider_button_max.x_position + speed_slider_button_max.width/8, speed_slider_button_max.y_position - speed_slider_button_max.height/3))  # Draws launch angle number
        screen.blit(arial_font_type.render(mass_slider_button_min.text, True, colour_scheme[0]), (mass_slider_button_min.x_position + mass_slider_button_min.width/8, mass_slider_button_min.y_position - mass_slider_button_min.height/3))  # Draws launch angle number
        screen.blit(arial_font_type.render(mass_slider_button_max.text, True, colour_scheme[0]), (mass_slider_button_max.x_position + mass_slider_button_max.width/8, mass_slider_button_max.y_position - mass_slider_button_max.height/3))  # Draws launch angle number
        screen.blit(arial_font_type.render(gravity_slider_button_min.text, True, colour_scheme[0]), (gravity_slider_button_min.x_position + gravity_slider_button_min.width/8, gravity_slider_button_min.y_position - gravity_slider_button_min.height/3))  # Draws launch angle number
        screen.blit(arial_font_type.render(gravity_slider_button_max.text, True, colour_scheme[0]), (gravity_slider_button_max.x_position + gravity_slider_button_max.width/8, gravity_slider_button_max.y_position - gravity_slider_button_max.height/3))  # Draws launch angle number
        draw_text_midleft('0', arial_font_type, colour_scheme[0], screen, 9*WIDTH/47, 90*HEIGHT/100)
        draw_text_midleft('0', arial_font_type, colour_scheme[0], screen, 9*WIDTH/47, 96*HEIGHT/100)
        draw_text_midleft('90', arial_font_type, colour_scheme[0], screen, WIDTH/2, 90*HEIGHT/100)
        draw_text_midleft('1', arial_font_type, colour_scheme[0], screen, WIDTH/2, 96*HEIGHT/100)
        draw_text_midleft('Radius:', arial_font_small_title, colour_scheme[0], screen, 41*WIDTH/70, 72*HEIGHT/100)
        draw_text_midleft('Period:', arial_font_small_title, colour_scheme[0], screen, 41*WIDTH/70, 78*HEIGHT/100)
        draw_text_midleft('Angular Speed:', arial_font_small_title, colour_scheme[0], screen, 41*WIDTH/70, 84*HEIGHT/100)
        draw_text_midleft('Max Speed:', arial_font_small_title, colour_scheme[0], screen, 41*WIDTH/70, 90*HEIGHT/100)
        draw_text_midleft('Min Speed:', arial_font_small_title, colour_scheme[0], screen, 41*WIDTH/70, 96*HEIGHT/100)
        if len(str(round(radius, 2))) > 8:
            draw_text_midleft(f'{str("{:.3e}".format(radius))}m', arial_font_small_title, colour_scheme[0], screen, 47 * WIDTH / 70,72 * HEIGHT / 100)  # Draws max height
        else:
            draw_text_midleft(f'{round(radius, 2)}m', arial_font_small_title, colour_scheme[0], screen, 47*WIDTH/70, 72*HEIGHT/100)  # Draws max height
        if len(str(round(period, 2))) > 8:
            draw_text_midleft(f'{str("{:.3e}".format(period))}m', arial_font_small_title, colour_scheme[0], screen, 47 * WIDTH / 70,78 * HEIGHT / 100)  # Draws max height
        else:
            draw_text_midleft(f'{round(period, 2)}m', arial_font_small_title, colour_scheme[0], screen, 47*WIDTH/70, 78*HEIGHT/100)  # Draws max height
        if len(str(round(angular_speed, 2))) > 8:
            draw_text_midleft(f'{str("{:.3e}".format(angular_speed))}m', arial_font_small_title, colour_scheme[0], screen, 53 * WIDTH / 70,84 * HEIGHT / 100)  # Draws max height
        else:
            draw_text_midleft(f'{round(angular_speed, 2)}m', arial_font_small_title, colour_scheme[0], screen, 53*WIDTH/70, 84*HEIGHT/100)  # Draws max height
        if len(str(round(max_speed, 2))) > 8:
            draw_text_midleft(f'{str("{:.3e}".format(max_speed))}m', arial_font_small_title, colour_scheme[0], screen, 50 * WIDTH / 70,90 * HEIGHT / 100)  # Draws max height
        else:
            draw_text_midleft(f'{round(max_speed, 2)}m', arial_font_small_title, colour_scheme[0], screen, 50*WIDTH/70, 90*HEIGHT/100)  # Draws max height
        if len(str(round(min_speed, 2))) > 8:
            draw_text_midleft(f'{str("{:.3e}".format(min_speed))}m', arial_font_small_title, colour_scheme[0], screen, 50 * WIDTH / 70,96 * HEIGHT / 100)  # Draws max height
        else:
            draw_text_midleft(f'{round(min_speed, 2)}m', arial_font_small_title, colour_scheme[0], screen, 50*WIDTH/70, 96*HEIGHT/100)  # Draws max height

        draw_text_midleft(str(round(speed, 2)), arial_font_label, colour_scheme[0], screen, WIDTH/10, 72*HEIGHT/100)  # Draws launch angle text
        draw_text_midleft('Speed(ms-1):', arial_font_label, colour_scheme[0], screen, WIDTH/150, 72*HEIGHT/100)  # Draws launch angle text

        draw_text_midleft(str(round(mass, 2)), arial_font_label, colour_scheme[0], screen, WIDTH/14, 78*HEIGHT/100)  # Draws launch angle text
        draw_text_midleft('Mass(kg):', arial_font_label, colour_scheme[0], screen, WIDTH/150, 78*HEIGHT/100)  # Draws launch velocity text

        draw_text_midleft(str(round(gravity, 2)), arial_font_label, colour_scheme[0], screen, 19*WIDTH/200, 84*HEIGHT/100)  # Draws launch angle text
        draw_text_midleft('Gravity(ms-2):', arial_font_label, colour_scheme[0], screen, WIDTH/150, 84*HEIGHT/100)  # Draws gravity text

        draw_text_midleft(str(round(track_angle, 2)), arial_font_label, colour_scheme[0], screen, 18*WIDTH/180, 9*HEIGHT/10)  # Draws launch angle text
        draw_text_midleft('Track angle(°):', arial_font_label, colour_scheme[0], screen, WIDTH/150, 9*HEIGHT/10)  # Draws track angle text

        draw_text_midleft(str(round(friction, 3)), arial_font_label, colour_scheme[0], screen, WIDTH/17, 96*HEIGHT/100)  # Draws launch angle text
        draw_text_midleft('Friction:', arial_font_label, colour_scheme[0], screen, WIDTH/150, 96*HEIGHT/100)  # Draws friction text
    else:

        # Menu closed display
        menu_button.button_click(mouse_x, mouse_y, left_click)
        if menu_button.active:
            menu_open = True
            menu_button.active = False
        pygame.draw.rect(screen, menu_button.colour, menu_button.button, 0, 1)
        pygame.draw.line(screen, colour_scheme[0], (0, HEIGHT - 3), (WIDTH, HEIGHT - 3), line_thickness)

    # Returns values
    return lower_limit, upper_limit, speed_min, speed_max, mass_min, mass_max, gravity_min, gravity_max, radius, period, angular_speed, speed, mass, gravity, track_angle, track_angle, friction, left_click, menu_button, menu_open, start_button
