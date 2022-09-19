class Setting():
    
    def __init__(self) -> None:
        
        #Screen setting
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        #ship speed
        self.ship_speed = 1.5

        #Bullet setting
        self.bullet_speed_factor = 1
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (230,230,230)
        self.bullet_allowed = 10

        #Alien setting
        self.alien_speed_factor = 0.3
        self.fleet_drop_speed = 3
        #fleet_direction = 1 обозначает движение вправо, -1 влево
        self.fleet_direction = 1
    