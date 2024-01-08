from .escape import has_escaped


def draw_line_until_escaped(t):
    angle = 0
    step = 5
    t.home()
    t.pendown()
    t.shape('turtle')
    t.pen(pencolor='green', pensize=5)
    t.forward(5)
    while not has_escaped(t.position()):
        t.left(angle)
        t.forward(step)
    t.penup()