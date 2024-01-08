import random

from .escape import has_escaped
from .store_position_data import store_position_data

# Uses the turtle to draw a spiral
# until the turtles position is outside the bag

def draw_spiral(t):
    t.penup()
    t.home()
    t.left(random.randint(0, 360))
    t.pendown()
    i = 0
    turnAngle = 360/random.randint(1, 10)
    while not has_escaped(t.position()):
        i += 1
        t.forward(i*5)
        t.right(turnAngle)