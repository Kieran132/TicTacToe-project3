import random

def main():
    intro_message = intro()
    board = createBoard()
    print_board = printBoard()
    player_symbol = playerSym()
    checker = boardCheck(board, player_1, player_2)