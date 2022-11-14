# About this project:
 This is a snake game written with pygame.
 I try to do this project with a lot of OOP technics.
 Disclaim : These ideas are not come from myself, but from this guy :
 https://github.com/ChristianD37/YoutubeTutorials/tree/master/Game%20States

## game.py:
The main program to run the "game window"
* It'll render the scene on the top of the "state_stack."
* Game with different menus is basically a stack.
* So it's easy to modularize different scene in game.

## character.py:
The program implements character like snake and food in the game

### Contain 2 parts:
1. Snake
Inherented from `Item`, and implements how the snake works in game.
* Bugs : Turn around very quick will result in self eating.

2. Food
The food in game. It'll have more features in the future.

## utilities:
A folder with tools that might help
### button.py
I thought I would use buttons in this game, and I'm wrong.
It can load a image as a button. Maybe I can add more features, like it'll sprinkle when hover or it can use rect with text as a button, but not now.

## states:
This is where magic happens, every single scene in game is done in here

### state.py:
An interface for other states. `update` and `render` method should be implement in the subclass of state.
* enter_state : append new state to state_stack in `game.py`
* exit_state : pop state to state_stack in `game.py`

### title.py:
Title scene, the game will enter this state immediately when the game is initialized.
I'll add setting menu for more features in the future.

### play.py:
It comes after title scene, initialized when start to play the game.
It will load settings and game mode from setting menu in the future.

### pause.py:
"Press P to Pause"