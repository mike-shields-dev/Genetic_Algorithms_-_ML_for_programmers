# Use the turtles position
# to check whether it is outside
# of the bag


def has_escaped(position):
    x = int(position[0])
    y = int(position[1])
    return x < -35 or x > 35 or y < -35 or y > 35
