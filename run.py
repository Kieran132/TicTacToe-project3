import random

def main():
    intro_message = intro()
    board = create_board()
    print_board = printBoard()
    player_symbol = player_sym()
    checker = boardCheck(board, player_1, player_2)


def intro():
    """
    Function to give a message for the player and outline rules
    """
    print("Ready to play Tic Tac Toe?!/n")
    print("First to get 3 in a row wins!/n")
    print("Press enter to continue /n")

def create_board():
    """
    Function to create layout of a blank board
    """
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]        
    return board

def player_sym():
    """
    Function that allows the players to choose which symbol they want
    """
    player_1 = input("Player 1, please choose your symbol, X or O?")
    if player_1 == "X":
        player_2 = "O"
        print("Player 2, you are O")
    else:
        player_2 = "X"
        print("Player 2, you are X")
    input("Press Enter to play!")
    print("/n")
    return (player_1, player_2)