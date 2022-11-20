from states.state import State
from states.pause import Pause
from states.dead import Dead
from characters.food import Food
from characters.snake import Snake
import pygame as pg
import itertools

class Play(State):
    def __init__(self, game):
        State.__init__(self, game)
        pg.display.set_caption("Snake Game - Play")
        # load images
        self.bg = pg.image.load("./assets/background.png").convert()
        self.new_game()
    
    def update(self, delta_time, actions):
        
        # move snake and update food
        self.snake.update(delta_time, actions)
        self.foods.update(delta_time, actions)
        
        # check situations
        self.check_selfeating()
        self.check_borders()
        self.check_food_eaten()
        self.check_food_overlap()
        
        if actions["pause"] and not self.game.pausing:
            self.game.pausing = True
            new_state = Pause(self.game)
            new_state.enter_state()
        self.game.reset_keys()
      
    def render(self, display):
        display.blit(self.bg, (0,0))
        self.snake.render(display)
        self.foods.render(display)
        self.game.draw_text(display, "Your Score: "+str(self.snake.length-1), 20, (0,0,0), 20, 15)
    
    def new_game(self):
        self.snake = Snake(self.game)
        self.foods = Food(self.game, 5)
    
    def check_borders(self):
        if self.snake.rect.left < 0 or self.snake.rect.right > self.game.WINDOW_WIDTH or \
           self.snake.rect.top < 0 or self.snake.rect.bottom > self.game.WINDOW_HEIGHT: 
            self.enter_dead()
            self.new_game()
    
    def check_selfeating(self):
        if len(self.snake.segments) != len(set(segment.center for segment in self.snake.segments)):
            self.enter_dead()
            self.new_game()
    
    def check_food_overlap(self):
        # check overlap between food and snake after eating
        for food in self.foods.group.sprites():
            if food.rect.collidelist(self.snake.segments) != -1:
                food.rect.center = food.get_random_position()
                self.check_food_overlap()
        
        #check overlap between foods
        for i, j in itertools.combinations(self.foods.group.sprites(), 2):
            if i.rect.colliderect(j.rect):
                j.rect.center = j.get_random_position()
                self.check_food_overlap()
    
    def check_food_eaten(self):
        for food in self.foods.group.sprites():
            if self.snake.rect.colliderect(food.rect):
                food.rect.center = food.get_random_position()
                self.snake.length += 1

    def enter_dead(self):
        new_state = Dead(self.game)
        new_state.enter_state()
    