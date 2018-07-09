from random import choice

def get_board_template(n):
    return ("  {}\n{}"
              .format("".join(map(" {} ".format, range(n))),
                  " {}".format("+".join(["---"] * n))
                     .join("\n\n").
                         join(map("{0[0]}{0[1]}".format,
                                  enumerate(["|".join([" {} "] * n)] * n)))))

BOARD_TEMP = get_board_template(3)

def strfboard(board):
    return BOARD_TEMP.format(*map(get_sym, board))

def print_board(board):
    print(strfboard(board))

syms = "OX"

def get_sym(i):
    if i is None:
        return " "
    return syms[i]

if __name__ == "__main__":
    print("3x3 template:\n{}".format(BOARD_TEMP))
    for i in range(2, 5):
        print("\nrandom {0}x{0} board:".format(i))
        print(get_board_template(i).format(*map(get_sym, (choice([None, True, False]) for _ in range(i ** 2)))))
