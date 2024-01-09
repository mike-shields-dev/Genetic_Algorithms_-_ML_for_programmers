import os
import pickle
import random

from .escape import has_escaped
from .store_position_data import store_position_data

# Uses the turtle to draw a spiral
# until the turtles position is outside the bag

def draw_spiral(t):
    history = []
    t.penup()
    t.home()
    t.pendown()
    t.left(random.randint(0, 360))
    i = 0
    turnAngle = 360 / random.randint(3, 10)
    store_position_data(t, history)
    while not has_escaped(t.position()):
        t.right(turnAngle)
        t.forward(i * 5)
        store_position_data(t, history)
        i += 1
    t.penup()
    return history

def draw_spirals_and_dump_history(t, count):
    history = []
    for i in range(count):
        t.home()
        history.extend(draw_spiral(t))
        
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "data_dumps", "data_spirals")

    with open(file_path, "wb") as file:
        pickle.dump(history, file)
