import turtle
import argparse
import inspect

from .bag import draw_bag
from .draw_line import draw_line
from .draw_spirals import draw_spirals_and_dump_history
from .draw_squares import draw_squares_and_dump_history


if __name__ == "__main__":
    fns = {
        "line": draw_line,
        "squares": draw_squares_and_dump_history,
        "spirals": draw_spirals_and_dump_history,
    }

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f", "--function", choices=fns, help="One of " + ",".join(fns.keys())
    )
    parser.add_argument("-n", "--number", default=50, type=int, help="How many?")
    args = parser.parse_args()


try:
    turtle.setworldcoordinates(-70.0, -70.0, 70.0, 70.0)
    t = turtle.Turtle()
    draw_bag(t)
    t.pencolor("green")
    t.pensize(2)
    fn = fns[args.function]
    if len(inspect.getfullargspec(fn).args) == 2:
        fn(t, args.number)
    else:
        fn(t)
    turtle.mainloop()
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)

    x, y = inst.args
    print("y =", y)
    parser.print_help()