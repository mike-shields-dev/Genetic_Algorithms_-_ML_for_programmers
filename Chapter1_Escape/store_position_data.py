from .escape import has_escaped

# Store the previous positions of the turtle
# in the provided history list


def store_position_data(t, history):
    [posX, posY] = t.position()
    history.append([posX, posY, has_escaped([posX, posY])])
