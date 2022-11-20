import pygame
import pygame as pg
TILESIZE = 25

class Snake(pygame.sprite.Sprite):
    images = None
    def __init__(self, grp, pos, length, parent=None):
        super().__init__(grp)
        self.parent = parent
        self.child = None
        self.direction = 'w'
        self.length = length
        self.grp = grp
        if not self.parent: self.image = Snake.images['head_w']
        elif length == 1: self.image = Snake.images['tail_w']
        else: self.image = Snake.images['body_ww']

        self.pos = pos
        self.rect = self.image.get_rect(x=self.pos[0]*TILESIZE, y=self.pos[1]*TILESIZE)
        if length > 1:
            self.child = Snake(grp, (pos[0]-1, pos[1]), length-1, self)

    def move(self):
        # if we have a parent, let's look were it moves
        parent_direction = self.parent.direction if self.parent else None

        if self.direction == 'n': self.pos = self.pos[0], self.pos[1] - 1
        elif self.direction == 's': self.pos = self.pos[0], self.pos[1] + 1
        elif self.direction == 'e': self.pos = self.pos[0] - 1, self.pos[1]
        elif self.direction == 'w': self.pos = self.pos[0] + 1, self.pos[1]

        self.rect = self.image.get_rect(x=self.pos[0]*TILESIZE, y=self.pos[1]*TILESIZE)

        # move the child
        if self.child:
            self.child.move()

        if not self.parent: self.image = Snake.images['head_' + self.direction]
        elif not self.child: self.image = Snake.images['tail_' + parent_direction]
        else: self.image = Snake.images['body_' + parent_direction + self.direction]

        # follow the parent
        if parent_direction:
            self.direction = parent_direction

    def update(self):
        # no parent means we're the head of the snake
        # and we should move we a key is pressed
        if not self.parent:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_w]: self.direction = 'n'
            if pressed[pygame.K_s]: self.direction = 's'
            if pressed[pygame.K_a]: self.direction = 'e'
            if pressed[pygame.K_d]: self.direction = 'w'


def load_snake_img():
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

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 480))
    Snake.images = load_snake_img()
    # let's trigger the MOVE event every 500ms
    MOVE = pygame.USEREVENT + 1
    pygame.time.set_timer(MOVE, 300)

    all_sprites = pygame.sprite.Group()
    snake = Snake(all_sprites, (4, 8), 8)
    clock = pygame.time.Clock()
    dt = 0
    while True:
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                return
            if e.type == MOVE:
                # print(snake.child)
                snake.move()

        screen.fill((30, 30, 30))

        all_sprites.update()
        all_sprites.draw(screen)

        dt = clock.tick(60)
        pygame.display.flip()

main()