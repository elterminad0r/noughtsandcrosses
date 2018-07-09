"""
Handling and verifying user input
"""

name_from_bool = ["noughts", "crosses"]

state_from_string = {"_": None, 'x': True, 'o': False}

def isqrt(n):
    if n < 2:
        return n
    else:
        smallCandidate = isqrt(n >> 2) << 1
        largeCandidate = smallCandidate + 1
        if largeCandidate ** 2 > n:
            return smallCandidate
        else:
            return largeCandidate

def parse_board(board):
    b = [state_from_string[c] for c in board if c in state_from_string]
    if isqrt(len(b)) ** 2 != len(b):
        raise ValueError('The board must be square')
    return b

def get_pos(s):
    """
    Get position in 1d list from 2d coordinate reference
    """
    x, y = map(int, s.split())
    if not all(0 <= c <= 2 for c in (x, y)):
        raise ValueError("Not in range 0-2")

    return y * 3 + x

def get_input(board, is_crosses):
    """
    Get user input
    """
    print("You are playing as {}".format(name_from_bool[is_crosses]))
    while True:
        try:
            mov = get_pos(input("Enter the position you want to play in > "))
            if board[mov] is not None:
                raise ValueError("This position is already taken")
        except ValueError as ve:
            print(ve)
            continue
        return mov
