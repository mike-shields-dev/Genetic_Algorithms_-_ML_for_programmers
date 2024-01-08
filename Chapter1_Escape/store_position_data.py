from .escape import has_escaped


def store_position_data(t, history):
    [posX, posY] = t.position()
    history.append([posX, posY, has_escaped([posX, posY])])