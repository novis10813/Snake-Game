from characters.character import BasicBlock
from pygame.sprite import Group
import pygame as pg


class BasicFood(BasicBlock):
    """Basic food object"""
    def __init__(self, game):
        super().__init__(game)
        self.load_sprite()
        self.rect.center = self.get_random_position()
    
    def load_sprite(self):
        self.image = pg.image.load("./assets/food.png").convert_alpha()
        self.rect = self.image.get_rect()


class Food:
    '''
    Use `Group` to create multiple food
    It should add `setting` here in the future for different modes
    '''
    def __init__(self, game, num=1):
        self.food_num = num
        self.group = Group()
        
        # initialize food according to number
        for _ in range(self.food_num): self.group.add(BasicFood(game))
    
    def render(self, display):
        self.group.draw(display)
    
    def update(self, delta_time, actions):
        self.group.update(delta_time, actions)