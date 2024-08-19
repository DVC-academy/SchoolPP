import random


def move(board, size):
    while True:
        row, col = random.randint(0, size-1), random.randint(0, size-1)
        if board[row][col] == '.':
            return row, col
