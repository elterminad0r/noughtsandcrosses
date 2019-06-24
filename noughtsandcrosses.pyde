# vim: ft=python

from random import choice

from computer import get_computer_move
from checking import is_run

DRAW_WIDTH = 0.8

def draw_board(board, n, w):
    pushMatrix()
    scale(w)
    for ind, tile in enumerate(board):
        if tile is not None:
            x, y = ind % n, ind // n
            if tile:
                rect(x + 0.5, y + 0.5, DRAW_WIDTH, DRAW_WIDTH)
            else:
                ellipse(x + 0.5, y + 0.5, DRAW_WIDTH, DRAW_WIDTH)
    popMatrix()

def setup():
    global board, gameover
    size(800, 800)
    fill(255)
    rectMode(CENTER)
    noStroke()
    background(0)
    board = [None] * 9

    gameover = None

    cmov = get_computer_move(board, True, 3)
    board[cmov] = True


def draw():
    global board
    if gameover is None:
        background(0)
    elif gameover == True:
        background(255, 0, 0)
    else:
        background(255, 255, 0)
    draw_board(board, 3, width / 3.0)
        
def mouseClicked():
    global gameover
    if not gameover:
        x, y = int(3 * mouseX / width), int(3 * mouseY / height)
        pos = 3 * y + x
        if board[pos] is None:
            print("click")
            board[pos] = False
            cmov = get_computer_move(board, True, 3)
            board[cmov] = True
            if is_run(board, cmov, 3):
                gameover = True
            elif board.count(None) == 0:
                gameover = False

def keyPressed():
    if keyCode == ord("R"):
        setup()
