class GameStats():

    def __init__(self, ai_setting) -> None:
        self.ai_setting = ai_setting
        self.reset_stats()
        #Игра запускается в активном состояении
        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.ai_setting.ship_limit
        self.score = 0

