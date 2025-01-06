# ULTIMATE Battleships
Battleships, also known simply as Battleship, is a classic two-player strategy game that blends deduction, tactics, and a touch of luck. Originating as a pencil-and-paper game during World War I, it has since evolved into a popular board game, digital adaptation, and mobile app enjoyed by players of all ages worldwide.

## Game Overview

In this Battleships, the player commands a fleet of ships strategically placed on a grid. The objective is to locate and "sink" the opponent’s fleet, in this case, the computer by guessing it's ships positions through a series of targeted strikes. The game involves strategic thinking as player must conceal his/her ships placement while trying to discover and destroy his/her opponent’s.

## Why should you play the battleship game?
Battleships is more than just a game-it's a test of strategy, anticipation, and patience. Its simplicity makes it accessible, while its depth keeps players coming back for more. Whether played on paper, a game board, or digitally, it remains an enduring favorite in family game nights and competitive play.

Are you ready to command your fleet and outmaneuver your opponent? Let the battle begin!

- [Introduction](#introduction)
- [Project](#project)
  - [Ultimate Battleships Game - User Goals](#Ultimate-Battleships-Game---User-Goals)
  - [Ultimate Battleships Game - Site Owner Goals](#Ultimate-Battleships-Game---Site-Owner-Goals)
- [Development](#development)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Resources](#resources)
  - [Libraries](#libraries)
- [Testing](#testing)
- [Future Updates](#future-updates)  
- [Validation](#validation)
- [Deployment](#deployment)
  - [Heroku](#heroku)
  - [Branching the GitHub Repository using GitHub Desktop and Visual Studio Code](#branching-the-github-repository-using-github-desktop-and-visual-studio-code)
- [Bugs](#bugs)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

## Introduction

Welcome to the Ultimate Battleships Game! This is a console-based implementation of the classic game of Battleship where a player competes against a computer opponent. The game involves placing ships on a grid and then taking turns to guess the location of each other's ships.

## Project 

## Ultimate Battleships Game - User Goals

### Entertainment and Engagement
- Enjoy a fun, strategic gameplay experience.
- Have an intuitive and seamless user interface.
- Experience a fair and balanced game.

### Competitive Play
- Challenge friends or random opponents the computr in this case.
- Improve skills through repeated play and strategizing.
- Track wins, losses, and rankings.

### Ease of Access
- Access the game easily on multiple platforms (desktop, mobile, or tablet).
- Play without needing extensive instructions or tutorials.

### Customization
- Personalize the game board, ships, and other visual elements.
- Select difficulty levels or specific rulesets.


## Ultimate Battleships Game - Site Owner Goals

### User Retention and Engagement
To ensure long-term user retention and engagement.

### Monetization
Monetizing the game effectively is essential for sustainability.

### Community Growth
Fostering a robust community will help drive traffic and promote user loyalty.

### Data Collection
Leveraging user data (with appropriate legal considerations) to improve the game experience.

### Brand Building
Building a strong brand is vital for attracting and retaining users.

### Scalability
Preparing for future growth is essential to accommodate more users.



## Development

Welcome to the Ultimate Battleships Game! This is a console-based implementation of the classic game of Battleship where a player competes against a computer opponent. The game involves placing ships on a grid and then taking turns to guess the location of each other's ships.

### Board Class

-   **Attributes:**

    -   `board_size`: Size of the board

    -   `num_ships`: Number of ships on the board

    -   `name`: Name of the player or "Computer"

    -   `type`: Type of board ("player" or "computer")

    -   `guesses`: List of tuples representing guessed coordinates

    -   `ships`: List of tuples representing ship coordinates

-   **Methods:**

    -   `__init__(self, board_size, num_ships, name, board_type)`: Initializes the board with the given size, number of ships, name, and type.

    -   `display(self, hide_ships=False)`: Displays the board. If `hide_ships` is True, ships are hidden.

    -   `process_guess(self, x, y)`: Processes a guess and returns whether it's a hit, miss, or repeat.

    -   `add_ship(self, x, y)`: Adds a ship to the board at the specified coordinates.

### Global Scores

-   **Dictionary:**

    -   `scores = {"computer": 0, "player": 0}`

Helper Functions
----------------

-   `random_point(board_size)`: Returns a random integer between 0 and `board_size - 1`.

-   `valid_coordinates(x, y, board)`: Checks if coordinates are valid and not already occupied.

-   `populate_board(board)`: Places ships randomly on the board.

-   `populate_board_player(board)`: Allows the player to manually place ships on the board.

-   `get_player_guess(board)`: Gets the player's guess input.

-   `get_computer_guess(board)`: Generates a random guess for the computer.

-   `take_turn(board, guess_func)`: Handles a single turn for either player or computer.

-   `play_game(computer_board, player_board)`: Alternates turns between player and computer until the game ends.

-   `new_game()`: Initializes and starts a new game.

Game Flow
---------

### Initialization

-   Input: Board size, number of ships, player name

-   Create `Board` instances for the computer and player

### Setup Phase

-   Player manually places ships

-   Computer places ships randomly

### Gameplay Phase

-   Alternate turns between player and computer

-   Handle guesses and process hits/misses

-   Update scores

-   Display updated boards and summary

### Endgame

-   Declare the winner based on remaining ships

-   Display final scores

Relationships
-------------

-   `new_game()` creates `Board` objects and calls `populate_board` or `populate_board_player`.

-   `play_game()` uses helper functions like `get_player_guess`, `get_computer_guess`, and `take_turn`.

## Features

1. Manual placement of ships by player.
   
![manual placement](assets/images/ship_placement.png)

2. Random board generation for computer and player cannot see where the computer's ships are.
   
![Random board](assets/images/random_board.png)

3. Accepts user inputs and gives saummary of scores after each round
   
![Round score](assets/images/round_score.png)

4. Input validation for 
- Numbers out of board's range
- Check whether inputs are numbers
- Checks whether the same coordinates are given more than once
  
![Input validation](assets/images/input_validation.png)



