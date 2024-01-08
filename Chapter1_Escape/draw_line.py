from .escape import has_escaped

# Uses a turtle to draw a line until
# the turtles position is outside of the bag

def draw_line(t):
    angle = 0
    step = 5
    t.home()
    t.pendown()
    t.forward(5)
    while not has_escaped(t.position()):
        t.left(angle)
        t.forward(step)
    t.penup()