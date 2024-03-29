def main():
    """
    Functions needed to run the game
    """
    name_1, name_2 = intro()
    board = create_board()
    printing_board(board)
    player_1, player_2 = player_sym(name_1, name_2)
    board_check(board, player_1, player_2, name_1, name_2)


def intro():
    """
    Function to give a message for the player and outline rules
    """
    print("Ready to play Tic Tac Toe?!")
    print("First to get 3 in a row wins!")
    while True:
        name_1 = input("Player 1, Enter your name: ")
        if not is_valid_input(name_1):
            print("Invalid input. Please enter only letters and numbers.")
            continue
        else:
            break
    while True:
        name_2 = input("Player 2, Enter your name: ")
        if not is_valid_input(name_2):
            print("Invalid input. Please enter only letters and numbers.")
            continue
        else:
            return name_1, name_2


def is_valid_input(input_str):
    """
    Function to check if the input string contains only letters and numbers
    """
    valid_chars = set(
            'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    for char in input_str:
        if char not in valid_chars:
            return False
    return True


def create_board():
    """
    Function to create layout of a blank board
    """
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    return board


def player_sym(name_1, name_2):
    """
    Function that allows the players to choose which symbol they want
    """
    while True:
        player_1 = input(name_1 + ", please choose your symbol, X or O? ")
        player_1 = player_1.strip().upper()
        if player_1 == 'X' or player_1 == 'O':
            break
        else:
            print("Invalid symbol. Please choose either X or O.")
    player_2 = 'O' if player_1 == 'X' else 'X'
    print(name_2 + ", you are", player_2)
    input("Press Enter to play!")
    return (player_1, player_2)


def start(board, player_1, player_2, count, name_1, name_2):
    """
    Function to start the game
    """
    if count % 2 == 1:
        player = name_2
    elif count % 2 == 0:
        player = name_1
    print(player + ", it is your turn.")
    row = int(get_row())
    column = int(get_col())
    while ((row) > 2 or (row) < 0) or ((column) > 2 or (column) < 0):
        row = get_row()
        column = get_col()
    while (board[row][column] == player_1) or (board[row][column] == player_2):
        wrong(board, player_1, player_2, row, column)
        row = int(get_row())
        column = int(get_col())
    if player == name_1:
        board[row][column] = player_1
    else:
        board[row][column] = player_2
    return (board)


def get_row():
    """
    Validates the input for row selection is within the right limit
    """
    while True:
        row = input(
            'enter row number: Top: 0, Middle: 1, Bottom: 2: ')
        try:
            if int(row.strip()) not in [0, 1, 2, ]:
                print("Invalid input, Enter number between 0 and 2")
                continue
            else:
                return row
        except ValueError:
            print("Please choose a number")
            continue


def get_col():
    """
    Validates the input for column selection is within the right limit
    """
    while True:
        column = input(
            'enter column number: Left: 0, Middle: 1, Right: 2: ')
        try:
            if int(column.strip()) not in [0, 1, 2, ]:
                print("Invalid input, Enter number between 0 and 2")
                continue
            else:
                return column
        except ValueError:
            print("Please choose a number")
            continue


def board_check(board, player_1, player_2, name_1, name_2):
    """
    Checks to see if the board is full
    """
    count = 1
    winner = True
    while count < 10 and winner is True:
        start(board, player_1, player_2, count, name_1, name_2)
        printing_board(board)
        if count == 9:
            print("Game Over")
            if winner is True:
                print("Game is a tie")
        winner = champion(board, player_1, player_2, count, name_1, name_2)
        count += 1
    if winner is False:
        print("Game Over")


def printing_board(board):
    """
    Prints the board to the terminal in a better visual way
    """
    rows = len(board)
    print("---+---+---")
    for r in range(rows):
        print(board[r][0], " |", board[r][1], "|", board[r][2])
        print("---+---+---")
    return board


def champion(board, player_1, player_2, count, name_1, name_2):
    """
    Checks board to see if there is a winner
    """
    winner = True
# Horizontal Winning Conditions
    for row in range(0, 3):
        if (board[row][0] == board[row][1] == board[row][2] == player_1):
            winner = False
            print(name_1 + ", you won!")
        elif (board[row][0] == board[row][1] == board[row][2] == player_2):
            winner = False
            print(name_2 + ", you won!")
# Vertial Winning Conditions
    for col in range(0, 3):
        if (board[0][col] == board[1][col] == board[2][col] == player_1):
            winner = False
            print(name_1 + ", you won!")
        elif (board[0][col] == board[1][col] == board[2][col] == player_2):
            winner = False
            print(name_2 + ", you won!")
# Diagonal Winning Conditions
    if board[0][0] == board[1][1] == board[2][2] == player_1:
        winner = False
        print(name_1 + ", you won!")
    elif board[0][0] == board[1][1] == board[2][2] == player_2:
        winner = False
        print(name_2 + ", you won!")
    elif board[0][2] == board[1][1] == board[2][0] == player_1:
        winner = False
        print(name_1 + ", you won!")
    elif board[0][2] == board[1][1] == board[2][0] == player_2:
        winner = False
        print(name_2 + ", you won!")
    return winner


def wrong(board, player_1, player_2, row, column):
    """
    Function that tells user a place has already been selected
    """
    print("Already selected, please choose another.")


main()
