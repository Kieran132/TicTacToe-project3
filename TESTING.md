# Testing

## Code Institute Python Linter

No issues

<img src="assests/README.md photos/python_verification.png">

## Bugs

Throughout the creation of this temrinal based game, there were a few bugs that came about that needed to be addressed:

#### Input Validation
On my orignal game, the user was able to input any character or number and this brought up an error on the terminal. 

In order to solve this probem, I created two new functions that both had while loops to check the users input was in the correct range I had set. If this was true then the loop would end. If the input was out of the range I had set, then a message will appear on the terminal telling the user how to correct the mistake.

#### TypeError

When implementing the new functions into the start function I put together to run the came a TypeError appeared:
 while ((row) > 2 or (row) < 0) or ((column) > 2 or (column) < 0):
TypeError: '>' not supported between instances of 'str' and 'int'

The way around solving this probelm was to add int() and insert the functions name within. This converts the specified value into an integer.

#### Double selection of already selected space

Once a player selects an already selected position, the programme throws an error message. However, if the same combination is chosen again, a TypeError message was presented to the terminal:

  File "run.py", line 61, in start
    while (board[row][column] == player_1) or (board[row][column] == player_2):
TypeError: list indices must be integers or slices, not str

To solve this issue in both get_row and get_column function I changed it to:

int(input(
            'enter row number: Top: 0, Middle: 1, Bottom: 2: '))
        if row not in [0, 1, 2]:

int(input(
            'enter column number: Left: 0, Middle: 1, Right: 2: '))
        if column not in [0, 1, 2]:
