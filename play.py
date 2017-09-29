"""
Play noughts and crosses
"""

from interface import get_input
from checking import state, States, board_temp

board = [None] * 9

def print_board(board):
    print(board_temp.format(*map(get_sym, board)))

syms = "OX"

def get_sym(i):
    if i is None:
        return " "
    return syms[i]
class Win(Exception):
    pass

class Draw(Exception):
    pass

def do_player_move(board, is_crosses):
    """
    Execute player move - assumes board is valid at start of turn
    """
    print_board(board)

    pos = get_input(board, is_crosses)
    board[pos] = is_crosses

    st = state(board)
    if st == States.DRAW:
        raise Draw()
    elif st in (States.X_WIN, States.O_WIN):
        raise Win(st)

def play(board):
    try:
        playing = False
        while True:
            do_player_move(board, playing)
            playing = not playing
    finally:
        print_board(board)

if __name__ == "__main__":
    play(board)
