# Python Terminal Jetpack Joyride

## Introduction

This is the terminal version of Jetpack Joyride written in Python. It uses the basic Python libraries and modules.

This game has been tested on **Linux** based Operating Systems.

## Structure and Features

The game application exhibits the OOP concepts of Inheritance, Encapsulation, Polymorphism, Abstraction along with Function Overloading.

## About the Game

### Controls

* w - Up
* a - Left
* d - Right
* b - Fire Bullets
* Spacebar - Activating Shield
* k - Activating Speed Boost
* q - Quit

### Features and Powerups

1. Shield: The player can activate a shield around using the Spacebar key. The shield prevents the player from losing lives on collision with obstacles or bullets from Enemy. The shield can only be activated for 10 seconds in every 60 seconds.

2. Magnet: A randomly placed magnet appears in front of the player and tries to pull the player towards itself. On contact with the magnet lives are lost in accordance to the extent of the touch

3. Speedboost: A randomly placed speedboost appears in front of the player and on taking the powerup, the speed of the player increases for 10 seconds in every 60 seconds.

4. Bullets: An unlimited set of bullets which when fired can kill the ultimate boss enemy and destroy obstacles on the way.

5. Boss Enemy: A moving powerful dragon fires bullets every 5 seconds and killing him will allow one to win the game.

### Notes
- Every stationary item and moving item is derived from the Object class and Person class respectively.
- The objects uses polymorphism to redefine their attributes and methods in the parent class.
- Gravitational simulation is used to model the movement of the player
- The Game Screen has its own class, Board, which generates the game map and can built objects and players onto the screen.
- The game has a pre-generated level map which is rendered during the run time and is updated according to Mando's position in the game.

## Running the program

1. Install all the requirements:
    - `pip3 install -r requirements.txt`
2. Run the program:
    - `python3 play_game.py`

## Project Tree

* board.py
* config.py
* object.py
* person.py
* play_game.py
* __pycache__
    * alarmexception.cpython-37.pyc
    * board.cpython-37.pyc
    * config.cpython-37.pyc
    * input.cpython-37.pyc
    * object.cpython-37.pyc
    * person.cpython-37.pyc
* README.md
* requirements.txt
