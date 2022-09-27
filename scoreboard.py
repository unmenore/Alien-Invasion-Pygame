import pygame.font

class Scoreboard():

    def __init__(self,ai_setting,screen,stats) -> None:
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_setting = ai_setting
        self.stats = stats

        #Настройки вывода счета
    
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,32)

        self.prep_score()
        self.prep_game_record()

    def prep_score(self):
        #Пепобразует счет в графическое изображение
        round_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(round_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_setting.bg_color)

        #Вывод счета в части экрана
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left + 20
        self.score_rect.top = 10

    def show_score(self):
        #Вывод счета на экран
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.game_record_image, self.game_record_rect)

    def prep_game_record(self):
        game_record = int(round(self.stats.game_record, -1))
        game_record_str = "{:,}".format(game_record)
        self.game_record_image = self.font.render(game_record_str, True, self.text_color, self.ai_setting.bg_color)

        #Выравнимание рекорда по центру верхней стороны
        self.game_record_rect = self.game_record_image.get_rect()
        self.game_record_rect.centerx = self.screen_rect.centerx
        self.game_record_rect.top = self.score_rect.top