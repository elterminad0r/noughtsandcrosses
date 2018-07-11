"""
Play noughts and crosses
"""

from argparse import ArgumentParser
from itertools import cycle, repeat

from base import GameFinish, Draw
from interface import SquareInt, do_player_move
from computer import do_computer_move
from formatting import print_board

def get_args():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("-c", "--computer", action="store_true",
                    help="play against computer opponent")
    parser.add_argument("--headstart", action="store_true",
                    help="start first when playing against computer")
    parser.add_argument("--noughts-start", action="store_true",
                    help="noughts to start instead of crosses")
    parser.add_argument("-s", "--size", type=int, default=3,
                    help="size of board to play on")
    return parser.parse_args()

def play(board, players, noughts_start):
    is_crosses = not noughts_start
    try:
        for player in players:
            player(board, is_crosses)
            is_crosses = not is_crosses
            if board.count(None) == 0:
                raise Draw("Nobody wins!")
    except GameFinish as gf:
        print("{}: {}".format(type(gf).__name__, gf))

if __name__ == "__main__":
    args = get_args()
    if args.computer:
        if args.headstart:
            players = cycle([do_player_move, do_computer_move])
        else:
            players = cycle([do_computer_move, do_player_move])
    else:
        players = repeat(do_player_move)
    play([None] * args.size ** 2, players, args.noughts_start)
