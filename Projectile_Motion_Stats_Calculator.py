import math


def projectile_motion_stats_calculator(launch_velocity, launch_angle, gravity, projectile, WIDTH, HEIGHT):
    max_height = launch_velocity * launch_velocity * math.sin(launch_angle) * math.sin(launch_angle) / (2 * gravity) + 2*HEIGHT/3 - projectile.radius - projectile.starting_y_position
    time_of_flight = ((launch_velocity * math.sin(launch_angle)) + math.sqrt((launch_velocity * math.sin(launch_angle) * launch_velocity * math.sin(launch_angle)) + (2 * (2*HEIGHT/3 - projectile.radius - projectile.starting_y_position) * gravity))) / gravity
    horizontal_range = launch_velocity * math.cos(launch_angle) * time_of_flight + (projectile.starting_x_position - WIDTH/10)
    return max_height, horizontal_range, time_of_flight
