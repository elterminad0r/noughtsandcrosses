"""
Play noughts and crosses. Incorporates both human and computer players.
"""

from argparse import ArgumentParser
from itertools import cycle, repeat

from base import GameFinish, Draw
from interface import do_player_move
from computer import do_computer_move as _do_computer_move

def get_args():
    """
    Get configuration for the program. See the help text for details.
    """
    parser = ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("-c", "--computer", action="store_true",
                    help="play against computer opponent")
    mode.add_argument("-b", "--battle", action="store_true",
                    help="computer plays against itself")
    parser.add_argument("--headstart", action="store_true",
                    help="start first when playing against computer")
    parser.add_argument("--noughts-start", action="store_true",
                    help="noughts to start instead of crosses")
    parser.add_argument("-s", "--size", type=int, default=3,
                    help="size of board to play on")
    parser.add_argument("-v", "--verbose", action="store_true",
                    help="Show minmax thought process")
    return parser.parse_args()

def play(board, players, noughts_start, n):
    """
    Play a game of noughts and crosses until a finishing condition or a draw,
    given an infinite iterable of players.
    """
    is_crosses = not noughts_start
    try:
        for player in players:
            player(board, is_crosses, n)
            is_crosses = not is_crosses
            if board.count(None) == 0:
                raise Draw("Nobody wins!")
    except GameFinish as gf:
        print("{}: {}".format(type(gf).__name__, gf))

if __name__ == "__main__":
    args = get_args()
    # Correctly initialise the infinite iterable of players according to
    # arguments
    vb = args.verbose
    do_computer_move = lambda *args: _do_computer_move(*args, verbose=vb)
    if args.computer:
        if args.headstart:
            players = cycle([do_player_move, do_computer_move])
        else:
            players = cycle([do_computer_move, do_player_move])
    elif args.battle:
        players = repeat(do_computer_move)
    else:
        players = repeat(do_player_move)
    play([None] * args.size ** 2, players, args.noughts_start, args.size)
