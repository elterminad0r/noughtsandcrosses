"""
Implementation of minmax algorithm
"""

from textwrap import indent
from traceback import extract_stack

from base import Win
from checking import get_state, State, is_run
from formatting import print_board, strfboard, syms
from interface import SquareBoard

from argparse import ArgumentParser

def get_args():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("-b", "--board", type=SquareBoard, default='_o__x____',
                    help='The initial board state')
    parser.add_argument("-q", "--quiet", action="store_true",
                    help="do not print minmax tree")
    return parser.parse_args()

state_from_bool = [State.O_WIN, State.X_WIN]

def maximise(evaluations, is_crosses):
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

def minimise(evaluations, is_crosses):
    LOSE_STATE, WIN_STATE = state_from_bool[not is_crosses], state_from_bool[is_crosses]
    draw_seen = False
    for e in evaluations:
        if e == WIN_STATE:
            return e
        elif e == State.DRAW:
            draw_seen = True
    if draw_seen:
        return State.DRAW
    return LOSE_STATE

def generate_moves(board, is_crosses):
    broken = True
    for ind, i in enumerate(board):
        if i is None:
            try:
                board[ind] = is_crosses
                yield ind, board
            finally:
                board[ind] = None

def evaluate_board(board, is_crosses, crosses_playing, verbose=False):
    verbose and print(indent("examining as {}:\n{}".format(syms[crosses_playing], indent(strfboard(board), ' ')), ' ' * len(extract_stack())))

    state = get_state(board)
    if state == State.NEUTRAL:
        evaluations = (evaluate_board(board, is_crosses, not crosses_playing, verbose=verbose) for move, board in generate_moves(board, crosses_playing))
        if is_crosses ^ crosses_playing:
            return maximise(evaluations, is_crosses)
        else:
            return minimise(evaluations, is_crosses)
    else:
        verbose and print(indent("state here: {}".format(state), " " * len(extract_stack())))
        return state

def get_computer_move(board, is_crosses, verbose=False):
    if all(i is None for i in board):
        return 0
    WIN_STATE = state_from_bool[is_crosses]
    moves = generate_moves(board, is_crosses)
    draw = None
    for move, board in moves:
        ev = evaluate_board(board, is_crosses, not is_crosses, verbose=verbose)
        if ev == WIN_STATE:
            verbose and print("Win incoming")
            return move
        elif ev == State.DRAW:
            verbose and print("Draw forcable")
            draw = move
    if draw is not None:
        return draw
    return board.index(None)

def do_computer_move(board, is_crosses, verbose=False):
    move = get_computer_move(board, is_crosses, verbose=verbose)
    board[move] = is_crosses
    print("Computer plays at ({}, {})".format(move % 3, move // 3))
    print_board(board)
    if is_run(board, move):
        raise Win("I'm sorry, Dave. I'm afraid I can't do that.")

if __name__ == "__main__":
    args = get_args()
    board = args.board
    print_board(board)
    do_computer_move(board, True, True)
