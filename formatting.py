"""
Pretty-printing OXO boards
"""

from argparse import ArgumentParser
from random import choices

def get_args():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("n", type=int, help="size of demo board")
    return parser.parse_args()

def get_board_template(n):
    width = len(str(n - 1))
    return ("{}\n{}"
              .format("".join(map("{:4}".format, range(n))),
                  "  {}".format("+".join(["---"] * n))
                     .join("\n\n").
                         join(map("{0[0]:2}{0[1]}".format,
                                  enumerate(["|".join([" {} "] * n)] * n)))))

BOARD_TEMP = get_board_template(3)

def strfboard(board):
    return BOARD_TEMP.format(*map(get_sym, board))

def print_board(board):
    print("{}\n".format(strfboard(board)))

syms = "OX"

def get_sym(i):
    if i is None:
        return " "
    return syms[i]

if __name__ == "__main__":
    args = get_args()
    n = args.n
    n_temp = get_board_template(n)
    print("{0}x{0} template:\n{1}".format(n, n_temp))
    print("\nrandom {0}x{0} board:".format(n))
    print(n_temp.format(*map(get_sym, (choices([None, True, False], k=n**2)))))
