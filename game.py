from states.title import Title

import pygame as pg


class Game:
    def __init__(self):
        pg.init()
        self.WINDOW_WIDTH = 500
        self.WINDOW_HEIGHT = 500
        self.SCREEN_WIDTH = self.WINDOW_WIDTH*1.2
        self.SCREEN_HEIGHT = self.WINDOW_HEIGHT*1.2
        self.game_canvas = pg.Surface((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.TILE_SIZE = 25
        self.screen = pg.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.clock = pg.time.Clock()
        self.actions = {"left":False, "right":False, "up":False, "down":False, "space":False, "pause":False}
        self.dt, self.prev_time = 0, 0
        self.state_stack = []
        self.playing = True
        self.running = True
        self.pausing = False
        self.load_state()
    
    def game_loop(self):
        while self.playing:
            self.get_dt()
            self.check_event()
            self.update()
            self.render()
    
    def update(self):
        self.state_stack[-1].update(self.dt, self.actions)
        
    def render(self):
        self.state_stack[-1].render(self.game_canvas)
        self.screen.blit(pg.transform.scale(self.game_canvas,(self.SCREEN_WIDTH,self.SCREEN_HEIGHT)), (0,0))
        pg.display.flip()
    
    def draw_text(self, surface, text, text_size, color, x, y):
        self.font = pg.font.SysFont("comicsansms", text_size)
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_surface, text_rect)
    
    def get_dt(self):
        self.dt = self.clock.tick(30)
        self.prev_time = pg.time.get_ticks()
    
    def load_state(self):
        self.title_screen = Title(self)
        self.state_stack.append(self.title_screen)
        
    def check_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.playing = False
                    self.running = False
                if event.key == pg.K_a:
                    self.actions["left"] = True
                if event.key == pg.K_d:
                    self.actions["right"] = True
                if event.key == pg.K_w:
                    self.actions["up"] = True
                if event.key == pg.K_s:
                    self.actions["down"] = True
                if event.key == pg.K_p:
                    self.actions["pause"] = True
                if event.key == pg.K_SPACE:
                    self.actions["space"] = True
            
            if event.type == pg.KEYUP:
                if event.key == pg.K_a:
                    self.actions["left"] = False
                if event.key == pg.K_d:
                    self.actions["right"] = False
                if event.key == pg.K_w:
                    self.actions["up"] = False
                if event.key == pg.K_s:
                    self.actions["down"] = False
                if event.key == pg.K_p:
                    self.actions["pause"] = False
                if event.key == pg.K_SPACE:
                    self.actions["space"] = False
    
    def reset_keys(self):
        for action in self.actions:
            self.actions[action] = False

if __name__ == "__main__":
    g = Game()
    while g.running:
        g.game_loop()