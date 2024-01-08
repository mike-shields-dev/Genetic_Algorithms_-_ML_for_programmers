import turtle as t
from Chapter1_Escape.hello_turtle import draw_bag


if __name__ == "__main__":
    t.setworldcoordinates(-70., -70., 70., 70.)
    draw_bag()
    t.mainloop()