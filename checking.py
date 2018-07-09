"""
Functions implementing grid checks
"""

from argparse import ArgumentParser

from base import State
from formatting import get_board_template

def get_args():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("n", type=int, help="size of board to check")
    return parser.parse_args()

def get_groups(n):
    rows = ([r for i in range(n)
               for r in [range(i * n, i * n + n), range(i, i + n ** 2, n)]]
          + [range(0, n ** 2, n + 1), range(n - 1, n ** 2 - n + 1, n - 1)])

    return [[r for r in rows if i in r] for i in range(n ** 2)]

groups = get_groups(3)

def is_run(board, pos):
    """
    Check if one tile is a part of any complete groups.
    """
    return any(len(set(board[i] for i in group)) == 1 for group in groups[pos])

def get_state(board):
    """
    Get state of board. This function is given no information about position
    so is necessarily much slower. If you do know the last played tile, use
    is_run instead, as this only checks all groups pertaining to that tile.
    """
    for pos, m in enumerate(board):
        if m is not None:
            if is_run(board, pos):
                if m:
                    return State.X_WIN
                return State.O_WIN

    if board.count(None) == 0:
        return State.DRAW
    return State.NEUTRAL

def show_groups(n):
    board_temp = get_board_template(n)
    for ind, pos in enumerate(get_groups(n)):
        print(ind, pos)
        for g in pos:
            dft = [" "] * n ** 2
            for i in g:
                dft[i] = "G"
            dft[ind] = 'M'
            print(board_temp.format(*dft), end="\n\n")

if __name__ == "__main__":
    args = get_args()
    show_groups(args.n)
