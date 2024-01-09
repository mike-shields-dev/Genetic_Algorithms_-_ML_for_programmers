import turtle

from .bag import draw_bag
from .draw_line import draw_line
from .draw_spirals import draw_spirals_and_dump_history
from .draw_squares import draw_squares_and_dump_history


def attempt_escape(t):
    t.shape("turtle")
    t.pen(pencolor="green", pensize=2)

    # Use the various methods of escape
    # draw_line(t)
    # draw_squares_and_dump_history(t, 100)
    draw_spirals_and_dump_history(t, 5)


if __name__ == "__main__":
    t = turtle.Turtle()
    turtle.setworldcoordinates(-70.0, -70.0, 70.0, 70.0)
    draw_bag(t)
    attempt_escape(t)
    turtle.mainloop()
