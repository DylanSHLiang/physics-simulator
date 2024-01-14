from Presets import *
import pygame
from Image_Colour_Change import image_colour_changer


class button:
    def __init__(self, x_position, y_position, width, height, colour, highlight_colour, text, image, active):
        self.x_position = x_position
        self.y_position = y_position
        self.width = width
        self.height = height
        self.colour = colour
        self.normal_colour = colour
        self.highlight_colour = highlight_colour
        self.text = text
        self.image = image
        self.active = active
        self.button = pygame.Rect(self.x_position, self.y_position, self.width, self.height)

    def button_click(self, mouse_x, mouse_y, left_click,):
        if self.button.collidepoint((mouse_x, mouse_y)):
            self.colour = self.highlight_colour
            if self.image:
                self.image = image_colour_changer(self.image, self.normal_colour, self.highlight_colour)
            if left_click:
                self.active = True
        else:
            self.colour = self.normal_colour
            if self.image:
                self.image = image_colour_changer(self.image, self.highlight_colour, self.normal_colour)
        if self.active:
            self.colour = self.highlight_colour
            if self.image:
                self.image = image_colour_changer(self.image, self.normal_colour, self.highlight_colour)

    def one_time_button_click(self, mouse_x, mouse_y, left_click,):
        if not self.active:
            if self.button.collidepoint((mouse_x, mouse_y)):
                self.colour = self.highlight_colour
                if self.image:
                    self.image = image_colour_changer(self.image, self.normal_colour, self.highlight_colour)
                if left_click:
                    self.active = True
            else:
                self.colour = self.normal_colour
                if self.image:
                    self.image = image_colour_changer(self.image, self.highlight_colour, self.normal_colour)
        else:
            self.colour = self.highlight_colour
            if self.image:
                self.image = image_colour_changer(self.image, self.normal_colour, self.highlight_colour)

    def toggle_button_click(self, mouse_x, mouse_y, left_click):
        if self.button.collidepoint((mouse_x, mouse_y)):
            self.colour = self.highlight_colour
            if self.image:
                self.image = image_colour_changer(self.image, self.normal_colour, self.highlight_colour)
            if left_click:
                if self.active:
                    self.active = False
                else:
                    self.active = True
        else:
            self.colour = self.normal_colour
            if self.image:
                self.image = image_colour_changer(self.image, self.highlight_colour, self.normal_colour)
        if self.active:
            self.colour = self.highlight_colour
            if self.image:
                self.image = image_colour_changer(self.image, self.normal_colour, self.highlight_colour)

    def slider_button_click(self, mouse_x, mouse_y, left_click, mouse_move, mouse_release, minimum, maximum,
                            restriction):
        if self.button.collidepoint((mouse_x, mouse_y)):
            self.colour = self.highlight_colour
            if self.image:
                self.image = image_colour_changer(self.image, self.normal_colour, self.highlight_colour)
            if left_click:
                self.active = True
        else:
            self.colour = self.normal_colour
            if self.image:
                self.image = image_colour_changer(self.image, self.highlight_colour, self.normal_colour)
        if self.active and restriction:
            if mouse_x < minimum:
                self.x_position = minimum
            elif mouse_x > maximum:
                self.x_position = maximum
            elif mouse_move:
                self.x_position = mouse_x
            self.colour = self.highlight_colour
            if self.image:
                self.image = image_colour_changer(self.image, self.normal_colour, self.highlight_colour)
        if mouse_release:
            self.active = False
        self.button.centerx = self.x_position

    def input_button_click(self, mouse_x, mouse_y, left_click, key_down, other_input_buttons, parameter, limit):
        if left_click:
            self.active = False
            if not self.button.collidepoint((mouse_x, mouse_y)):
                if not self.text:
                    self.text = '0'
                    parameter = 0
                else:
                    parameter = float(self.text)
                self.active = False
                return parameter
        if self.button.collidepoint((mouse_x, mouse_y)):
            self.colour = self.highlight_colour
            if self.image:
                self.image = image_colour_changer(self.image, self.normal_colour, self.highlight_colour)
            if left_click:
                self.active = True
                for buttons in other_input_buttons:
                    buttons.active = False
        else:
            self.colour = self.normal_colour
            if self.image:
                self.image = image_colour_changer(self.image, self.highlight_colour, self.normal_colour)
        if self.active:
            self.colour = self.highlight_colour
            if self.image:
                self.image = image_colour_changer(self.image, self.normal_colour, self.highlight_colour)
            if key_down:
                if key_down == 'BACKSPACE':
                    self.text = self.text[0:-1]
                elif key_down == '\r':
                    if not self.text:
                        self.text = '0'
                        parameter = 0
                    else:
                        parameter = float(self.text)
                    self.active = False
                    return parameter
                elif len(self.text) < limit and '.' in self.text:
                    if key_down == '0' or key_down == '1' or key_down == '2' or key_down == '3' or key_down == '4' or key_down == '5' or key_down == '6' or key_down == '7' or key_down == '8' or key_down == '9':
                        if self.text == '0':
                            self.text = str(key_down)
                        else:
                            self.text += str(key_down)
                elif len(self.text) < limit - 1:
                    if key_down == '0' or key_down == '1' or key_down == '2' or key_down == '3' or key_down == '4' or key_down == '5' or key_down == '6' or key_down == '7' or key_down == '8' or key_down == '9' or key_down == '.':
                        if self.text == '0':
                            self.text = str(key_down)
                        else:
                            self.text += str(key_down)
        return parameter


