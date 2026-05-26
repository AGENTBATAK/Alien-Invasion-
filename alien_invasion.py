import sys
import setting
import pygame
import ship
import keybind
from bullet import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

class Alien_invasion:
    speed = 2
    def __init__(self):
        pygame.init()
        self.settings = setting.Settings()
        self.clock = pygame.time.Clock()
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("ALIEN GAME")
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.ship = ship.Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.create_fleet()
        self.game_active = False
        self.play_button = Button(self,"Play")
    

        
    def run_game(self):
        while True:
            self._check_event()#We make a new _check_events() method 2 and move the lines that check
                               #whether the player has clicked to close the window into this new method.
            if self.game_active:
                self._update_ship()
                self._update_bullets()
                self._update_aliens()    
                self.bullets.update()
            self.clock.tick(100)                  
            self._update_screen()
    def _check_play_button(self,mouse_pos):
        #only start when player click
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            #Reset the game settings
            self.settings.initialize_dynamic_settings()
            #to hide mouse cursor
            pygame.mouse.set_visible(False)
            #resetting stats
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            self.game_active = True
            #getting rid of remaining bullet , aliens
            self.bullets.empty()
            self.aliens.empty()
            #Creating new fleet and all
            self.create_fleet()
            self.ship.center_ship()        
    def _check_event(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)
                
    def _fire_bullet(self):
        # Creates a new bullet and add it to the bullet grp.
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)        
    def _update_bullets(self):
        #This will help us to update bullet postiion and remove old ones and add new ones.
        self.bullets.update()
        
        for bullets in self.bullets.copy():
            if bullets.rect.bottom<= 0:
                self.bullets.remove(bullets)
        
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens , True ,True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        if not self.aliens:
            self.bullets.empty()
            self.create_fleet()
            self.settings.increase_speed()
            
            # Increase level.
            self.stats.level += 1
            self.sb.prep_level()
        
    def _ship_hit(self):
        if self.stats.ships_left>0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            self.bullets.empty()
            self.aliens.empty()
            self.create_fleet()
            self.ship.center_ship()
            sleep(0.5)    
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)
    def _check_aliens_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break    
    def _update_screen(self):
            self.screen.fill(self.settings.bg_color)
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.ship.blitme()
            self.aliens.draw(self.screen)
            self.sb.show_score() # Draw the score information.
            if not self.game_active:
                self.play_button.draw_button()
            pygame.display.flip()
    def _update_ship(self):
        if keybind.move_up():
            if self.ship.rect.top > 0:
                self.ship.rect.y -= self.speed
        if keybind.move_down():
            if self.ship.rect.bottom < self.settings.screen_height:
                self.ship.rect.y += self.speed
        if keybind.move_left():
            if self.ship.rect.left > 0:
                self.ship.rect.x -= self.speed
        if keybind.move_right():
            if self.ship.rect.right < self.settings.screen_width:
                self.ship.rect.x += self.speed
        if keybind.space_key():
            self._fire_bullet()
            
        #self.ship.rect.clamp_ip(self.screen.get_rect()) #We can use this directly instead of using too much if loops
    def create_fleet(self):   #This is going to create new aliens and add them horizontally till there is no room left and now going to create rows as well
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        
        current_x , current_y = alien_width , alien_height# we create a var that hold alien width and height a.k.a the width of single alien and its height
        #WE GOING TO RUN TWO LOOP THE FIRST ONE WILL SHIFT THE ROW AND SECOND ONE WORK AS SAME AS BEFORE
        
        while current_y < (self.settings.screen_height - 4*alien_height): 
            while current_x < (self.settings.screen_width - 4*alien_width): #this loop will take the width and compare it to the whole screen leaving just the amount of space we mentioned here
                self.create_alien(current_x,current_y)
                current_x += 6*alien_width
            # WE RESET VALUE OF x BEFORE EACH NEXT ROW AND INCREASE Y VALUE
            current_x = alien_width
            current_y += 4*alien_height
            # WE DO NOT NEEED TO SETUP SEPERATE FUNC FOR Y BECAUSE IT JUST SHIFT LINE IN THIS CODE THE SPRITE IS ONLY GETTING USED BY x OR HORIZONTAAL CREATION  OF ALIENS
    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()
    
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
    def create_alien(self,x_position,y_position):
        new_alien = Alien(self)  #create new alien
        new_alien.x = x_position  # put that new alien to current_x variable
        new_alien.rect.x = x_position # Check the position of the alien on screen and store it
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)# add alien on the screen
            

if __name__=='__main__':
    ai = Alien_invasion()
    ai.run_game()















































