# About this project:
 This is a snake game written with pygame.
 I try to do this project with a lot of OOP technics.

 Disclaim : The idea of the whole structure doesn't come up with by myself originally, but it is from this guy :
 https://github.com/ChristianD37/YoutubeTutorials/tree/master/Game%20States

## game.py:
The main program to run the "game window"
* It'll render the scene on the top of the "state_stack."
* Game with different menus is basically a stack.
* So it's easy to modularize different scene in game.

## characters:
The programs implement characters like snake and food in the game

### character.py:
The interface of everything in this game. It inherits from `pygame.sprite.Sprite` and it has two method:
1. load_sprite : load skin and initialize sprite.
2. get_random_position : initialize random position for the block.

### snake.py:
* NOT FINISHED YET!!!
There will be three kinds of classes in the future.
1. segment : It inherits from `BasicBlock`, which will decide the part of the snake.
2. special segment (not implement yet) : Will inherit from `segment`, for different game mode in the future.
3. Snake : Initialize group of segment, and it will control the behavior of those segments.
* So far it inherits from `BasicBlock` for direct use.
* Bugs : Turn around very quick will result in self eating.

### food.py:
There will be three kinds of classes in the future.
1. BasicFood : Inherit from `BasicBlock`. Just load the apple skin.
2. special food (not implement yet) : Will inherit from `BasicFood`, for different game mode in the future.
3. Food : Initialize group of food, you can decide how many apples are there in a game now.

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

### dead.py:
when die, the game will go into this state.

You can choose to restart the game or go back to menu.
