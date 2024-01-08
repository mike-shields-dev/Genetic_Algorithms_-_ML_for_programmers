import turtle

from Chapter1_Escape.bag import draw_bag
from Chapter1_Escape.escape import draw_line


def attempt_escape():
    draw_line()

if __name__ == "__main__":
    turtle.setworldcoordinates(-70., -70., 70., 70.)
    draw_bag()
    attempt_escape()
    turtle.mainloop()
