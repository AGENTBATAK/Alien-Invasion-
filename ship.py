import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        #Load image
        
        self.image = pygame.image.load('D:\Alien Invasion\gam_images\Ship.bmp')
        self.image2=pygame.transform.scale(self.image,(65,65)) # Scale size of the ship
        self.rect = self.image2.get_rect()
        
        self.rect.midbottom = self.screen_rect.midbottom
        
    def blitme(self):
        self.screen.blit(self.image2, self.rect)
    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        
        
        
        
        
#We import the pygame module before defining the class. The __init__()
#method of Ship takes two parameters: the self reference and a reference to
#the current instance of the AlienInvasion class. This will give Ship access to
#all the game resources defined in AlienInvasion. We then assign the screen
#to an attribute of Ship 1, so we can access it easily in all the methods in this
#class. We access the screen’s rect attribute using the get_rect() method and
#assign it to self.screen_rect 2. Doing so allows us to place the ship in the
#correct location on the screen.
#To load the image, we call pygame.image.load() 3 and give it the location
#of our ship image. This function returns a surface representing the ship,
#which we assign to self.image. When the image is loaded, we call get_rect() to
#access the ship surface’s rect attribute so we can later use it to place the ship.
#Start each new ship at bottom of the screen 