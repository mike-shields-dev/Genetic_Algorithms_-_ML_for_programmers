# Uses a turtle instance to draw a bag.


def draw_bag(t):
    t.pen(pencolor="brown", pensize=5)
    t.penup()
    t.goto(-35, 35)
    t.pendown()
    t.right(90)
    t.forward(70)
    t.left(90)
    t.forward(70)
    t.left(90)
    t.forward(70)
    t.penup()
