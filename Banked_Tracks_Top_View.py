from Presets import *
from Banked_Tracks_Menu import banked_tracks_menu
from Banked_Tracks_Stats_Calculator import banked_tracks_stats_calculator
from Classes import *


def banked_tracks_top_view(start_icon, temp_radius, FPS, WIDTH, HEIGHT, colour_scheme, track_object, track_ball, lower_limit, upper_limit, speed_min, speed_max, mass_min, mass_max, gravity_min, gravity_max, angle, program_time, pause_time, show_forces_button, back_button, start_button, menu_button, speed_slider_button_min, speed_slider_button, speed_slider_button_max, mass_slider_button_min, mass_slider_button, mass_slider_button_max, gravity_slider_button_min, gravity_slider_button, gravity_slider_button_max, track_angle_button, friction_slider_button, friction_button, track, menu_open, radius, period, angular_speed, speed, mass, gravity, track_angle, friction, start_time, running):
    # Adjusts font sizes
    side_view_button = button(14*WIDTH/64, HEIGHT/20, WIDTH/8, HEIGHT/15, colour_scheme[0], colour_scheme[2], 'Side View', None, None)  # Creates side view button
    arial_font_title = pygame.font.SysFont('arial', int(WIDTH / 20), 1)
    arial_font_header = pygame.font.SysFont('arial', int(WIDTH / 30), 1)
    arial_font_small_title = pygame.font.SysFont('arial', int(WIDTH / 38), 1)
    arial_font_text = pygame.font.SysFont('arial', int(WIDTH / 36), 0)
    arial_font_type = pygame.font.SysFont('arial', int(WIDTH / 50), 0)
    arial_font_label = pygame.font.SysFont('arial', int(WIDTH / 60), 0)
    while running:
        # Resets left click
        left_click = False

        # Resets screen
        screen.fill((255, 255, 255))

        # Gets mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Processes events
        left_click, running, mouse_move, mouse_release, key_down = Events.events(left_click, running)

        back_button.button_click(mouse_x, mouse_y, left_click)
        if back_button.active:
            running = False
            back_button.active = False

        # Updates side_view button
        side_view_button.button_click(mouse_x, mouse_y, left_click)
        if side_view_button.active:
            side_view_button.active = False
            return start_icon, temp_radius, track_object, track_ball, lower_limit, upper_limit, speed_min, speed_max, mass_min, mass_max, gravity_min, gravity_max, angle, program_time, pause_time, show_forces_button, back_button, start_button, menu_button, speed_slider_button_min, speed_slider_button, speed_slider_button_max, mass_slider_button_min, mass_slider_button, mass_slider_button_max, gravity_slider_button_min, gravity_slider_button, gravity_slider_button_max, track_angle_button, friction_slider_button, friction_button, track, menu_open, radius, period, angular_speed, speed, mass, gravity, track_angle, friction, start_time, running

        # Calculates values
        if radius:
            temp_radius = radius
            if radius < WIDTH/32:
                track_ball.radius = radius
            else:
                track_ball.radius = WIDTH/32
        gravity_force, normal_force, net_force, radius, period, angular_speed, min_speed, max_speed = banked_tracks_stats_calculator(speed, mass, gravity, track_angle, friction)

        # Updates start button
        start_button.toggle_button_click(mouse_x, mouse_y, left_click)
        if start_button.active and period:
            program_time = time.time() - start_time - pause_time
            angle = 2 * math.pi * (program_time % period) / period
            track_ball.x_acceleration = math.cos(angle) * net_force
            track_ball.y_acceleration = math.sin(angle) * net_force
            track_ball.x_velocity = math.cos(angle)
            track_ball.y_velocity = math.sin(angle)
            track_ball.x_position = WIDTH/2 - math.cos(angle) * radius
            track_ball.y_position = HEIGHT/2 - math.sin(angle) * radius
        elif period:
            pause_time = time.time() - start_time - program_time
            angle = 2 * math.pi * (program_time % period) / period
            track_ball.x_position = WIDTH/2 - math.cos(angle) * radius
            track_ball.y_position = HEIGHT/2 - math.sin(angle) * radius
        else:
            pause_time = time.time() - start_time - program_time

        # Draws banked tracks simulation
        if radius:
            pygame.draw.circle(screen, track.colour, (WIDTH/2, HEIGHT/2), radius + 80)
        else:
            pygame.draw.circle(screen, track.colour, (WIDTH/2, HEIGHT/2), temp_radius + 80)
        pygame.draw.circle(screen, colour_scheme[0], (WIDTH/2, HEIGHT/2), 2)
        pygame.draw.circle(screen, (0, 0, 0), (track_ball.x_position, track_ball.y_position), track_ball.radius)
        # Draws banked tracks simulation

        # Updates show forces button
        show_forces_button.toggle_button_click(mouse_x, mouse_y, left_click)
        if show_forces_button.active:
            pygame.draw.line(screen, (0, 0, 255), (track_ball.x_position, track_ball.y_position), (track_ball.x_position + int(math.cos(angle) * net_force), track_ball.y_position + int(math.sin(angle) * net_force)), line_thickness)

        # Draws Overlay
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 0, WIDTH, HEIGHT/6))
        # Draws text
        draw_text_midleft('Banked Tracks', arial_font_small_title, colour_scheme[0], screen, WIDTH/26, HEIGHT/12)
        draw_text_centre(side_view_button.text, arial_font_small_title, side_view_button.colour, screen, 10*WIDTH/36, HEIGHT/12)
        draw_text_centre(show_forces_button.text, arial_font_small_title, show_forces_button.colour, screen, 79*WIDTH/180, HEIGHT/12)
        draw_text_midleft('- gravitational force ', arial_font_type, colour_scheme[0], screen, 39*WIDTH/64, 3*HEIGHT/87)
        draw_text_midleft('- net force ', arial_font_type, colour_scheme[0], screen, 39*WIDTH/64, 7*HEIGHT/87)
        draw_text_midleft('- normal force ', arial_font_type, colour_scheme[0], screen, 39*WIDTH/64, 11*HEIGHT/87)

        # Draws Labels
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(35*WIDTH/64, HEIGHT/35, WIDTH/20, HEIGHT/35))
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(35*WIDTH/64, 5*HEIGHT/70, WIDTH/20, HEIGHT/35))
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(35*WIDTH/64, 8*HEIGHT/70, WIDTH/20, HEIGHT/35))

        # Draws buttons
        pygame.draw.rect(screen, show_forces_button.colour, show_forces_button.button, 2, 3)
        pygame.draw.rect(screen, start_button.colour, start_button.button, 2, 3)
        pygame.draw.rect(screen, side_view_button.colour, side_view_button.button, 2, 3)

        # Draws icons
        screen.blit(back_arrow.image, (back_arrow.x_position, back_arrow.y_position))
        screen.blit(start_icon.image, (start_icon.x_position, start_icon.y_position))

        # Draws lines
        pygame.draw.line(screen, colour_scheme[1], (0, HEIGHT / 6), (WIDTH, HEIGHT / 6), line_thickness)
        pygame.draw.line(screen, colour_scheme[1], (0, 1), (WIDTH, 1), line_thickness)
        # Draws Overlay

        # Processes menu
        lower_limit, upper_limit, speed_min, speed_max, mass_min, mass_max, gravity_min, gravity_max, radius, period, angular_speed, speed, mass, gravity, track_angle, track_angle, friction, left_click, menu_button, menu_open, start_button = banked_tracks_menu(min_speed, max_speed, colour_scheme, lower_limit, upper_limit, speed_min, speed_max, mass_min, mass_max, gravity_min, gravity_max, mouse_move, mouse_release, menu_button, menu_open, start_button, friction_button, speed_slider_button_min, speed_slider_button, speed_slider_button_max, mass_slider_button_min, mass_slider_button, mass_slider_button_max, gravity_slider_button_min, gravity_slider_button, gravity_slider_button_max, track_angle_button, friction_slider_button, WIDTH, HEIGHT, left_click, key_down, mouse_x, mouse_y, radius, period, angular_speed, speed, mass, gravity, track_angle, friction)

        # Draws back button
        pygame.draw.rect(screen, back_button.colour, back_button.button, 2, 3)
        screen.blit(back_arrow.image, (back_arrow.x_position, back_arrow.y_position))

        pygame.display.update()
        clock.tick(FPS)
    return start_icon, temp_radius, track_object, track_ball, lower_limit, upper_limit, speed_min, speed_max, mass_min, mass_max, gravity_min, gravity_max, angle, program_time, pause_time, show_forces_button, back_button, start_button, menu_button, speed_slider_button_min, speed_slider_button, speed_slider_button_max, mass_slider_button_min, mass_slider_button, mass_slider_button_max, gravity_slider_button_min, gravity_slider_button, gravity_slider_button_max, track_angle_button, friction_slider_button, friction_button, track, menu_open, radius, period, angular_speed, speed, mass, gravity, track_angle, friction, start_time, running
