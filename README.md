# About this projext:
 This is a snake game written with pygame.
 I try to do this project with a lot of OOP technics.

## game.py:
The main program to run the "window"
* It'll render the scene on the top of the "state_stack."
* Game with different menus is basically a stack.
* So it's easy to modularize different scene in game.

## character.py:
The program implements character like snake and food in the game

### Contain 2 parts:
1. Snake
Inherented from `Item`, and implements how the snake works in game.
* Bugs: Turn around very quick will result in self eating.

2. Food
The food in game. It'll have more features in the future.



