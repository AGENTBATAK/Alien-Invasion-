import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''This is a class for alien in the game'''
    
    def __init__(self,ai_game):
        super().__init__() # Help us to use methods of inherited class easily.
        
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load("D:\Alien Invasion\gam_images\Screenshot 2026-04-22 050714.bmp")
        self.image = pygame.transform.scale(self.image,(50,46))
        self.rect = self.image.get_rect()
        #use to draw and track position of the image on screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)    
    def update(self):
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
  