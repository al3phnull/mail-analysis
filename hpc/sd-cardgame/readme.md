# Software Development Code Improvement

The `doc/` directory contains all the relevant documentation to the project.

The `code/` directory contains all of the necessary files to build and run the game.
To execute the code base, you must be inside the `code/` directory
- In order to play a game, first `cd code/` then run `./play_dbc.py`.

- To run the test suite for the code, run `/run_tests.sh`

- The main code may be viewed by looking at `code/dbc/` 
This directory is build as a package, and it consists of several encapsulated classes that work together to
run the game.
`card.py` Returns card parameters
`pile.py` Manages card pile attributes and methods
`player.py` Sets up and declares functions for the player
`bot.py` Inherits from the Player class
`data.py` Provides input to the game
`game.py` Provides the core functionality of the game
`main.py` Initialises and runs the game

- A subdirectory `code/dbc/tests/` contains the unit test suite for the code.

- The json resources are located in `code/res/`
`strings.json` contains all the text assets used in game.
`cards.json` is used to load cards into the game as dictionaries.

The `old/` directory includes the original code and the
codebase used for refactoring the code.

- Required packages: json, random, sys, os, time


## Game setup
- The game is played by two players, the __player__ and the __computer__.
- Both players start with 30 health
- Each player is assigned four relevant card piles:
 - The __deck__ which consists of ten cards: 8 Serfs, 2 Squires
 - The __discard__ pile which starts empty
 - The __active__ hand which starts empty
 - The __hand__ which starts off empty
- The central board lies between the two players:
 - The __central deck__ consists of 36 varied cards
 - The central __active area__ which starts empty
 - A __supplement__ pile that lies alongside the __central__ deck. Supplements are identical to regular cards from the pile, and they provide additional medium-attack powered cards when a stronger one cannot be afforded from the __central deck__.

