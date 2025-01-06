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

## Classes and Objects

### Board
The `Board` class handles the game logic and maintains the state of the game.

- **Attributes:**
  - `board_size`: Size of the board (integer).
  - `num_ships`: Number of ships to be placed on the board (integer).
  - `name`: Name of the board owner (string).
  - `type`: Type of board (string: "player" or "computer").
  - `guesses`: List of guesses made on the board (list of tuples).
  - `ships`: List of ship locations on the board (list of tuples).

- **Methods:**
  - `__init__(self, board_size, num_ships, name, board_type)`: Initializes the board with given parameters.
  - `display(self, hide_ships=False)`: Displays the current state of the board.
  - `process_guess(self, x, y)`: Processes a player's guess and updates the board.
  - `add_ship(self, x, y)`: Adds a ship at specified coordinates.

