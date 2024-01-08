from .escape import has_escaped


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