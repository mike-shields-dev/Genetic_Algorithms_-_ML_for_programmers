import turtle

from Chapter1_Escape.bag import draw_bag
from Chapter1_Escape.draw_line_until_escaped import draw_line_until_escaped
from Chapter1_Escape.draw_squares_until_escaped import draw_squares_until_escaped


def attempt_escape(t):
    # draw_line_until_escaped(t)
    draw_squares_until_escaped(t, 100)

if __name__ == "__main__":
    t = turtle.Turtle()
    turtle.setworldcoordinates(-70., -70., 70., 70.)
    draw_bag(t)
    attempt_escape(t)
    turtle.mainloop()
