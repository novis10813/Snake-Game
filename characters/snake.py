from characters.character import BasicBlock
from pygame.math import Vector2
import pygame as pg

class segment(BasicBlock):
    images = None
    def __init__(self, game, is_head=False):
        super().__init__(game)
        
        self.is_head = is_head
        self.is_tail = False
        self.direction = "w"
    
    def load_sprite(self):
        if self.is_head: self.image = segment.images["head_w"]
        
class Snake(BasicBlock):
    def __init__(self, game): # grp, pos, length, parent=None
        super().__init__(game)
        
        # different snake block for different part
        # self.parent = parent
        # self.child = None
        # self.direction = "up"
        
        # deal with snake skin
        # no parent, which means it's parent (snake head)
        # if not self.parent: self.image = Snake.images["head_up"]
        # only head and tail
        # elif length == 1: self.image = Snake.images["tail_up"]
        # else: self.image = Snake.images["body_up"]
        
        # self.rect = self.image.get_rect(x=pos[0]*self.size, y=pos[1]*self.size)
        # self.child = Snake(grp, (pos[0], pos[1]+1), length-1, self)
        self.images = self.load_snake_img()
        self.direction = "w"
        # self.load_sprite()
        self.image = self.images["head_w"]
        self.rect = self.image.get_rect()
        self.rect.center = self.get_random_position()
        self.movement = Vector2(0, 0)
        self.length = 1
        self.segments = []
        
        ## Movement configuration
        # smaller the delay, faster the snake
        self.delay = 200
        self.time = 0
        self.movements = {"right":1, "left":1, "up":1, "down":1}
    
    def control(self, actions):
        if actions["right"] and self.movements["right"]:
            self.movement = Vector2(self.size, 0)
            self.movements = {"right":1, "left":0, "up":1, "down":1}
            self.image = self.images["head_w"]
            
        if actions["left"] and self.movements["left"]:
            self.movement = Vector2(-self.size, 0)
            self.movements = {"right":0, "left":1, "up":1, "down":1}
            self.image = self.images["head_e"]
            
        if actions["up"] and self.movements["up"]:
            self.movement = Vector2(0, -self.size)
            self.movements = {"right":1, "left":1, "up":1, "down":0}
            self.image = self.images["head_n"]
            
        if actions["down"] and self.movements["down"]:
            self.movement = Vector2(0, self.size)
            self.movements = {"right":1, "left":1, "up":0, "down":1}
            self.image = self.images["head_s"]
    
    def move(self):
        if self.game.prev_time - self.time > self.delay:
            self.time = self.game.prev_time
            self.rect.move_ip(self.movement)
            self.segments.append(self.rect.copy())
            self.segments = self.segments[-self.length:]
    
    def update(self, delta_time, actions):
        self.control(actions)
        self.move()
    
    def render(self, display):
        for segment in self.segments:
            display.blit(self.image, segment)
        # [pg.draw.rect(display, 'blue', segment) for segment in self.segments]

    def load_snake_img(self):
        head = pg.image.load("./assets/snake/head.png").convert_alpha()
        body_s = pg.image.load("./assets/snake/straight.png").convert_alpha()
        body_b = pg.image.load("./assets/snake/bend.png").convert_alpha()
        tail = pg.image.load("./assets/snake/tail.png").convert_alpha()
        
        return {
            "head_n": head,
            "head_s": pg.transform.rotate(head, 180),
            "head_e": pg.transform.rotate(head, 90),
            "head_w": pg.transform.rotate(head, -90),
            "body_nn": body_s,
            "body_ss": pg.transform.rotate(body_s, 180),
            "body_ee": pg.transform.rotate(body_s, 90),
            "body_ww": pg.transform.rotate(body_s, -90),
            "body_se": body_b,
            "body_en": pg.transform.rotate(body_b, -90),
            "body_nw": pg.transform.rotate(body_b, 180),
            "body_ws": pg.transform.rotate(body_b, 90),
            "body_sw": pg.transform.flip(body_b, flip_x=True, flip_y=False),
            "body_wn": pg.transform.rotate(pg.transform.flip(body_b, flip_x=True, flip_y=False), 90),
            "body_ne": pg.transform.rotate(pg.transform.flip(body_b, flip_x=True, flip_y=False), 180),
            "body_es": pg.transform.rotate(pg.transform.flip(body_b, flip_x=True, flip_y=False), -90),
            "tail_n": tail,
            "tail_s": pg.transform.rotate(tail, 180),
            "tail_e": pg.transform.rotate(tail, 90),
            "tail_w": pg.transform.rotate(tail, -90),
        }