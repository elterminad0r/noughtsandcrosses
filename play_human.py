"""
Play noughts and crosses
"""

from interface import get_input
from checking import get_state, State
from formatting import print_board

def do_player_move(board, is_crosses):
    """
    Execute player move - assumes board is valid at start of turn
    """
    print_board(board)
    pos = get_input(board, is_crosses)
    board[pos] = is_crosses
    st = get_state(board)
    if st == State.DRAW:
        raise Draw()
    elif st in (State.X_WIN, State.O_WIN):
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
    play([None] * 9)
