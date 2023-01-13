# Tic Tac Toe - Project 3 Python Essentials
If you are a true old school gamer, there is nothing more notstalgic than to go back to terminal games and having to type what you wanted to do into the terminal for and output to be produced. This Tic Tac Toe game does exactly that.

## Live Site 


## Repository
https://github.com/Kieran132/TicTacToe-project3

## Contents
- Project Goals
- Existing Features
    - Name Entry
    - Player Symbol Choice
    - PLayers Symbol Choices
    - Player One First Go
    - Row and Column Choice
    - Placement on Grid
    - Shows Winner
    - Shows Tie
    - Invalid Input
    - Already Selected
- Technologies Used
- Testing
- Deployment
- Credits

## Project Goals
The aim of this project was to showcase backend technology Python. I felt that creating something interactive and fun would be more engaging and also more user friendly for the user. This quick simple game of Tic Tac Toe, really hypes up the competitiveness of both users to the point where they want to keep playing until either has at leat won once.

## Existing Features
Throughout playing this terminal based games, it is a very simple step by step process. A selection had to be made before the game can progress and be playable.

#### Name Entry

<img src="assests/README.md photos/name_entry.png">

To make the game more personal and exciting having the users name on the system playing against another person. This input adds a sense of drive and determination to win at the game. Once the user inputs their name, this is used througout the game by telling the player it is their turn or if they win the game.

#### Player Symbol Choice

<img src="assests/README.md photos/player_1_symbol_choice.png">

Once name inputs have been entered, the terminal asks a player to choose between X or O. The user then enters X or O and the programme will continue

#### Both Player Symbol Choice

<img src="assests/README.md photos/shows_players_symbols.png">

Depending on what letter is selected initially, the game will then get the second users name and tell them which symbol they are. The to start the game, the user will hit enter

#### Player One First Go

<img src="assests/README.md photos/player_1_first_go.png">

Once enter has been hit, the terminal will tell a player it is their turn, then give them the option of selecting a row.

#### Row and Column Choice

<img src="assests/README.md photos/shows_column_row_choice.png">

The terminal will ask for both a row and column selection and details of where each selection is, is given in the question for the user.

#### Placement on the Grid

<img src="assests/README.md photos/shows_selection_on_grid.png">

Once a player has correctly inputted the correct range, the game will show their input as a placement on the grid with the symbol they have been assigned

#### Showing the Winner

<img src="assests/README.md photos/shows_winner.png">

If a player has managed to get a row of 3 of their symbol then the game will stop and a message will show tellng the players who is the winner

#### Showing a Tie

<img src="assests/README.md photos/shows_tie.png">

If the game come to the conclusion that neither player was able to get a row of three, then the game will finish the game and highlight the game is a tie and the game is over.

#### Invalid Input

<img src="assests/README.md photos/invalid-entry.png">

For a valid input the be entered, the user must enter the correct value. However, if the user chooses a number or character outside the parameters then an invalid message will show up to the user asking them to reselect within the correct range of values.

#### Already Selected Space

<img src="assests/README.md photos/already_selected.png">

Playing a game like this with multiple inputs, it can be difficult to rememeber which space the other player has selected. If a player chooses a space that has already been chosen, a message will appear telling them that and asking to choose another.

## Technologies Used
- Gitpod - used to create the website
- Github - used to store repository of website and deploy website
- Python - used to write the code for the game
- Heroku - used to deploy the game for users to play

## Testing

Click [Here](/TESTING.md) to see further information on testng and bugs

## Deployment

### Github Deployment
The website was delpoyed using GitHub. To do this I did the following;
1. When on the websites GitHub repository, click on the settings tab
2. Now on the settings page, on the left hand side of the page, click on the pages tab
3. Under the Source section, click on the drop down menu titled Branch and select main
4. The page is now published with a link available to use.

(https://github.com/Kieran132/TicTacToe-project3)

### Creating a Fork or Copying
To clone/fork/copy the repository you click on the fork tab which is situated next to unwatch tab in the top right corner of the page

### Clone
To create a clone you do the following;
1. Click on the code tab, left of the Gitpod tab
2. To the right of the repository name, click the clipboard icon
3. In the IED open GitBash
4. Change the working directory to the location you prefer
5. Add Git Clone with the copy of the repositroy name
6. Clone has been created

### Repositroy deployment via Heroku
- On the https://dashboard.heroku.com/apps page, click New and then select Create New App from the drop-down menu.
- When the next page loads insert the App name and Choose a region. The click Create app
- In the settings tab click on Reveal Config Vars and add the key Port and the value 8000. There were no credentials required for this app.
- Below this click Add buildpack and choose python and nodejs in that order.

#### Deployment of the app
- Click on the Deploy tab and select Github-Connect to Github.
- Enter the repository name and click Search.
- Choose the repository that holds the correct files and click Connect.
- A choice is offered between manual or automatic deployment whereby the app is updated when changes are pushed to GitHub.
- Once the deployment method has been chosen the app will be built and can be launched by clicking the Open app button at the top of the page.



## Credits

- https://gist.github.com/qianguigui1104/edb3b11b33c78e5894aad7908c773353 - Was used as a refernece point of understanding the outcome and writing python code

- https://medium.com/byte-tales/the-classic-tic-tac-toe-game-in-python-3-1427c68b8874 - used as a reference on writing and understanding python code

- https://inventwithpython.com/chapter10.html - used as a reference on writing and understanding python code

- Tutor support - Helped in re-writing the code to iron out errors that kept popping up

