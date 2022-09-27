#setting for game
class Setting():
    
    def __init__(self) -> None:
        
        #Screen setting
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        #ship speed
        self.ship_limit = 3

        #Bullet setting
        self.bullet_speed_factor = 1
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (230,230,230)
        self.bullet_allowed = 5

        #Alien setting
        self.fleet_drop_speed = 10

        #Темп укорения игры
        self.speed_scale = 1.1
        #Тем ускорения стоимости
        self.score_scale = 1.5
        self.initialize_dynamic_setting()


    def initialize_dynamic_setting(self):
        self.ship_speed_factor = 1.5
        self.alien_speed_factor = 0.3

        #fleet_direction = 1 обозначает движение вправо, -1 влево
        self.fleet_direction = 1

        #Подсчет очков
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speed_scale
        self.bullet_width *= self.speed_scale
        self.alien_speed_factor *= self.speed_scale

        self.alien_points = int(self.alien_points * self.score_scale)