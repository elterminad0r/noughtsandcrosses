from enum import Enum

rows = ([r for i in range(3)
           for r in [range(i * 3, i * 3 + 3), range(i, i + 9, 3)]]
      + [range(0, 9, 4), range(2, 7, 2)])

groups = [[r for r in rows if i in r] for i in range(9)]

board_temp = ("  {}\n{}"
        .format("".join(map(" {} ".format, range(3))),
                " {}".format("+".join(["---"] * 3))
                   .join("\n\n").
                       join(map("{0[0]}{0[1]}".format,
                                enumerate(["|".join([" {} "] * 3)] * 3)))))

class States(Enum):
    DRAW = 0
    X_WIN = 1
    O_WIN = 2
    NEUTRAL = 3

def is_run(board, pos):
    return any(len(set(board[i] for i in group)) == 1 for group in groups[pos])

def state(board):
    """
    Get state of board
    """
    for pos, m in enumerate(board):
        if m is not None:
            if is_run(board, pos):
                if m:
                    return States.X_WIN
                return States.O_WIN

    if board.count(None) == 0:
        return States.DRAW
    return States.NEUTRAL

def show_groups():
    for ind, pos in enumerate(groups):
        for g in pos:
            dft = [" "] * 9
            for i in g:
                dft[i] = "G"
            print(ind, pos)
            print(board_temp.format(*dft))

if __name__ == "__main__":
    show_groups()
