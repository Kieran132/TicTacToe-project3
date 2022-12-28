import random


def main():
    intro_message = intro()
    board = create_board()
    print_board = printing_board(board)
    player_1, player_2 = player_sym()
    checker = board_check(board, player_1, player_2)


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


def start(board, player_1, player_2, count):
    """
    Function to start the game
    """
    if count % 2 == 0:
        player = player_1
    elif count % 2 == 1:
        player = player_2
    print("Player" + player + ", it is your turn.")
    row = int(input("Pick a row:"
                    "[upper row: enter 0, middle row: enter 1, bottom row: enter 2]:"))
    column = int(input("Pick a column:"
                       "[left column: enter 0, middle column: enter 1, right column enter 2]"))

    while (row > 2 or row < 0) or (column > 2 or column < 0):
        off_board(row, column)
        row = int(input("Pick a row[upper row:"
                        "[enter 0, middle row: enter 1, bottom row: enter 2]:"))
        column = int(input("Pick a column:"
                           "[left column: enter 0, middle column: enter 1, right column enter 2]"))

    while (board[row][column] == player_1) or (board[row][column] == player_2):
        fill = wrong(board, player_1, player_2, row, column)
        row = int(input("Pick a row[upper row:"
                        "[enter 0, middle row: enter 1, bottom row: enter 2]:"))
        column = int(input("Pick a column:"
                            "[left column: enter 0, middle column: enter 1, right column enter 2]")) 
        
    if player == player_1:
        board[row][column] = player_1
    else:
        board[row][column] = player_2
    return (board)


def board_check(board, player_1, player_2):
    count = 1
    winner = True

    while count < 10 and winner == True:
        gaming = start(board, player_1, player_2, count)
        print_board = printing_board(board)

        if count == 9:
            print("Game Over")
            if winner == True:
                print("Game is a tie")

        winner = champion(board, player_1, player_2, count)
        count += 1 
    if winner == False:
        print("Game Over")


def off_board(row, column):
    """
    Tells user if they select wrong range for the grid
    """
    print("Please pick another one")


def printing_board(board):
    rows = len(board)
    cols = len(board)
    print("---+---+---")
    for r in range(rows):
        print(board[r][0], " |", board[r][1], "|", board[r][2])
        print("---+---+---")
    return board

def champion(board, player_1, player_2, count):
    """
    Checks board to see if there is a winner
    """
    winner = True
    for row in range(0, 3):
        if (board[row][0] == board[row][1] == board[row][2] == player_1):
            winner = False
            print("Player" + player_1 + ", you are a winner!")
        elif (board[row][0] == board[row][1] == board[row][2] == player_2):
            winner = False
            print("Player" + player_2 + ", you are a winner!")

    for col in range(0, 3):
        if (board[col][0] == board[col][1] == board[col][2] == player_1):
            winner = False
            print("Player" + player_1 + ", you are a winner!")
        elif (board[col][0] == board[col][1] == board[col][2] == player_2):
            winner = False
            print("Player" + player_2 + ", you are a winner!")

    if board[0][0] == board[1][1] == board[2][2] == player_1:
        winner = False 
        print("Player " + player_1 + ", you won!")

    elif board[0][0] == board[1][1] == board[2][2] == player_2:
        winner = False
        print("Player " + player_2 + ", you won!")

    elif board[0][2] == board[1][1] == board[2][0] == player_1:
        winner = False
        print("Player " + player_1 + ", you won!")

    elif board[0][2] == board[1][1] == board[2][0] == player_2:
        winner = False
        print("Player " + player_2 + ", you won!")

    return winner