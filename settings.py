class Setting():
    
    def __init__(self) -> None:
        
        #Screen setting
        self.screen_width = 800
        self.screen_height = 1200
        self.bg_color = (0, 0, 0)

        #ship speed
        self.ship_speed = 1.5

        #Bullet setting
        self.bullet_speed_factor = 1
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (230,230,230)
        self.bullet_allowed = 10
    