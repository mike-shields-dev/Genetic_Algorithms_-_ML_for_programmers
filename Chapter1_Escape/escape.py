import turtle


def has_escaped(position):
    x = int(position[0])
    y = int(position[1])
    
    return x < -35 or x > 35 or y < -35 or y > 35

def draw_line():
    angle = 0
    step = 5
    t = turtle.Turtle()
    t.shape('turtle')
    t.pen(pencolor='green', pensize=5)
    t.pendown()
    t.forward(5)

    while not has_escaped(t.position()):
        t.left(angle)
        t.forward(step)

