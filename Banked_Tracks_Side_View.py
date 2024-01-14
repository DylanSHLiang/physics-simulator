from Presets import *
from Banked_Tracks_Menu import banked_tracks_menu
from Banked_Tracks_Top_View import banked_tracks_top_view
from Banked_Tracks_Stats_Calculator import banked_tracks_stats_calculator
from Classes import *


def banked_tracks_side_view(FPS, WIDTH, HEIGHT, colour_scheme):
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
    show_forces_button = button(11*WIDTH/30, HEIGHT/20, WIDTH/7, HEIGHT/15, colour_scheme[0], colour_scheme[2], 'Show Forces', None, None)
    top_view_button = button(14*WIDTH/64, HEIGHT/20, WIDTH/8, HEIGHT/15, colour_scheme[0], colour_scheme[2], 'Top View', None, None)
    menu_button = button(WIDTH/2, HEIGHT, WIDTH/22, HEIGHT/30, colour_scheme[0], colour_scheme[2], None, None, None)
    menu_button.button.midbottom = menu_button.x_position, menu_button.y_position

    # Creates menu buttons
    friction_button = button(42*WIDTH/80, 96*HEIGHT/100, HEIGHT/20, HEIGHT/20, colour_scheme[0], colour_scheme[2], None, None, None)
    speed_slider_button_min = button(WIDTH/6, 72*HEIGHT/100, WIDTH/17, WIDTH/34, colour_scheme[0], colour_scheme[2], '0', None, None)
    speed_slider_button = button(12*WIDTH/25, 72*HEIGHT/100, WIDTH/80, WIDTH/40, colour_scheme[0], colour_scheme[2], None, None, None)
    speed_slider_button_max = button(WIDTH/2, 72*HEIGHT/100, WIDTH/17, WIDTH/34, colour_scheme[0], colour_scheme[2], '0', None, None)
    mass_slider_button_min = button(WIDTH/6, 78*HEIGHT/100, WIDTH/17, WIDTH/34, colour_scheme[0], colour_scheme[2], '0', None, None)
    mass_slider_button = button(12*WIDTH/25, 78*HEIGHT/100, WIDTH/80, WIDTH/40, colour_scheme[0], colour_scheme[2], None, None, None)
    mass_slider_button_max = button(WIDTH/2, 78*HEIGHT/100, WIDTH/17, WIDTH/34, colour_scheme[0], colour_scheme[2], '0', None, None)
    gravity_slider_button_min = button(WIDTH/6, 84*HEIGHT/100, WIDTH/17, WIDTH/34, colour_scheme[0], colour_scheme[2], '0', None, None)
    gravity_slider_button = button(12*WIDTH/25, 84*HEIGHT/100, WIDTH/80, WIDTH/40, colour_scheme[0], colour_scheme[2], None, None, None)
    gravity_slider_button_max = button(WIDTH/2, 84*HEIGHT/100, WIDTH/17, WIDTH/34, colour_scheme[0], colour_scheme[2], '0', None, None)
    track_angle_button = button(8*WIDTH/25, 90*HEIGHT/100, WIDTH/80, WIDTH/40, colour_scheme[0], colour_scheme[2], None, None, None)
    friction_slider_button = button(WIDTH/4, 96*HEIGHT/100, WIDTH/80, WIDTH/40, colour_scheme[0], colour_scheme[2], None, None, None)
    friction_button.button.centery = friction_button.y_position
    speed_slider_button_min.button.centery = speed_slider_button_min.y_position
    speed_slider_button.button.centery = speed_slider_button.y_position
    speed_slider_button_max.button.centery = speed_slider_button_max.y_position
    mass_slider_button_min.button.centery = mass_slider_button_min.y_position
    mass_slider_button.button.centery = mass_slider_button.y_position
    mass_slider_button_max.button.centery = mass_slider_button_max.y_position
    gravity_slider_button_min.button.centery = gravity_slider_button_min.y_position
    gravity_slider_button.button.centery = gravity_slider_button.y_position
    gravity_slider_button_max.button.centery = gravity_slider_button_max.y_position
    track_angle_button.button.centery = track_angle_button.y_position
    friction_slider_button.button.centery = friction_slider_button.y_position

    # Creates banked tracks objects
    track = triangle((2*WIDTH/3, 5*HEIGHT/8), (WIDTH/3, 5*HEIGHT/8), (WIDTH/3, 5*HEIGHT/8), colour_scheme[2])
    track_object = moving_block(colour_scheme[0], 392, 258, WIDTH/16, WIDTH/16)
    track_object.side_image.set_colorkey(colour_scheme[0])
    track_object.side_image = pygame.transform.rotate(track_object.side_image, 60)
    track_ball = ball((0, 0, 0), 0, 0, 0, 0, 0, 0, 0, 0, 50)

    # Sets variables
    speed_min = 0
    speed_max = 0
    mass_min = 0
    mass_max = 0
    gravity_min = 0
    gravity_max = 0
    menu_open = True
    radius = 0
    period = 0
    angular_speed = 0
    speed = 0
    mass = 0
    gravity = 0
    track_angle = 0
    friction = 0
    start_time = time.time()
    pause_time = 0
    program_time = 0
    angle = 0
    lower_limit = 0
    upper_limit = 0
    temp_radius = 0

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

        # Updates back button
        back_button.button_click(mouse_x, mouse_y, left_click)
        # Back button function
        if back_button.active:
            running = False
            back_button.active = False

        # Updates start button
        start_button.toggle_button_click(mouse_x, mouse_y, left_click)

        # Updates top_view button
        top_view_button.button_click(mouse_x, mouse_y, left_click)
        if top_view_button.active:
            start_icon, temp_radius, track_object, track_ball, lower_limit, upper_limit, speed_min, speed_max, mass_min, mass_max, gravity_min, gravity_max, angle, program_time, pause_time, show_forces_button, back_button, start_button, menu_button, speed_slider_button_min, speed_slider_button, speed_slider_button_max, mass_slider_button_min, mass_slider_button, mass_slider_button_max, gravity_slider_button_min, gravity_slider_button, gravity_slider_button_max, track_angle_button, friction_slider_button, friction_button, track, menu_open, radius, period, angular_speed, speed, mass, gravity, track_angle, friction, start_time, running = banked_tracks_top_view(start_icon, temp_radius, FPS, WIDTH, HEIGHT, colour_scheme, track_object, track_ball, lower_limit, upper_limit, speed_min, speed_max, mass_min, mass_max, gravity_min, gravity_max, angle, program_time, pause_time, show_forces_button, back_button, start_button, menu_button, speed_slider_button_min, speed_slider_button, speed_slider_button_max, mass_slider_button_min, mass_slider_button, mass_slider_button_max, gravity_slider_button_min, gravity_slider_button, gravity_slider_button_max, track_angle_button, friction_slider_button, friction_button, track, menu_open, radius, period, angular_speed, speed, mass, gravity, track_angle, friction, start_time, running)
            top_view_button.active = False

        # Calculates values
        if radius:
            temp_radius = radius
            if radius < WIDTH/16:
                track_object.width = radius
                track_object.height = radius
            else:
                track_object.width = WIDTH/16
                track_object.height = WIDTH/16
        gravity_force, normal_force, net_force, radius, period, angular_speed, min_speed, max_speed = banked_tracks_stats_calculator(speed, mass, gravity, track_angle, friction)

        # Updates Track
        if radius:
            track.update_triangle(track_angle, radius, 2*WIDTH/3, 5*HEIGHT/8)
            track_object.update_moving_block(track_angle, radius, 2*WIDTH/3, 5*HEIGHT/8)
        elif not track_angle and not friction:
            track.update_triangle(track_angle, temp_radius, 2*WIDTH/3, 5*HEIGHT/8)
            track_object.update_moving_block(track_angle, temp_radius, 2*WIDTH/3, 5*HEIGHT/8)
        # Draws banked tracks simulation
        pygame.draw.polygon(screen, track.colour, (track.point_1, track.point_2, track.point_3))
        screen.blit(track_object.side_image, (track_object.x_position - int(track_object.side_image.get_width() / 2), track_object.y_position - int(track_object.side_image.get_height() / 2)))

        # Updates show forces button
        show_forces_button.toggle_button_click(mouse_x, mouse_y, left_click)
        if show_forces_button.active:
            if net_force > 1000:
                pygame.draw.line(screen, (0, 255, 0), (track_object.x_position, track_object.y_position), (track_object.x_position, track_object.y_position + int(1000)), line_thickness)
                pygame.draw.line(screen, (0, 0, 255), (track_object.x_position, track_object.y_position), (track_object.x_position + int(1000), track_object.y_position), line_thickness)
                pygame.draw.line(screen, (255, 0, 0), (track_object.x_position, track_object.y_position), (track_object.x_position + int(1000 * math.cos((math.pi / 180 * track_angle) - math.pi / 2)), track_object.y_position - int(1000 * math.sin((math.pi / 180 * track_angle) + math.pi / 2))), line_thickness)
            else:
                pygame.draw.line(screen, (0, 255, 0), (track_object.x_position, track_object.y_position), (track_object.x_position, track_object.y_position + int(gravity_force)), line_thickness)
                pygame.draw.line(screen, (0, 0, 255), (track_object.x_position, track_object.y_position), (track_object.x_position + int(net_force), track_object.y_position), line_thickness)
                pygame.draw.line(screen, (255, 0, 0), (track_object.x_position, track_object.y_position), (track_object.x_position + int(normal_force * math.cos((math.pi / 180 * track_angle) - math.pi / 2)), track_object.y_position - int(normal_force * math.sin((math.pi / 180 * track_angle) + math.pi / 2))), line_thickness)

        # Draws Overlay
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 0, WIDTH, HEIGHT/6))
        # Draws text
        draw_text_midleft('Banked Tracks', arial_font_small_title, colour_scheme[0], screen, WIDTH/26, HEIGHT/12)
        draw_text_centre(top_view_button.text, arial_font_small_title, top_view_button.colour, screen, 10*WIDTH/36, HEIGHT/12)
        draw_text_centre(show_forces_button.text, arial_font_small_title, show_forces_button.colour, screen, 79*WIDTH/180, HEIGHT/12)
        draw_text_midleft('- gravitational force ', arial_font_type, colour_scheme[0], screen, 39*WIDTH/64, 3*HEIGHT/87)
        draw_text_midleft('- net force ', arial_font_type, colour_scheme[0], screen, 39*WIDTH/64, 7*HEIGHT/87)
        draw_text_midleft('- normal force ', arial_font_type, colour_scheme[0], screen, 39*WIDTH/64, 11*HEIGHT/87)

        # Draws Labels
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(35*WIDTH/64, HEIGHT/35, WIDTH/20, HEIGHT/35))
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(35*WIDTH/64, 5*HEIGHT/70, WIDTH/20, HEIGHT/35))
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(35*WIDTH/64, 8*HEIGHT/70, WIDTH/20, HEIGHT/35))

        # Draws buttons
        pygame.draw.rect(screen, start_button.colour, start_button.button, 2, 3)
        pygame.draw.rect(screen, top_view_button.colour, top_view_button.button, 2, 3)
        pygame.draw.rect(screen, show_forces_button.colour, show_forces_button.button, 2, 3)

        # Draws icons
        screen.blit(start_icon.image, (start_icon.x_position, start_icon.y_position))

        # Draws lines
        pygame.draw.line(screen, colour_scheme[1], (0, HEIGHT / 6), (WIDTH, HEIGHT / 6), line_thickness)
        pygame.draw.line(screen, colour_scheme[1], (0, 1), (WIDTH, 1), line_thickness)

        # Processes menu
        lower_limit, upper_limit, speed_min, speed_max, mass_min, mass_max, gravity_min, gravity_max, radius, period, angular_speed, speed, mass, gravity, track_angle, track_angle, friction, left_click, menu_button, menu_open, start_button = banked_tracks_menu(min_speed, max_speed, colour_scheme, lower_limit, upper_limit, speed_min, speed_max, mass_min, mass_max, gravity_min, gravity_max, mouse_move, mouse_release, menu_button, menu_open, start_button, friction_button, speed_slider_button_min, speed_slider_button, speed_slider_button_max, mass_slider_button_min, mass_slider_button, mass_slider_button_max, gravity_slider_button_min, gravity_slider_button, gravity_slider_button_max, track_angle_button, friction_slider_button, WIDTH, HEIGHT, left_click, key_down, mouse_x, mouse_y, radius, period, angular_speed, speed, mass, gravity, track_angle, friction)

        # Draws back button
        pygame.draw.rect(screen, back_button.colour, back_button.button, 2, 3)
        screen.blit(back_arrow.image, (back_arrow.x_position, back_arrow.y_position))

        pygame.display.update()
        clock.tick(FPS)
