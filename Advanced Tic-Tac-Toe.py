# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 21:56:17 2024

@author: NIHAR MAHAJAN
"""

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.winner = None
        self.small_boards = [[None for _ in range(3)] for _ in range(3)]

    def print_board(self):
        for row in self.board:
            print(' | '.join(row))
            print('-' * 9)

    def print_small_boards(self):
        for i in range(3):
            for j in range(3):
                print(f"Board {i + 1}-{j + 1}:")
                for row in self.small_boards[i][j]:
                    print(' | '.join(row))
                    print('-' * 9)
                print()

    def make_move(self, big_row, big_col, small_row, small_col):
        if self.winner:
            print(f"Player {self.winner} has already won the game!")
            return

        if self.small_boards[big_row][big_col] is not None or self.board[small_row][small_col] != ' ':
            print("Invalid move. Try again.")
            return

        self.small_boards[big_row][big_col] = self.current_player
        self.board[small_row][small_col] = self.current_player

        if self.check_small_board_win(small_row, small_col) or self.check_big_board_win(big_row, big_col):
            self.winner = self.current_player
            print(f"Player {self.winner} wins!")

        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_small_board_win(self, row, col):
        return self.check_row_win(row) or self.check_col_win(col) or self.check_diagonal_win()

    def check_big_board_win(self, big_row, big_col):
        return self.check_row_win(big_row, big=True) or self.check_col_win(big_col, big=True) or self.check_diagonal_win(big=True)

    def check_row_win(self, row, big=False):
        board = self.board if not big else self.small_boards[row]
        return all(cell == self.current_player for cell in board[row])

    def check_col_win(self, col, big=False):
        board = self.board if not big else [self.small_boards[row][col] for row in range(3)]
        return all(cell == self.current_player for cell in board)

    def check_diagonal_win(self, big=False):
        if not big:
            return all(self.board[i][i] == self.current_player for i in range(3)) or \
                   all(self.board[i][2 - i] == self.current_player for i in range(3))
        else:
            return all(self.small_boards[i][i][i] == self.current_player for i in range(3)) or \
                   all(self.small_boards[i][2 - i][i] == self.current_player for i in range(3))


# Example usage:
game = TicTacToe()

while not game.winner:
    game.print_small_boards()
    game.print_board()

    big_row = int(input("Enter the big row (1-3): ")) - 1
    big_col = int(input("Enter the big column (1-3): ")) - 1
    small_row = int(input("Enter the small row (1-3): ")) - 1
    small_col = int(input("Enter the small column (1-3): ")) - 1

    game.make_move(big_row, big_col, small_row, small_col)