"""
Implementation of minmax algorithm
"""

from textwrap import indent
from traceback import extract_stack

from base import Resign
from checking import get_state, State
from formatting import print_board, strfboard, syms
from interface import parse_board

from argparse import ArgumentParser

def get_args():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("-b", "--board", type=parse_board, default='_o__x____',
                    help='The initial board state')
    return parser.parse_args()

state_from_bool = [State.O_WIN, State.X_WIN]

def optimise(evaluations, is_crosses):
    LOSE_STATE, WIN_STATE = state_from_bool[not is_crosses], state_from_bool[is_crosses]
    draw_seen = False
    for e in evaluations:
        if e == LOSE_STATE:
            return e
        elif e == State.DRAW:
            draw_seen = True
    if draw_seen:
        return State.DRAW
    return WIN_STATE

def generate_moves(board, is_crosses):
    broken = True
    for ind, i in enumerate(board):
        if i is None:
            try:
                board[ind] = is_crosses
                yield ind, board
            finally:
                board[ind] = None

def evaluate_board(board, is_crosses):
    print(indent("examining as {}:\n{}".format(syms[is_crosses], indent(strfboard(board), ' ')), ' ' * len(extract_stack())))

    state = get_state(board)
    if state == State.NEUTRAL:
        return optimise((evaluate_board(board, not is_crosses) for move, board in generate_moves(board, is_crosses)), is_crosses)
    else:
        return state

def do_computer_move(board, is_crosses):
    WIN_STATE = state_from_bool[is_crosses]
    moves = generate_moves(board, is_crosses)
    for move, board in moves:
        if evaluate_board(board, is_crosses) == WIN_STATE:
            return move
    raise Resign('Computer is stuck')

if __name__ == "__main__":
    args = get_args()
    board = args.board
    print_board(board)
    move = do_computer_move(board, True)
    print("computer selects {}".format(move))
    board[move] = True
    print_board(board)
