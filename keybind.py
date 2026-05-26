import ctypes
keybind = ctypes.CDLL("./Keybind.dll")

keybind.moveUp.restype = ctypes.c_bool
keybind.moveDown.restype = ctypes.c_bool
keybind.moveLeft.restype = ctypes.c_bool
keybind.moveRight.restype = ctypes.c_bool
keybind.spacedown.restype = ctypes.c_bool


def move_up():
    return keybind.moveUp()

def move_down():
    return keybind.moveDown()

def move_left():
    return keybind.moveLeft()

def move_right():
    return keybind.moveRight()

def space_key():
    return keybind.spacedown()







