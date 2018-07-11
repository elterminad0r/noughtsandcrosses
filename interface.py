"""
Handling and verifying user input
"""

from base import Win
from formatting import print_board, syms
from checking import is_run

name_from_bool = ["noughts", "crosses"]

state_from_string = {"_": None, 'x': True, 'o': False}

def isqrt(n):
    if n < 2:
        return n
    else:
        smallCandidate = isqrt(n >> 2) << 1
        largeCandidate = smallCandidate + 1
        if largeCandidate ** 2 > n:
            return smallCandidate
        else:
            return largeCandidate

def SquareInt(s):
    """
    Acts as a "parser" for perfect square integers for argparse
    """
    n = int(s)
    if isqrt(n) ** 2 != n:
        raise ValueError("{!r} is not a square number".format(s))
    return n

def SquareBoard(board):
    b = [state_from_string[c] for c in board if c in state_from_string]
    if isqrt(len(b)) ** 2 != len(b):
        raise ValueError('The board must be square')
    return b

def get_pos(s):
    """
    Get position in 1d list from 2d coordinate reference
    """
    x, y = map(int, s.split())
    if not all(0 <= c <= 2 for c in (x, y)):
        raise ValueError("Not in range 0-2")

    return y * 3 + x

def get_input(board, is_crosses):
    """
    Get user input
    """
    print("You are playing as {}".format(name_from_bool[is_crosses]))
    while True:
        try:
            mov = get_pos(input("Enter the position you want to play in > "))
            if board[mov] is not None:
                raise ValueError("This position is already taken")
        except ValueError as ve:
            print(ve)
            continue
        return mov

def do_player_move(board, is_crosses):
    """
    Execute player move - assumes board is valid at start of turn
    """
    print_board(board)
    try:
        pos = get_input(board, is_crosses)
    except (KeyboardInterrupt, EOFError):
        raise Win("{} wins because {} is a coward".format(syms[not is_crosses], syms[is_crosses]))
    board[pos] = is_crosses
    if is_run(board, pos):
        raise Win("{} wins".format(syms[is_crosses]))
