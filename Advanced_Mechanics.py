from Presets import *
from Projectile_Motion import projectile_motion
from Circular_Motion import circular_motion
from Banked_Tracks_Side_View import banked_tracks_side_view
from Gravity_In_Space import gravity_in_space


def advanced_mechanics(FPS, WIDTH, HEIGHT, colour_scheme):
    # Adjusts font sizes
    arial_font_title = pygame.font.SysFont('arial', int(WIDTH / 20), 1)
    arial_font_header = pygame.font.SysFont('arial', int(WIDTH / 30), 1)
    arial_font_small_title = pygame.font.SysFont('arial', int(WIDTH / 38), 1)
    arial_font_text = pygame.font.SysFont('arial', int(WIDTH / 36), 0)
    arial_font_type = pygame.font.SysFont('arial', int(WIDTH / 50), 0)
    arial_font_label = pygame.font.SysFont('arial', int(WIDTH / 60), 0)

    # Creates GUI elements
    projectile_motion_button = button(5*WIDTH/32, 2*HEIGHT/9, HEIGHT/3, HEIGHT/3, colour_scheme[0], colour_scheme[2], 'Projectile Motion', None, None)
    circular_motion_button = button(21*WIDTH/32, 2*HEIGHT/9, HEIGHT/3, HEIGHT/3, colour_scheme[0], colour_scheme[2], 'Circular Motion', None, None)
    banked_tracks_button = button(5*WIDTH/32, 3*HEIGHT/5, HEIGHT/3, HEIGHT/3, colour_scheme[0], colour_scheme[2], 'Banked Tracks', None, None)
    gravity_in_space_button = button(21*WIDTH/32, 3*HEIGHT/5, HEIGHT/3, HEIGHT/3, colour_scheme[0], colour_scheme[2], 'Gravity in Space', None, None)
    back_arrow.image = image_colour_changer(back_arrow.image, colour_scheme[2], back_arrow.colour)
    back_button = button(153 * WIDTH / 160, 37 * HEIGHT / 40, WIDTH / 30, WIDTH / 30, colour_scheme[0], colour_scheme[2], None, back_arrow.image, None)
    projectile_motion_icon.x_position, projectile_motion_icon.y_position, projectile_motion_icon.image = 5*WIDTH/32, 2*HEIGHT/8, pygame.transform.scale(projectile_motion_icon.picture, (HEIGHT/3, HEIGHT/3))
    circular_motion_icon.x_position, circular_motion_icon.y_position, circular_motion_icon.image = 171*WIDTH/256, 23*HEIGHT/84, pygame.transform.scale(circular_motion_icon.picture, (8*HEIGHT/27, 8*HEIGHT/27))
    banked_tracks_icon.x_position, banked_tracks_icon.y_position, banked_tracks_icon.image = 5*WIDTH/32, 7*HEIGHT/11, pygame.transform.scale(banked_tracks_icon.picture, (HEIGHT/3, HEIGHT/3))
    gravity_in_space_icon.x_position, gravity_in_space_icon.y_position, gravity_in_space_icon.image = 87*WIDTH/128, 53*HEIGHT/80, pygame.transform.scale(gravity_in_space_icon.picture, (HEIGHT/4, HEIGHT/4))

    running = True
    while running:
        # Resets left click
        left_click = False

        # Resets Screen
        screen.fill((255, 255, 255))

        # Gets mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Processes events
        left_click, running, mouse_move, mouse_release, key_down = Events.events(left_click, running)

        # Updates projectile motion button
        projectile_motion_button.button_click(mouse_x, mouse_y, left_click)
        if projectile_motion_button.active:
            projectile_motion(FPS, WIDTH, HEIGHT, colour_scheme)
            projectile_motion_button.active = False

        # Updates circular motion button
        circular_motion_button.button_click(mouse_x, mouse_y, left_click)
        if circular_motion_button.active:
            circular_motion(FPS, WIDTH, HEIGHT, colour_scheme)
            circular_motion_button.active = False

        # Updates banked tracks button
        banked_tracks_button.button_click(mouse_x, mouse_y, left_click)
        if banked_tracks_button.active:
            banked_tracks_side_view(FPS, WIDTH, HEIGHT, colour_scheme)
            banked_tracks_button.active = False

        # Updates gravity in space button
        gravity_in_space_button.button_click(mouse_x, mouse_y, left_click)
        if gravity_in_space_button.active:
            gravity_in_space(FPS, WIDTH, HEIGHT, colour_scheme)
            gravity_in_space_button.active = False

        # Updates back button
        back_button.button_click(mouse_x, mouse_y, left_click)
        if back_button.active:
            running = False
            back_button.active = False

        # Draws screen
        # Draws line
        pygame.draw.line(screen, colour_scheme[1], (0, 1), (WIDTH, 1), line_thickness)
        pygame.draw.line(screen, colour_scheme[1], (0, HEIGHT/6), (WIDTH, HEIGHT/6), line_thickness)

        # Draws icons
        screen.blit(back_button.image, (back_arrow.x_position, back_arrow.y_position))
        screen.blit(projectile_motion_icon.image, (projectile_motion_icon.x_position, projectile_motion_icon.y_position))
        screen.blit(circular_motion_icon.image, (circular_motion_icon.x_position, circular_motion_icon.y_position))
        screen.blit(banked_tracks_icon.image, (banked_tracks_icon.x_position, banked_tracks_icon.y_position))
        screen.blit(gravity_in_space_icon.image, (gravity_in_space_icon.x_position, gravity_in_space_icon.y_position))

        # Draws buttons
        pygame.draw.rect(screen, projectile_motion_button.colour, projectile_motion_button.button, corner_roundness, line_thickness)
        pygame.draw.rect(screen, circular_motion_button.colour, circular_motion_button.button, corner_roundness, line_thickness)
        pygame.draw.rect(screen, banked_tracks_button.colour, banked_tracks_button.button, corner_roundness, line_thickness)
        pygame.draw.rect(screen, gravity_in_space_button.colour, gravity_in_space_button.button, corner_roundness, line_thickness)
        pygame.draw.rect(screen, back_button.colour, back_button.button, 2, 3)

        # Draws text
        draw_text_centre('Advanced Mechanics', arial_font_title, colour_scheme[0], screen, WIDTH / 2, HEIGHT/12)
        draw_text_centre(projectile_motion_button.text, arial_font_text, projectile_motion_button.colour, screen, WIDTH/4, 7*HEIGHT/27)
        draw_text_centre(circular_motion_button.text, arial_font_text, circular_motion_button.colour, screen, 3*WIDTH/4, 7*HEIGHT/27)
        draw_text_centre(banked_tracks_button.text, arial_font_text, banked_tracks_button.colour, screen, WIDTH/4, 23*HEIGHT/36)
        draw_text_centre(gravity_in_space_button.text, arial_font_text, gravity_in_space_button.colour, screen, 3*WIDTH/4, 23*HEIGHT/36)

        pygame.display.update()
        clock.tick(FPS)
