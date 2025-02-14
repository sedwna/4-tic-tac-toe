# Tic-Tac-Py

Welcome to **Tic-Tac-Py**, a Python-based implementation of the classic Tic-Tac-Toe game with a twist! This project allows you to play Tic-Tac-Toe in two modes:
1. **Player vs. Player**: Play against a friend.
2. **Player vs. Computer**: Play against an AI opponent.

The game is designed to run in the terminal and features colorful visuals using the `termcolor` library.

---

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [How to Run](#how-to-run)
- [Gameplay](#gameplay)
- [Code Structure](#code-structure)
- [Dependencies](#dependencies)

---

## Introduction

**4-Tic-Tac-Toe** is a Python implementation of the classic Tic-Tac-Toe game. The game is played on a 3x3 grid, and players take turns marking a space with their symbol (`X` or `O`). The goal is to be the first to get three of your symbols in a row (horizontally, vertically, or diagonally).

This project includes two modes:
1. **Player vs. Player**: Two players can play against each other.
2. **Player vs. Computer**: Play against a simple AI opponent.

The game is designed to be simple, fun, and easy to play in the terminal.

---

## Features

- **Two Game Modes**:
  - **Player vs. Player**: Play against a friend.
  - **Player vs. Computer**: Play against an AI opponent.
- **Colorful Visuals**: Uses the `termcolor` library to add color to the game board and messages.
- **Simple Controls**: Easy-to-understand input system for selecting moves.
- **Winning Logic**: Automatically checks for a winner or a draw.
- **Cross-Platform**: Works on any system with Python installed.

---

## How to Run

### Prerequisites
- **Python 3.x**: Ensure Python is installed on your system.
- **`termcolor` Library**: Install the `termcolor` library for colored output.

### Steps to Run
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/sedwna/4-tic-tac-toe.git
   ```

2. **Install Dependencies**:
   Install the `termcolor` library using pip:
   ```bash
   pip install termcolor
   ```

3. **Run the Game**:
   Run the Python script to start the game:
   ```bash
   python 4-tic-tak-toe.py
   ```

4. **Follow the Instructions**:
   - Choose a game mode:
     - `1`: Play against a friend.
     - `2`: Play against the computer.
     - `3`: Exit the game.
   - Follow the on-screen instructions to make your moves.

---

## Gameplay

### Player vs. Player Mode
1. Player 1 is `X`, and Player 2 is `O`.
2. Players take turns entering a number (1-9) corresponding to the grid position they want to mark.
3. The first player to get three of their symbols in a row wins.
4. If all spaces are filled without a winner, the game ends in a draw.

### Player vs. Computer Mode
1. The player is `X`, and the computer is `O`.
2. The player enters a number (1-9) to mark their position.
3. The computer automatically makes its move after a short delay.
4. The first to get three in a row wins, or the game ends in a draw.

---

## Code Structure

The project is organized into the following functions:

- **`check_board(plyr)`**: Checks if the current player has won.
- **`plyer_move(num, shape)`**: Handles the player's move and checks for a win.
- **`computer_move()`**: Implements the AI logic for the computer's move.
- **`print_board()`**: Displays the current state of the game board.
- **`start_AI()`**: Starts the game in Player vs. Computer mode.
- **`start_duel()`**: Starts the game in Player vs. Player mode.
- **`menu()`**: Displays the main menu and handles user input.

---

## Dependencies

- **Python 3.x**: The game is written in Python and requires Python 3.x to run.
- **`termcolor` Library**: Used for adding colored output to the terminal.
  - Install using `pip install termcolor`.

---

### Main Menu
```
choose what do you want to do?  
1.Start with friend
2.Start with computer
3.exit
--enter a number --> 
```

### Game Board
```
[1][2][3]

[4][5][6]

[7][8][9]
```

### Player vs. Computer
```
Player : X 
Computer : O
3 second to start...
```

### Winning Message
```
Player(1) WIN
```

---

Enjoy playing **4-Tic-Tac-Toe**! If you have any questions or feedback, feel free to open an issue or contribute to the project.

---

