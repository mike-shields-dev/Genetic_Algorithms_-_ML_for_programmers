import turtle

from Chapter1_Escape.bag import draw_bag
from Chapter1_Escape.draw_concentric_squares import draw_concentric_squares


def attempt_escape(t):
    t.shape('turtle')
    t.pen(pencolor='green', pensize=2)
    # draw_line(t)
    draw_concentric_squares(t, 100)

if __name__ == "__main__":
    t = turtle.Turtle()
    turtle.setworldcoordinates(-70., -70., 70., 70.)
    draw_bag(t)
    attempt_escape(t)
    turtle.mainloop()
