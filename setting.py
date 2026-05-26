class Settings:
    def __init__(self):
        # Scrreen setting
        self.screen_width = 1200
        self.screen_height = 900
        self.bg_color=(32,32,33) # Code for black background
        #Bullet work
        self.bullet_speed = 6.0
        self.bullet_width = 5.0
        self.bullet_height = 2
        self.bullet_color = (88,188,88)
        self.bullets_allowed = 4
        #Aliens setting
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #fleet direction of 1 represent right; -1 represent left.
        self.fleet_direction = 1