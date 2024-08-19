import random
import time

import player1
import player2
import bot1
import bot2


class TicTacToe:
    def __init__(self, size, win_length):
        self.size = size
        self.win_length = win_length
        self.board = [['.' for _ in range(size)] for _ in range(size)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print('|'.join(self.colorize(cell) for cell in row))

    def colorize(self, cell):
        if cell == 'X':
            return f"\033[91m{cell}\033[0m"  # Red for X
        elif cell == 'O':
            return f"\033[94m{cell}\033[0m"  # Blue for O
        else:
            return f"\033[97m{cell}\033[0m"  # White for empty cells

    def check_win(self, player):
        for row in range(self.size):
            for col in range(self.size):
                if self.check_line(player, row, col, 1, 0) or \
                   self.check_line(player, row, col, 0, 1) or \
                   self.check_line(player, row, col, 1, 1) or \
                   self.check_line(player, row, col, 1, -1):
                    return True
        return False

    def check_line(self, player, row, col, d_row, d_col):
        count = 0
        for i in range(self.win_length):
            r = row + i * d_row
            c = col + i * d_col
            if 0 <= r < self.size and 0 <= c < self.size and self.board[r][c] == player:
                count += 1
            else:
                break
        return count == self.win_length

    def check_draw(self):
        for row in self.board:
            if '.' in row:
                return False
        return True

    def make_move(self, row, col):
        if self.board[row][col] == '.':
            self.board[row][col] = self.current_player
            return True
        return False

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'


def main():
    size = 3
    win_length = 3
    game = TicTacToe(size, win_length)
    round = 1

    while True:
        print(f"Round {round}")
        round += 1
        game.print_board()
        if game.current_player == 'X':
            row, col = player2.move(game.board, size)
        else:
            row, col = bot2.move(game.board, size)

        if game.make_move(row, col):
            if game.check_win(game.current_player):
                print(f"Player {game.current_player} wins!")
                game.print_board()
                break
            elif game.check_draw():
                print("It's a draw!")
                game.print_board()
                break
            game.switch_player()
        else:
            print("Invalid move. Try again.")
        time.sleep(3)


if __name__ == "__main__":
    main()
