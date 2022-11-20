from random import randrange
import pygame as pg

class BasicBlock(pg.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.size = self.game.TILE_SIZE
        self.load_sprite()
        self.rect.center = self.get_random_position()
    
    # def update(self, delta_time, actions):
    #     pass
    
    # def render(self, display):
    #     pass
    
    # temporary for the block snake and block food
    def load_sprite(self):
        self.rect = pg.rect.Rect([0, 0, self.size - 2, self.size - 2])
    
    def get_random_position(self):
        return [randrange(self.size // 2, self.game.WINDOW_WIDTH - self.size // 2, self.size),
                randrange(self.size // 2, self.game.WINDOW_HEIGHT - self.size // 2, self.size)]