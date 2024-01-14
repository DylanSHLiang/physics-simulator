from Presets import *
from Classes import *


def circular_motion_menu(colour_scheme, force_min, force_max, mass_min, mass_max, speed_min, speed_max, menu_button, menu_open, start_button, force_slider_button_min, force_slider_button, force_slider_button_max, mass_slider_button_min, mass_slider_button, mass_slider_button_max, speed_slider_button_min, speed_slider_button, speed_slider_button_max, WIDTH, HEIGHT, left_click, mouse_move, mouse_release, key_down, mouse_x, mouse_y, radius, period, angular_speed, force, mass, speed, program_time, pause_time, circle):
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

        # Updates input buttons
        force_min = force_slider_button_min.input_button_click(mouse_x, mouse_y, left_click, key_down, [force_slider_button_max, mass_slider_button_min, mass_slider_button_max, speed_slider_button_min, speed_slider_button_max], force_min, 6)
        force_max = force_slider_button_max.input_button_click(mouse_x, mouse_y, left_click, key_down, [force_slider_button_min, mass_slider_button_min, mass_slider_button_max, speed_slider_button_min, speed_slider_button_max], force_max, 6)
        mass_min = mass_slider_button_min.input_button_click(mouse_x, mouse_y, left_click, key_down, [force_slider_button_min, force_slider_button_max, mass_slider_button_max, speed_slider_button_min, speed_slider_button_max], mass_min, 6)
        mass_max = mass_slider_button_max.input_button_click(mouse_x, mouse_y, left_click, key_down, [force_slider_button_min, force_slider_button_max, mass_slider_button_min, speed_slider_button_min, speed_slider_button_max], mass_max, 6)
        speed_min = speed_slider_button_min.input_button_click(mouse_x, mouse_y, left_click, key_down, [force_slider_button_min, force_slider_button_max, mass_slider_button_min, mass_slider_button_max, speed_slider_button_max], speed_min, 6)
        speed_max = speed_slider_button_max.input_button_click(mouse_x, mouse_y, left_click, key_down, [force_slider_button_min, force_slider_button_max, mass_slider_button_min, mass_slider_button_max, speed_slider_button_min], speed_max, 6)

        # Updates slider buttons
        force_slider_button.slider_button_click(mouse_x, mouse_y, left_click, mouse_move, mouse_release, WIDTH/4, 12*WIDTH/25, force_slider_button.active)
        force = ((float(force_max) - float(force_min)) * (force_slider_button.x_position - WIDTH/4) / (23*WIDTH/100)) + float(force_min)
        mass_slider_button.slider_button_click(mouse_x, mouse_y, left_click, mouse_move, mouse_release, WIDTH/4, 12*WIDTH/25, mass_slider_button.active)
        mass = ((float(mass_max) - float(mass_min)) * (mass_slider_button.x_position - WIDTH/4) / (23*WIDTH/100)) + float(mass_min)
        speed_slider_button.slider_button_click(mouse_x, mouse_y, left_click, mouse_move, mouse_release, WIDTH/4, 12*WIDTH/25, speed_slider_button.active)
        speed = ((float(speed_max) - float(speed_min)) * (speed_slider_button.x_position - WIDTH/4) / (23*WIDTH/100)) + float(speed_min)

        # Draws menu overlay
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 3*HEIGHT/4, WIDTH, HEIGHT))

        # Draw buttons
        pygame.draw.rect(screen, menu_button.colour, menu_button.button, 0, 1)  # Draws menu button

        # Draw line
        pygame.draw.line(screen, colour_scheme[0], (WIDTH/4, 87*HEIGHT/108), (12*WIDTH/25, 87*HEIGHT/108), line_thickness)
        pygame.draw.line(screen, colour_scheme[0], (WIDTH/4, 95*HEIGHT/108), (12*WIDTH/25, 95*HEIGHT/108), line_thickness)
        pygame.draw.line(screen, colour_scheme[0], (WIDTH/4, 103*HEIGHT/108), (12*WIDTH/25, 103*HEIGHT/108), line_thickness)
        pygame.draw.line(screen, colour_scheme[0], (23*WIDTH/152, 3 * HEIGHT / 4), (23*WIDTH/152, HEIGHT), line_thickness)
        pygame.draw.line(screen, colour_scheme[0], (54*WIDTH/95, 3 * HEIGHT / 4), (54*WIDTH/95, HEIGHT), line_thickness)
        pygame.draw.line(screen, colour_scheme[0], (0, 3 * HEIGHT / 4), (WIDTH, 3 * HEIGHT / 4), line_thickness)  # Draws menu line

        pygame.draw.rect(screen, force_slider_button.colour, force_slider_button.button, 0, 2)  # Draws force box
        pygame.draw.rect(screen, mass_slider_button.colour, mass_slider_button.button, 0, 2)  # Draws mass box
        pygame.draw.rect(screen, speed_slider_button.colour, speed_slider_button.button, 0, 2)  # Draws temp box

        # Draw input buttons
        pygame.draw.rect(screen, force_slider_button_min.colour, force_slider_button_min.button, 1, 1)  # Draws force box
        pygame.draw.rect(screen, force_slider_button_max.colour, force_slider_button_max.button, 1, 1)  # Draws force box
        pygame.draw.rect(screen, mass_slider_button_min.colour, mass_slider_button_min.button, 1, 1)  # Draws mass box
        pygame.draw.rect(screen, mass_slider_button_max.colour, mass_slider_button_max.button, 1, 1)  # Draws mass box
        pygame.draw.rect(screen, speed_slider_button_min.colour, speed_slider_button_min.button, 1, 1)  # Draws temp box
        pygame.draw.rect(screen, speed_slider_button_max.colour, speed_slider_button_max.button, 1, 1)  # Draws temp box

        # Draw text
        screen.blit(arial_font_type.render(force_slider_button_min.text, True, colour_scheme[0]), (force_slider_button_min.x_position + force_slider_button_min.width/16, force_slider_button_min.y_position - force_slider_button_min.width/6))  # Draws launch angle number
        screen.blit(arial_font_type.render(force_slider_button_max.text, True, colour_scheme[0]), (force_slider_button_max.x_position + force_slider_button_max.width/16, force_slider_button_max.y_position - + force_slider_button_max.width/6))  # Draws launch angle number
        screen.blit(arial_font_type.render(mass_slider_button_min.text, True, colour_scheme[0]), (mass_slider_button_min.x_position + mass_slider_button_min.width/16, mass_slider_button_min.y_position - + mass_slider_button_min.width/6))  # Draws launch angle number
        screen.blit(arial_font_type.render(mass_slider_button_max.text, True, colour_scheme[0]), (mass_slider_button_max.x_position + mass_slider_button_max.width/16, mass_slider_button_max.y_position - + mass_slider_button_max.width/6))  # Draws launch angle number
        screen.blit(arial_font_type.render(speed_slider_button_min.text, True, colour_scheme[0]), (speed_slider_button_min.x_position + speed_slider_button_min.width/16, speed_slider_button_min.y_position - + speed_slider_button_min.width/6))  # Draws launch angle number
        screen.blit(arial_font_type.render(speed_slider_button_max.text, True, colour_scheme[0]), (speed_slider_button_max.x_position + speed_slider_button_max.width/16, speed_slider_button_max.y_position - + speed_slider_button_max.width/6))  # Draws launch angle number
        draw_text_midleft('Radius:', arial_font_small_title, colour_scheme[0], screen, 29*WIDTH/50, 87*HEIGHT/108)
        draw_text_midleft('Period:', arial_font_small_title, colour_scheme[0], screen, 29*WIDTH/50, 95*HEIGHT/108)
        draw_text_midleft('Angular Speed:', arial_font_small_title, colour_scheme[0], screen, 29*WIDTH/50, 103*HEIGHT/108)
        if len(str(round(radius, 2))) > 8:
            draw_text_midleft(f'{str("{:.3e}".format(radius))}m', arial_font_small_title, colour_scheme[0], screen, 67*WIDTH/100, 87*HEIGHT/108)  # Draws max height
        else:
            draw_text_midleft(f'{round(radius, 2)}m', arial_font_small_title, colour_scheme[0], screen, 67*WIDTH/100, 87*HEIGHT/108)  # Draws max height
        if len(str(round(period, 2))) > 8:
            draw_text_midleft(f'{str("{:.3e}".format(period))}m', arial_font_small_title, colour_scheme[0], screen, 133*WIDTH/200, 95*HEIGHT/108)  # Draws max height
        else:
            draw_text_midleft(f'{round(period, 2)}m', arial_font_small_title, colour_scheme[0], screen, 133*WIDTH/200, 95*HEIGHT/108)  # Draws max height
        if len(str(round(angular_speed, 2))) > 8:
            draw_text_midleft(f'{str("{:.3e}".format(angular_speed))}m', arial_font_small_title, colour_scheme[0], screen, 75*WIDTH/100, 103*HEIGHT/108)  # Draws max height
        else:
            draw_text_midleft(f'{round(angular_speed, 2)}m', arial_font_small_title, colour_scheme[0], screen, 75*WIDTH/100, 103*HEIGHT/108)  # Draws max height

        draw_text_midleft(str(round(force, 2)), arial_font_label, colour_scheme[0], screen, 17*WIDTH/240, 87*HEIGHT/108)  # Draws launch angle text
        draw_text_midleft('Force(N):', arial_font_label, colour_scheme[0], screen, WIDTH/150, 87*HEIGHT/108)  # Draws launch angle text

        draw_text_midleft(str(round(mass, 2)), arial_font_label, colour_scheme[0], screen, 17*WIDTH/240, 95*HEIGHT/108)  # Draws launch angle text
        draw_text_midleft('Mass(kg):', arial_font_label, colour_scheme[0], screen, WIDTH/150, 95*HEIGHT/108)  # Draws launch velocity text

        draw_text_midleft(str(round(speed, 2)), arial_font_label, colour_scheme[0], screen, 11*WIDTH/120, 103*HEIGHT/108)  # Draws launch angle text
        draw_text_midleft('Speed(ms-2):', arial_font_label, colour_scheme[0], screen, WIDTH/150, 103*HEIGHT/108)  # Draws gravity text
    else:

        # Menu closed display
        menu_button.button_click(mouse_x, mouse_y, left_click)
        if menu_button.active:
            menu_open = True
            menu_button.active = False
        pygame.draw.rect(screen, menu_button.colour, menu_button.button, 0, 1)
        pygame.draw.line(screen, colour_scheme[0], (0, HEIGHT - 3), (WIDTH, HEIGHT - 3), line_thickness)

    # Returns values
    return force_min, force_max, mass_min, mass_max, speed_min, speed_max, radius, period, angular_speed, force, mass, speed, left_click, menu_button, menu_open, start_button, program_time, pause_time, circle
