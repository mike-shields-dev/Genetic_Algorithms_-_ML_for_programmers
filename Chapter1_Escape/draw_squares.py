from .escape import has_escaped
from .store_position_data import store_position_data

# Use turtle to draw a single square

def draw_square(t, size):
    history = []
    t.pendown()
    sides = 4
    for _ in range(sides):
        t.forward(size)
        t.left(90)
        store_position_data(t, history)
    t.penup()
    return history

# Use turtle to draw concentric squares 
# until the turtles position is outside of the bag

def draw_squares(t, count, step_size):
    history = []
    t.home()
    i = 1
    while i < count:
        t.penup()
        t.goto(-i * step_size / 2, -i * step_size / 2)
        if has_escaped(t.position()): 
            break
        t.pendown()
        history.extend(draw_square(t, i * 10))
        i += 1
    return history

def draw_squares_and_dump_history(t, count):
    history = draw_squares(t, count, 10)
    with open("data_square", "wb") as file:
        import pickle
        pickle.dump(history, file)