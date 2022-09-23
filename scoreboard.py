import pygame.font

class Scoreboard():

    def __init__(self,ai_setting,screen,stats) -> None:
        self.screen = screen
        self.sreen_rect = screen.get_rect()
        self.ai_setting = ai_setting
        self.stats = stats

        #Настройки вывода счета
    
        self.text_color = (50,50,50)
        self.font = pygame.font.SysFont(None,32)

        self.prer_score()

    def prep_score(self):
        #Пепобразует счет в графическое изображение
        score_str = str(self.stats.score)
        self.stats_image = self.font.render(score_str, True, self.tex_color, self.ai_setting.bg_color)

        #Вывод счета в части экрана
        self.score_rect=self.score_image.get_rect()
        self.score_rectleft = self.scren_rect.left + 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)