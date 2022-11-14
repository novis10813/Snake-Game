import pygame as pg


class Button:
    def __init__(self, pos, img, scale=1):
        width = img.get_width()
        height = img.get_height()
        self.image = pg.transform.scale(img, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.clicked = False
    
    def draw(self, surface):
        action = False
        pos = pg.mouse.get_pos()
        if self.rect.collidepoint(pos): # check hover
            
            if pg.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True
        
        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False
                
        surface.blit(self.image, self.rect.topleft)
        
        return action