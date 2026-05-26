class Settings:
    def __init__(self):
        # Scrreen setting
        self.screen_width = 1200
        self.screen_height = 900
        self.bg_color=(32,32,33) # Code for black background
        #Ship settings
        self.ship_limit = 3
        #Bullet work
        self.bullet_speed = 10.0
        self.bullet_width = 7.0
        self.bullet_height = 5
        self.bullet_color = (4, 217, 255)
        self.bullets_allowed = 8
        #Aliens setting
        self.alien_speed = 1.5
        self.fleet_drop_speed = 15
        #Defining how fast game speed increase
        self.speedup_scale = 1.9
        #How quick the alien point value increase
        self.score_scale =1.8
        self.initialize_dynamic_settings()
        #aliens scoring part
        self.alien_points = 50
        
    def initialize_dynamic_settings(self):
        #Initializing setting which will effect the entities throughout  the game
        self.ship_speed = 2
        self.bullet_speed = 2.5
        self.alien_speed = 1.5
        #fleet direction of 1 represent right; -1 represent left.
        self.fleet_direction = 1
        #Note :- This method can stay outside if we do not use this dynamic
        #function but because we want the direction to reset when game reset we 
        #use this.
        
    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)