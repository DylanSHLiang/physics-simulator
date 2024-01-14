import math


def banked_tracks_stats_calculator(speed, mass, gravity, track_angle, friction):
    if speed and mass and gravity:
        gravity_force = mass * gravity
        if track_angle:
            if track_angle == 90:
                return 0, 0, 0, 0, 0, 0, 0, 0
            else:
                if friction < math.tan(math.pi * track_angle / 180) and friction * math.tan(math.pi * track_angle / 180) < 1:
                    normal_force = gravity_force / math.cos(math.pi * track_angle / 180)
                    radius = speed * speed / (gravity * math.tan(math.pi * track_angle / 180))
                    period = 2 * math.pi * radius / speed
                    angular_speed = speed / radius
                    max_speed = math.sqrt((radius * gravity * (math.tan(math.pi * track_angle / 180) + friction) / (1 - (friction * math.tan(math.pi * track_angle / 180)))))
                    min_speed = math.sqrt((radius * gravity * (math.tan(math.pi * track_angle / 180) - friction) / (1 + (friction * math.tan(math.pi * track_angle / 180)))))
                    net_force = normal_force * math.sin(math.pi * track_angle / 180)
                    return gravity_force, normal_force, net_force, radius, period, angular_speed, min_speed, max_speed
                else:
                    return 0, 0, 0, 0, 0, 0, 0, 0
        elif friction:
            normal_force = gravity_force
            radius = speed * speed / (gravity * friction)
            period = 2 * math.pi * radius / speed
            angular_speed = speed / radius
            min_speed = 0
            max_speed = math.sqrt(radius * gravity * friction)
            return gravity_force, normal_force, 0, radius, period, angular_speed, min_speed, max_speed
        else:
            return 0, 0, 0, 0, 0, 0, 0, 0
    else:
        return 0, 0, 0, 0, 0, 0, 0, 0
