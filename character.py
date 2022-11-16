from random import randrange
from pygame.math import Vector2
import pygame as pg

class item:
    def __init__(self, game):
        self.game = game
        self.size = self.game.TILE_SIZE
        self.load_sprite()
        self.rect.center = self.get_random_position()
    
    def update(self, delta_time, actions):
        pass
    
    def render(self, display):
        pass
    
    # temporary for the block snake and block food
    def load_sprite(self):
        self.rect = pg.rect.Rect([0, 0, self.size - 2, self.size - 2])
    
    def get_random_position(self):
        return [randrange(self.size // 2, self.game.WINDOW_HEIGHT - self.size // 2, self.size),
                randrange(self.size // 2, self.game.WINDOW_HEIGHT - self.size // 2, self.size)]

class Snake(pg.sprite.Sprite, item):
    def __init__(self, game):
        self.game = game
        self.size = self.game.TILE_SIZE
        self.load_sprite()
        self.rect.center = self.get_random_position()
        self.direction = Vector2(0, 0)
        self.length = 1
        self.segments = []
        self.delay = 100 # smaller the delay, faster the snake
        self.time = 0
        self.directions = {"right":1, "left":1, "up":1, "down":1}
    
    def control(self, actions):
        if actions["right"] and self.directions["right"]:
            self.direction = Vector2(self.size, 0)
            self.directions = {"right":1, "left":0, "up":1, "down":1}
        if actions["left"] and self.directions["left"]:
            self.direction = Vector2(-self.size, 0)
            self.directions = {"right":0, "left":1, "up":1, "down":1}
        if actions["up"] and self.directions["up"]:
            self.direction = Vector2(0, -self.size)
            self.directions = {"right":1, "left":1, "up":1, "down":0}
        if actions["down"] and self.directions["down"]:
            self.direction = Vector2(0, self.size)
            self.directions = {"right":1, "left":1, "up":0, "down":1}
    
    def load_sprite(self):
        self.head = pg.image.load("./assets/snake/SnakeHead.png").convert_alpha()
        self.body_s = pg.image.load("./assets/snake/SnakeBody_straight.png").convert_alpha()
        self.body_b = pg.image.load("./assets/snake/SnakeBody_bend.png").convert_alpha()
        self.tail = pg.image.load("./assets/snake/SnakeTail.png").convert_alpha()
        
        directions = {
            "head_up": self.head,
            "head_down": pg.transform.rotate(self.head, 180),
            "head_right": pg.transform.rotate(self.head, 90),
            "head_left": pg.transform.rotate(self.head, -90),
            "body_up": self.body_s,
            "body_down": pg.transform.rotate(self.body_s, 180),
            "body_right": pg.transform.rotate(self.body_s, 90),
            "body_left": pg.transform.rotate(self.body_s, -90),
            "body_RD": self.body_b,
            "body_UR": pg.transform.rotate(self.body_b, -90),
            "body_LU": pg.transform.rotate(self.body_b, 180),
            "body_DL": pg.transform.rotate(self.body_b, 90),
            "body_LD": pg.transform.flip(self.head, flip_y=True),
            "body_UL": pg.transform.rotate(pg.transform.flip(self.head, flip_y=True), 90),
            "body_RU": pg.transform.rotate(pg.transform.flip(self.head, flip_y=True), 180),
            "body_DR": pg.transform.rotate(pg.transform.flip(self.head, flip_y=True), -90),
            "tail_up": self.tail,
            "tail_down": pg.transform.rotate(self.tail, 180),
            "tail_right": pg.transform.rotate(self.tail, 90),
            "tail_left": pg.transform.rotate(self.tail, -90),
        }
    
    def check_borders(self):
        if self.rect.left < 0 or self.rect.right > self.game.WINDOW_WIDTH:
            self.game.state_stack[-1].new_game()
        if self.rect.top < 0 or self.rect.bottom > self.game.WINDOW_HEIGHT:
            self.game.state_stack[-1].new_game()
    
    def check_food(self):
        for food in self.game.state_stack[-1].foods:
            if self.rect.colliderect(food.rect):
                # self.game.state_stack[-1].food.rect.center = self.game.state_stack[-1].food.get_random_position()
                food.rect.center = food.get_random_position()
                self.length += 1
    
    def check_food_overlap(self):
        for food in self.game.state_stack[-1].foods:
            if food.rect.collidelist(self.segments) != -1:
                food.rect.center = food.get_random_position()
    
    def check_selfeating(self):
        if len(self.segments) != len(set(segment.center for segment in self.segments)):
            self.game.state_stack[-1].new_game()
    
    def move(self):
        if self.game.prev_time - self.time > self.delay:
            self.time = self.game.prev_time
            self.rect.move_ip(self.direction)
            self.segments.append(self.rect.copy())
            self.segments = self.segments[-self.length:]
    
    def update(self, delta_time, actions):
        self.control(actions)
        self.move()
        
        # TODO: Move these method under `play.py`
        self.check_selfeating()
        self.check_borders()
        self.check_food()
        self.check_food_overlap()
    
    def render(self, display):
        [pg.draw.rect(display, 'blue', segment) for segment in self.segments]

class Food(item):
    def __init__(self, game):
        super().__init__(game)
        
    def render(self, display):
        display.blit(self.food_img, self.rect)
    
    def load_sprite(self):
        self.food_img = pg.image.load("./assets/food.png").convert_alpha()
        # width = self.food_img.get_width()
        # height = self.food_img.get_height()
        # self.food_img = pg.transform.scale(self.food_img, (int(width*1.2), int(height*1.2)))
        self.rect = self.food_img.get_rect()
    
    # def check_food_overlap(self):