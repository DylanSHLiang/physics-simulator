import math


def circular_motion_stats_calculator(force, mass, speed):
    acceleration = force / mass
    radius = speed * speed / acceleration
    period = 2 * math.pi * radius / speed
    angular_speed = speed / radius
    return radius, period, angular_speed

