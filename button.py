#All bottom control
import pygame.font

class Button():

    def __init__(self, ai_setting, screen, msg) -> None:
        #Атрибуты кнопки
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #Настройки кнопки
        self.width = 200
        self.heigh = 50
        self.button_colour = (255, 154, 0)
        self.text_colour = (255,255,255)
        self.font = pygame.font.SysFont(None, 32)

        #Построение объекта rect и выравнивани по центру
        self.rect = pygame.Rect(0,0, self.width, self.heigh)
        self.rect.center = self.screen_rect.center

        #Сообщение кнопки
        self.prep_msg(msg)

    
    def prep_msg(self, msg):
        #Перпобразование message в прямоугольник и выравнивание по центру
        self.msg_image = self.font.render(msg, True, self.text_colour, self.button_colour)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    
    def draw_button(self):
        #Отображение пустой кнопки и вывод сообщения
        self.screen.fill(self.button_colour, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)