from states.state import State
from states.pause import Pause
from character import Snake, Food
import pygame as pg

class Play(State):
    def __init__(self, game):
        State.__init__(self, game)
        pg.display.set_caption("Snake Game - Play")
        self.new_game()
        # add pic for background
        self.bg = pg.image.load("./assets/background.png").convert_alpha()
    
    def update(self, delta_time, actions):
        
        # move snake and update food
        self.snake.update(delta_time, actions)
        for food in self.foods:
            food.update(delta_time, actions)
        
        if actions["pause"] and not self.game.pausing:
            self.game.pausing = True
            new_state = Pause(self.game)
            new_state.enter_state()
        self.game.reset_keys()
      
    def render(self, display):
        display.blit(self.bg, (0,0))
        self.snake.render(display)
        for food in self.foods:
            food.render(display)
        self.game.draw_text(display, "Your Score: "+str(self.snake.length-1), 20, (0,0,0), 20, 15)
    
    def new_game(self):
        self.snake = Snake(self.game)
        self.foods = []
        for _ in range(5):
            food = Food(self.game)
            self.foods.append(food)