class block:
    def __init__(self, colour, x_position, y_position, width, height):
        self.colour = colour
        self.x_position = x_position
        self.y_position = y_position
        self.width = width
        self.height = height
        self.block = pygame.Rect(self.x_position, self.y_position, self.width, self.height)


class moving_block:
    def __init__(self, colour, x_position, y_position, width, height):
        self.colour = colour
        self.x_position = x_position
        self.y_position = y_position
        self.width = width
        self.height = height
        self.block = pygame.Rect(self.x_position, self.y_position, self.width, self.height)
        self.side_image = pygame.Surface((self.width, self.height))

    def update_moving_block(self, track_angle, radius, starting_x, starting_y):
        if radius > 2000:
            self.x_position = -100
            self.y_position = -100
        else:
            self.x_position = starting_x - radius + self.width/2*math.sin(math.radians(track_angle))
            self.y_position = starting_y - radius * math.tan(math.radians(track_angle)) - self.height/2*math.cos(math.radians(track_angle)) + 1
        self.side_image = pygame.Surface((self.width, self.height))
        self.side_image.set_colorkey((255, 255, 255))
        self.side_image = pygame.transform.rotate(self.side_image, 90 - track_angle)


class image:
    def __init__(self, x_position, y_position, width, height, picture, colour):
        self.x_position = x_position
        self.y_position = y_position
        self.width = width
        self.height = height
        self.picture = picture
        self.colour = colour
        self.image = pygame.transform.scale(self.picture, (self.width, self.height))


class ball:
    def __init__(self, colour, starting_x_position, starting_y_position, x_position, y_position, x_velocity, y_velocity,
                 x_acceleration, y_acceleration, radius):
        self.colour = colour
        self.starting_x_position = starting_x_position
        self.starting_y_position = starting_y_position
        self.x_position = x_position
        self.y_position = y_position
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.x_acceleration = x_acceleration
        self.y_acceleration = y_acceleration
        self.radius = radius


class planet:
    def __init__(self, colour, x_position, y_position, x_velocity, y_velocity, radius, mass):
        self.colour = colour
        self.x_position = x_position
        self.y_position = y_position
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.x_acceleration = 0
        self.y_acceleration = 0
        self.radius = radius
        self.mass = mass

    def calculate_stats(self, planet_array):
        gravitational_constant = 6.6743 * 10 ** -11

        new_planet_array = planet_array.copy()
        new_planet_array.remove(self)
        for other_body in new_planet_array:
            dx = self.x_position - other_body.x_position
            dy = self.y_position - other_body.y_position

            distance = math.sqrt(dx ** 2 + dy ** 2)
            try:
                force = gravitational_constant * self.mass * other_body.mass / distance ** 2
            except ZeroDivisionError:
                force = 0
            angle = math.atan2(dy, dx)

            self.x_acceleration -= force * math.cos(angle) / self.mass
            self.y_acceleration -= force * math.sin(angle) / self.mass

        return planet_array

    def calculate_position(self, dt):
        self.x_velocity += self.x_acceleration * dt
        self.y_velocity += self.y_acceleration * dt
        self.x_position += self.x_velocity * dt
        self.y_position += self.y_velocity * dt

    def calculate_collision(self, planet_array):
        new_planet_array = planet_array.copy()
        new_planet_array.remove(self)

        for other_body in new_planet_array:
            dx = self.x_position - other_body.x_position
            dy = self.y_position - other_body.y_position
            distance = math.sqrt(dx ** 2 + dy ** 2)

            if self in planet_array:
                if distance <= self.radius or distance <= other_body.radius:
                    planet_array.remove(self)
                    planet_array.remove(other_body)
                    body = planet(self.colour, (self.x_position + other_body.x_position) / 2, (self.y_position + other_body.y_position) / 2, (self.x_velocity * self.mass + other_body.x_velocity * other_body.mass) / (self.mass + other_body.mass), (self.y_velocity * self.mass + other_body.y_velocity * other_body.mass) / (self.mass + other_body.mass), (self.radius + other_body.radius)/2, self.mass + other_body.mass)
                    planet_array.append(body)
        return planet_array


class triangle:
    def __init__(self, point_1, point_2, point_3, colour):
        self.radius = point_1[0] - point_2[0]
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3
        self.colour = colour

    def update_triangle(self, track_angle, radius, starting_x, starting_y):
        if radius > 2000:
            self.point_2 = (0, self.point_1[1])
            self.point_3 = (self.point_2[0], starting_y - starting_x * math.tan(math.radians(track_angle)))
        else:
            self.point_2 = (self.point_1[0] - int(radius) - 80 * math.cos(math.radians(track_angle)), self.point_1[1])
            self.point_3 = (self.point_2[0], (int(self.point_2[1] - radius * math.tan(math.radians(track_angle)))) - 80 * math.sin(math.radians(track_angle)))
