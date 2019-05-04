def clock_angle(hour, min):
    MINUTES_PER_HOUR = 60
    DEGREES_PER_MIN = 360 / MINUTES_PER_HOUR
    DEGREES_PER_HOUR = 360 / 12

    min_angle = min * DEGREES_PER_MIN
    hour_angle = hour * DEGREES_PER_HOUR + (min / MINUTES_PER_HOUR) * DEGREES_PER_HOUR
    diff = abs(min_angle - hour_angle)
    if diff > 180:
        return 360 - diff
    return diff

def clock_angle2(hour, minute):
    MINUTES_PER_HOUR = 60
    DEGREES_PER_MIN = 360 / MINUTES_PER_HOUR
    DEGREES_PER_HOUR = 360 / 12

    min_angle = minute * DEGREES_PER_MIN
    hour_angle = hour * DEGREES_PER_HOUR  + (minute / MINUTES_PER_HOUR) * DEGREES_PER_HOUR
    diff = abs(min_angle - hour_angle)
    if diff > 180:
        return 360 - diff
    return diff