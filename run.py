import random

def main():
    intro_message = intro()
    board = createBoard()
    print_board = printBoard()
    player_symbol = playerSym()
    checker = boardCheck(board, player_1, player_2)


def intro():
    """
    Function to give a message for the player and outline rules
    """
    print("Ready to play Tic Tac Toe?!/n")
    print("First to get 3 in a row wins!/n")
    print("Press enter to continue /n")

def createBoard():
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]        
    return board