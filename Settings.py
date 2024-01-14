from Presets import *
from Draw_Text import draw_text_centre


def settings(FPS, WIDTH, HEIGHT, colour_scheme):
    running = True
    while running:
        arial_font_title = pygame.font.SysFont('arial', int(WIDTH / 20), 1)
        arial_font_header = pygame.font.SysFont('arial', int(WIDTH / 30), 1)
        arial_font_small_title = pygame.font.SysFont('arial', int(WIDTH / 38), 1)
        arial_font_text = pygame.font.SysFont('arial', int(WIDTH / 36), 0)
        arial_font_type = pygame.font.SysFont('arial', int(WIDTH / 50), 0)
        arial_font_label = pygame.font.SysFont('arial', int(WIDTH / 60), 0)
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # Creates GUI elements
        back_arrow.x_position, back_arrow.y_position, back_arrow.image = 307 * WIDTH / 320, 149 * HEIGHT / 160, pygame.transform.scale(back_arrow.picture, (WIDTH / 40, WIDTH / 40))
        back_arrow.image = image_colour_changer(back_arrow.image, back_arrow.colour, colour_scheme[0])
        back_button = button(153*WIDTH/160, 37*HEIGHT/40, WIDTH/30, WIDTH/30, colour_scheme[0], colour_scheme[2], None, back_arrow.image, None)
        screen_size_1920_1080 = button(3*WIDTH/20, 13*HEIGHT/40, WIDTH/5, HEIGHT/15, colour_scheme[0], colour_scheme[2], "1920 x 1080", None, None)
        screen_size_1600_900 = button(3*WIDTH/20, 11*HEIGHT/25, WIDTH/5, HEIGHT/15, colour_scheme[0], colour_scheme[2], "1600 x 900", None, None)
        screen_size_1366_768 = button(3*WIDTH/20, 111*HEIGHT/200, WIDTH/5, HEIGHT/15, colour_scheme[0], colour_scheme[2], "1366 x 768", None, None)
        screen_size_1280_720 = button(3*WIDTH/20, 67*HEIGHT/100, WIDTH/5, HEIGHT/15, colour_scheme[0], colour_scheme[2], "1280 x 720", None, None)
        screen_size_1024_576 = button(3*WIDTH/20, 157*HEIGHT/200, WIDTH/5, HEIGHT/15, colour_scheme[0], colour_scheme[2], "1024 x 576", None, None)
        screen_size_960_540 = button(3*WIDTH/20, 9*HEIGHT/10, WIDTH/5, HEIGHT/15, colour_scheme[0], colour_scheme[2], "960 x 540", None, None)
        fps_15_button = button(9*WIDTH/16, 13*HEIGHT/40, WIDTH/8, HEIGHT/15, colour_scheme[0], colour_scheme[2], "15 FPS", None, None)
        fps_24_button = button(13*WIDTH/16, 13*HEIGHT/40, WIDTH/8, HEIGHT/15, colour_scheme[0], colour_scheme[2], "24 FPS", None, None)
        fps_30_button = button(9*WIDTH/16, 33*HEIGHT/80, WIDTH/8, HEIGHT/15, colour_scheme[0], colour_scheme[2], "30 FPS", None, None)
        fps_60_button = button(13*WIDTH/16, 33*HEIGHT/80, WIDTH/8, HEIGHT/15, colour_scheme[0], colour_scheme[2], "60 FPS", None, None)
        fps_120_button = button(9*WIDTH/16, HEIGHT/2, WIDTH/8, HEIGHT/15, colour_scheme[0], colour_scheme[2], "120 FPS", None, None)
        fps_144_button = button(13*WIDTH/16, HEIGHT/2, WIDTH/8, HEIGHT/15, colour_scheme[0], colour_scheme[2], "144 FPS", None, None)
        colour_scheme_1 = button(2*WIDTH/3, 43*HEIGHT/60, WIDTH/6, HEIGHT/15, (0, 0, 0), (155, 155, 155), "Black & White", None, None)
        colour_scheme_2 = button(2 * WIDTH / 3, 97 * HEIGHT / 120, WIDTH / 6, HEIGHT / 15, (107, 73, 132), (198, 164, 223), "Deep Space", None, None)
        colour_scheme_3 = button(2 * WIDTH / 3, 27 * HEIGHT / 30, WIDTH / 6, HEIGHT / 15, (255, 0, 129), (255, 119, 188), "Bubblegum", None, None)

        # Resets left click
        left_click = False

        # Resets Screen
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

        # Updates screen size buttons
        screen_size_1920_1080.button_click(mouse_x, mouse_y, left_click)
        if screen_size_1920_1080.active:
            WIDTH, HEIGHT = 1920, 1080
            screen_size_1920_1080.active = False

        screen_size_1600_900.button_click(mouse_x, mouse_y, left_click)
        if screen_size_1600_900.active:
            WIDTH, HEIGHT = 1600, 900
            screen_size_1600_900.active = False

        screen_size_1366_768.button_click(mouse_x, mouse_y, left_click)
        if screen_size_1366_768.active:
            WIDTH, HEIGHT = 1366, 768
            screen_size_1366_768.active = False

        screen_size_1280_720.button_click(mouse_x, mouse_y, left_click)
        if screen_size_1280_720.active:
            WIDTH, HEIGHT = 1280, 720
            screen_size_1280_720.active = False

        screen_size_1024_576.button_click(mouse_x, mouse_y, left_click)
        if screen_size_1024_576.active:
            WIDTH, HEIGHT = 1024, 576
            screen_size_1024_576.active = False

        screen_size_960_540.button_click(mouse_x, mouse_y, left_click)
        if screen_size_960_540.active:
            WIDTH, HEIGHT = 960, 540
            screen_size_960_540.active = False

        # Updates FPS buttons
        fps_15_button.button_click(mouse_x, mouse_y, left_click)
        if fps_15_button.active:
            FPS = 15
            fps_15_button.active = False

        fps_24_button.button_click(mouse_x, mouse_y, left_click)
        if fps_24_button.active:
            FPS = 24
            fps_24_button.active = False

        fps_30_button.button_click(mouse_x, mouse_y, left_click)
        if fps_30_button.active:
            FPS = 30
            fps_30_button.active = False

        fps_60_button.button_click(mouse_x, mouse_y, left_click)
        if fps_60_button.active:
            FPS = 60
            fps_60_button.active = False

        fps_120_button.button_click(mouse_x, mouse_y, left_click)
        if fps_120_button.active:
            FPS = 120
            fps_120_button.active = False

        fps_144_button.button_click(mouse_x, mouse_y, left_click)
        if fps_144_button.active:
            FPS = 144
            fps_144_button.active = False

        # Updates colour scheme buttons
        colour_scheme_1.button_click(mouse_x, mouse_y, left_click)
        if colour_scheme_1.active:
            colour_scheme = [(0, 0, 0), (0, 0, 0), (155, 155, 155)]
            colour_scheme_1.active = False

        colour_scheme_2.button_click(mouse_x, mouse_y, left_click)
        if colour_scheme_2.active:
            colour_scheme = [(107, 73, 132), (3, 33, 74), (208, 174, 233)]
            colour_scheme_2.active = False

        colour_scheme_3.button_click(mouse_x, mouse_y, left_click)
        if colour_scheme_3.active:
            colour_scheme = [(255, 0, 129), (145, 209, 234), (255, 119, 188)]
            colour_scheme_3.active = False

        # Updates fonts

        # Draws screen
        # Draws lines
        pygame.draw.line(screen, colour_scheme[1], (0, 1), (WIDTH, 1), line_thickness)
        pygame.draw.line(screen, colour_scheme[1], (0, HEIGHT/6), (WIDTH, HEIGHT/6), line_thickness)
        pygame.draw.line(screen, colour_scheme[1], (WIDTH/2, HEIGHT/6), (WIDTH/2, HEIGHT), line_thickness)

        # Draws buttons
        pygame.draw.rect(screen, screen_size_1920_1080.colour, screen_size_1920_1080.button, 2, 3)
        pygame.draw.rect(screen, screen_size_1600_900.colour, screen_size_1600_900.button, 2, 3)
        pygame.draw.rect(screen, screen_size_1366_768.colour, screen_size_1366_768.button, 2, 3)
        pygame.draw.rect(screen, screen_size_1280_720.colour, screen_size_1280_720.button, 2, 3)
        pygame.draw.rect(screen, screen_size_1024_576.colour, screen_size_1024_576.button, 2, 3)
        pygame.draw.rect(screen, screen_size_960_540.colour, screen_size_960_540.button, 2, 3)
        pygame.draw.rect(screen, fps_15_button.colour, fps_15_button.button, 2, 3)
        pygame.draw.rect(screen, fps_24_button.colour, fps_24_button.button, 2, 3)
        pygame.draw.rect(screen, fps_30_button.colour, fps_30_button.button, 2, 3)
        pygame.draw.rect(screen, fps_60_button.colour, fps_60_button.button, 2, 3)
        pygame.draw.rect(screen, fps_120_button.colour, fps_120_button.button, 2, 3)
        pygame.draw.rect(screen, fps_144_button.colour, fps_144_button.button, 2, 3)
        pygame.draw.rect(screen, colour_scheme_1.colour, colour_scheme_1.button, 2, 3)
        pygame.draw.rect(screen, (3, 33, 74), colour_scheme_2.button, 0, 3)
        pygame.draw.rect(screen, colour_scheme_2.colour, colour_scheme_2.button, 2, 3)
        pygame.draw.rect(screen, (145, 209, 234), colour_scheme_3.button, 0, 3)
        pygame.draw.rect(screen, colour_scheme_3.colour, colour_scheme_3.button, 2, 3)

        # Draws text
        draw_text_centre('Settings', arial_font_title, colour_scheme[0], screen, WIDTH / 2, HEIGHT/12)
        draw_text_centre('Screen Size', arial_font_header, colour_scheme[0], screen, WIDTH/4, HEIGHT/4)
        draw_text_centre('FPS', arial_font_header, colour_scheme[0], screen, 3*WIDTH/4, HEIGHT/4)
        draw_text_centre('Colour Scheme', arial_font_header, colour_scheme[0], screen, 3*WIDTH/4, 39*HEIGHT/60)
        draw_text_centre(screen_size_1920_1080.text, arial_font_small_title, screen_size_1920_1080.colour, screen, WIDTH/4, 43*HEIGHT/120)  # Draws launch button label
        draw_text_centre(screen_size_1600_900.text, arial_font_small_title, screen_size_1600_900.colour, screen, WIDTH/4, 71*HEIGHT/150)  # Draws launch button label
        draw_text_centre(screen_size_1366_768.text, arial_font_small_title, screen_size_1366_768.colour, screen, WIDTH/4, 353*HEIGHT/600)  # Draws launch button label
        draw_text_centre(screen_size_1280_720.text, arial_font_small_title, screen_size_1280_720.colour, screen, WIDTH/4, 211*HEIGHT/300)  # Draws launch button label
        draw_text_centre(screen_size_1024_576.text, arial_font_small_title, screen_size_1024_576.colour, screen, WIDTH/4, 491*HEIGHT/600)  # Draws launch button label
        draw_text_centre(screen_size_960_540.text, arial_font_small_title, screen_size_960_540.colour, screen, WIDTH/4, 14*HEIGHT/15)  # Draws launch button label
        draw_text_centre(fps_15_button.text, arial_font_small_title, fps_15_button.colour, screen, 5*WIDTH/8, 43*HEIGHT/120)  # Draws launch button label
        draw_text_centre(fps_24_button.text, arial_font_small_title, fps_24_button.colour, screen, 7*WIDTH/8, 43*HEIGHT/120)  # Draws launch button label
        draw_text_centre(fps_30_button.text, arial_font_small_title, fps_30_button.colour, screen, 5*WIDTH/8, 107*HEIGHT/240)  # Draws launch button label
        draw_text_centre(fps_60_button.text, arial_font_small_title, fps_60_button.colour, screen, 7*WIDTH/8, 107*HEIGHT/240)  # Draws launch button label
        draw_text_centre(fps_120_button.text, arial_font_small_title, fps_120_button.colour, screen, 5*WIDTH/8, 8*HEIGHT/15)  # Draws launch button label
        draw_text_centre(fps_144_button.text, arial_font_small_title, fps_144_button.colour, screen, 7*WIDTH/8, 8*HEIGHT/15)  # Draws launch button label
        draw_text_centre(colour_scheme_1.text, arial_font_small_title, colour_scheme_1.colour, screen, 3*WIDTH/4, 3*HEIGHT/4)  # Draws launch button label
        draw_text_centre(colour_scheme_2.text, arial_font_small_title, colour_scheme_2.colour, screen, 3*WIDTH/4, 201*HEIGHT/240)  # Draws launch button label
        draw_text_centre(colour_scheme_3.text, arial_font_small_title, colour_scheme_3.colour, screen, 3*WIDTH/4, 223*HEIGHT/240)  # Draws launch button label

        # Draws back button
        pygame.draw.rect(screen, back_button.colour, back_button.button, 2, 3)
        screen.blit(back_arrow.image, (back_arrow.x_position, back_arrow.y_position))

        pygame.display.update()
        clock.tick(FPS)
    return FPS, WIDTH, HEIGHT, colour_scheme