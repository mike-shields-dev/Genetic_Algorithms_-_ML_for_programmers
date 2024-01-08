import turtle

from Chapter1_Escape.bag import draw_bag
from Chapter1_Escape.draw_line import draw_line
from Chapter1_Escape.draw_spiral import draw_spiral
from Chapter1_Escape.draw_squares import draw_squares_and_dump_history


def attempt_escape(t):
    t.shape('turtle')
    t.pen(pencolor='green', pensize=2)
    
    draw_line(t)
    draw_squares_and_dump_history(t, 100)
    draw_spiral(t)

if __name__ == "__main__":
    t = turtle.Turtle()
    turtle.setworldcoordinates(-70., -70., 70., 70.)
    draw_bag(t)
    attempt_escape(t)
    turtle.mainloop()
