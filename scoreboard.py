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

    def prep_score(self):
        #Пепобразует счет в графическое изображение
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_setting.bg_color)

        #Вывод счета в части экрана
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left + 20
        self.score_rect.top = 10

    def show_score(self):
        #Вывод счета на экран
        self.screen.blit(self.score_image, self.score_rect)