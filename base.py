from enum import Enum

class Win(Exception):
    pass

class Draw(Exception):
    pass

class Resign(Exception):
    pass

class State(Enum):
    DRAW = 0
    X_WIN = 1
    O_WIN = 2
    NEUTRAL = 3

EMPTY_BOARD = [None] * 9
