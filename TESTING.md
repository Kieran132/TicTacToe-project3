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
