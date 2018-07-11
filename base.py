from enum import Enum

class GameFinish(Exception):
    pass

class Win(GameFinish):
    pass

class Draw(GameFinish):
    pass

class State(Enum):
    DRAW = 0
    X_WIN = 1
    O_WIN = 2
    NEUTRAL = 3
