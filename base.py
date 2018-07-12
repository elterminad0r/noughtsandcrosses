"""
Base module with a couple of shared types
"""

class GameFinish(Exception):
    """
    Exception to throw when a game is finished
    """
    pass

class Win(GameFinish):
    """
    If a game is won
    """
    pass

class Draw(GameFinish):
    """
    If a game is drawn
    """
    pass

class State(object):
    """
    Enum to represent the possible states of a board
    """
    DRAW = 0
    X_WIN = 1
    O_WIN = 2
    NEUTRAL = 3
