from states.state import State

import pygame as pg

class Dead(State):
    def __init__(self, game):
        State.__init__(self, game)
        pg.display.set_caption("Dead")
    
    def update(self, delta_time, actions):
        if actions["pause"]:
            self.exit_state()
            self.exit_state()
        if actions["space"]:
            self.exit_state()
        self.game.reset_keys()
    
    def render(self, display):
        self.prev_state.render(display)
        self.game.draw_text(display, "You Died!", 40, (0,0,0), self.game.WINDOW_WIDTH/2, self.game.WINDOW_HEIGHT/2-40)
        self.game.draw_text(display, "Press P to Go Back to Menu", 20, (0,0,0), self.game.WINDOW_WIDTH/2, self.game.WINDOW_HEIGHT/2)
        self.game.draw_text(display, "Press Space to Restart", 20, (0,0,0), self.game.WINDOW_WIDTH/2, self.game.WINDOW_HEIGHT/2+40)