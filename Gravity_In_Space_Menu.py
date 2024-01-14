from Presets import *
from Classes import *


def gravity_in_space_menu(colour_scheme, planet_array, menu_button, menu_open, start_button, reset_button, radius_box, mass_box, WIDTH, HEIGHT, left_click, key_down, mouse_x, mouse_y, radius, mass):
    arial_font_title = pygame.font.SysFont('arial', int(WIDTH / 20), 1)
    arial_font_header = pygame.font.SysFont('arial', int(WIDTH / 30), 1)
    arial_font_small_title = pygame.font.SysFont('arial', int(WIDTH / 38), 1)
    arial_font_text = pygame.font.SysFont('arial', int(WIDTH / 36), 0)
    arial_font_type = pygame.font.SysFont('arial', int(WIDTH / 50), 0)
    arial_font_label = pygame.font.SysFont('arial', int(WIDTH / 60), 0)
    # Menu button function
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
        radius = radius_box.input_button_click(mouse_x, mouse_y, left_click, key_down, [mass_box], radius, 3)
        mass = mass_box.input_button_click(mouse_x, mouse_y, left_click, key_down, [radius_box], mass, 7)

        # Updates launch button
        reset_button.button_click(mouse_x, mouse_y, left_click)
        # Launch button function
        if reset_button.active:
            planet_array = []
            reset_button.active = False

        # Draws menu overlay
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 3*HEIGHT/4, WIDTH, HEIGHT))
        # Draw menu open buttons
        pygame.draw.rect(screen, menu_button.colour, menu_button.button, 0, 1)  # Draws menu button
        pygame.draw.rect(screen, reset_button.colour, reset_button.button, 1, 1)  # Draws launch button
        pygame.draw.rect(screen, radius_box.colour, radius_box.button, 1)  # Draws force box
        pygame.draw.rect(screen, mass_box.colour, mass_box.button, 1)  # Draws mass box

        # Draw line
        pygame.draw.line(screen, colour_scheme[0], (0, 3*HEIGHT/4), (WIDTH, 3*HEIGHT/4), line_thickness)  # Draws menu line

        # Draw text
        draw_text_centre(reset_button.text, arial_font_small_title, reset_button.colour, screen, reset_button.x_position + reset_button.width/2, reset_button.y_position + reset_button.height/2)  # Draws launch button label

        screen.blit(arial_font_type.render(radius_box.text, True, colour_scheme[0]), (radius_box.x_position + radius_box.width/8, radius_box.y_position + radius_box.height/8))  # Draws launch angle number
        draw_text_midleft('Radius(m):', arial_font_small_title, colour_scheme[0], screen, 3*WIDTH/50, 177*HEIGHT/200)  # Draws launch angle text

        screen.blit(arial_font_type.render(mass_box.text, True, colour_scheme[0]), (mass_box.x_position + mass_box.width/20, mass_box.y_position + mass_box.height/8))  # Draws launch velocity number
        draw_text_midleft('Mass(x10^10kg):', arial_font_small_title, colour_scheme[0], screen, 17*WIDTH/50, 177*HEIGHT/200)  # Draws launch velocity text

    else:
        # Menu closed display
        menu_button.button_click(mouse_x, mouse_y, left_click)
        if menu_button.active:
            menu_open = True
            menu_button.active = False
        pygame.draw.rect(screen, menu_button.colour, menu_button.button, 0, 1)
        pygame.draw.line(screen, colour_scheme[0], (0, HEIGHT - 3), (WIDTH, HEIGHT - 3), line_thickness)

    # Returns values
    return planet_array, radius, mass, left_click, menu_button, menu_open, start_button
