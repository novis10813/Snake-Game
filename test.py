import pygame
import math
from random import randint
from sys import exit

pygame.init()
clock = pygame.time.Clock()
disp_surface = pygame.display.set_mode(size = (610, 700))

class Snake(pygame.sprite.Sprite):
    def __init__(self, x_pos = 300, y_pos = 300):
        #Access the super class of Sprite
        super().__init__()
        #self.image = pygame.image.load("square1.png").convert_alpha()
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (0, 255, 0), (10, 10), 10)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(x = x_pos, y = y_pos)
    def update(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center = (x_pos, y_pos))

class Food(pygame.sprite.Sprite):
    """class to control food action"""
    def __init__(self):
        super().__init__() #access the Sprite super class methods
        #self.image = pygame.image.load("food1.png").convert_alpha()
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 0, 0), (10, 10), 10)
        x_pos = randint(50,600)
        y_pos = randint(50,650)
        self.rect = self.image.get_rect(x = x_pos,y = y_pos)
    def update(self, pos):
        x_pos = randint(50,600)
        y_pos = randint(50,650)
        self.rect = self.image.get_rect(x = x_pos,y = y_pos)


def update_body(track, distance):
    body = snakegroup.sprites()
    no_parts = len(body)
    body[0].update(*track[0])
    track_i = 1
    next_i = 1
    for i in range(1, no_parts):
        while track_i < len(track):
            pos = track[track_i]
            track_i += 1
            dx, dy = body[i-1].x_pos-pos[0], body[i-1].y_pos-pos[1]
            if math.sqrt(dx*dx + dy*dy) >= distance:
                body[i].update(*pos)
                next_i = i+1
                break
    while next_i < no_parts:
        body[next_i].update(*track[-1])
        next_i += 1
    del track[track_i:]
    return body

snakegroup = pygame.sprite.Group()
original_snake = Snake()
snakegroup.add(original_snake)
track = [(original_snake.x_pos, original_snake.y_pos)]

foods = pygame.sprite.GroupSingle()
foods.add(Food())

direction = (0, 0)
speed = 1
run = True
while run:
    for eachevent in pygame.event.get():
        if eachevent.type == pygame.QUIT:
            run = False
        if eachevent.type == pygame.KEYDOWN:
            if eachevent.key == pygame.K_LEFT and direction[0] != 1:
                direction = (-1, 0)
            if eachevent.key == pygame.K_RIGHT and direction[0] != -1:
                direction = (1, 0)
            if eachevent.key == pygame.K_UP and direction[1] != 1:
                direction = (0, -1)
            if eachevent.key == pygame.K_DOWN and direction[1] != -1:
                direction = (0, 1)

    track.insert(0, track[0])
    track[0] = (track[0][0] + direction[0] * speed) % disp_surface.get_width(), (track[0][1] + direction[1] * speed) % disp_surface.get_height()
    update_body(track, 20)

    if pygame.sprite.spritecollideany(foods.sprite, snakegroup):
        foods.empty()
        foods.add(Food())
        last_part = snakegroup.sprites()[-1]
        snakegroup.add(Snake(last_part.x_pos, last_part.y_pos))
        speed = min(10, speed + 1)
            
    disp_surface.fill((64,64,64))    
    snakegroup.draw(disp_surface)
    foods.draw(disp_surface)
    pygame.display.update()
    clock.tick(60)