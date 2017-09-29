"""
Handling and verifying user input
"""

name_from_bool = ["noughts", "crosses"]

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
