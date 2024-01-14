import math


def displacement_calculator(starting_x_position, starting_y_position, launch_angle, launch_velocity, time, gravity):
    x_position = time * launch_velocity * math.cos(math.radians(launch_angle)) + starting_x_position
    y_position = ((time * time * gravity) / 2) - time * launch_velocity * math.sin(math.radians(launch_angle)) + starting_y_position
    return x_position, y_position
