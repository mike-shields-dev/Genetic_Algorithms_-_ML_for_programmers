from .escape import has_escaped


def store_position_data(t, history):
    [posX, posY] = t.position()
    history.append([posX, posY, has_escaped([posX, posY])])

def draw_square(t, size):
    history = []
    t.pendown()
    for _ in range(4):
        t.forward(size)
        t.left(90)
        store_position_data(t, history)
    t.penup()
    return history

def draw_concentric_squares_until_escaped(t, count, step_size):
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

def draw_concentric_squares(t, count):
    history = draw_concentric_squares_until_escaped(t, count, 10)
    with open("data_square", "wb") as file:
        import pickle
        pickle.dump(history, file)