import pygame
from pygame.sprite import Sprite #The Bullet class inherits from Sprite, which we import from the pygame.sprite module

class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        
        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        # INSTEAD OF USING THE RECT ABOVE WE CAN USE DIRECT IMAGE
        self.y = float(self.rect.y)
        
# PURPOSE OF USING SPRITE:-
#1.When you use sprites, you can group related elements in your game and act on all the grouped elements at once    
    def update(self):
        self.y -= self.settings.bullet_speed #Move bullet in up direction
        self.rect.y = self.y    #Update bullet position
        
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
    
    
    
        
        
        
        
        
        