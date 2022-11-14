from states.state import State

import pygame as pg

class Pause(State):
    def __init__(self, game):
        self.game = game
        State.__init__(self,game)
        # pg.display.set_caption("Snake Game - Paused")
        
    def update(self, delta_time, actions):
        if actions["pause"] and self.game.pausing:
            self.game.pausing = False
            self.exit_state()
        self.game.reset_keys()
    
    def render(self, display):
        self.prev_state.render(display)
        self.game.draw_text(display, "Paused", 40, (0,0,0), self.game.WINDOW_WIDTH/2, self.game.WINDOW_HEIGHT/2-40)
        self.game.draw_text(display, "Press P to Continue", 35, (0,0,0), self.game.WINDOW_WIDTH/2, self.game.WINDOW_HEIGHT/2)
    
    # def transition_state(self):
        