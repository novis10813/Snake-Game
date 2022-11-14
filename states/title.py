from states.state import State
from states.play import Play
# from game import Game

import pygame as pg

class Title(State):
    def __init__(self, game):
        State.__init__(self, game)
        pg.display.set_caption("Snake Game - Menu")
    
    def update(self, delta_time, actions):
        if actions["space"]:
            new_state = Play(self.game)
            new_state.enter_state()
        self.game.reset_keys()
    
    def render(self, display:pg.Surface):
        display.fill((163, 219, 232))
        self.game.draw_text(display, "Snake Game", 40, (0,0,0), self.game.WINDOW_WIDTH/2, self.game.WINDOW_HEIGHT/4)
        self.game.draw_text(display, "Press Space to Start", 20, (0,0,0), self.game.WINDOW_WIDTH/2, self.game.WINDOW_HEIGHT/2)
        self.game.draw_text(display, "Press ESC to Leave", 20, (0,0,0), self.game.WINDOW_WIDTH/2, self.game.WINDOW_HEIGHT/2-30)