#This creat bullet
import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    
    def __init__(self, ai_setting, screen, ship) -> None:
        super().__init__()
        self.screen = screen
        #Start bullet position

        self.rect = pygame.Rect(0, 0, ai_setting.bullet_width,ai_setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top


        #Save bullet position
        self.y = float(self.rect.y)

        self.color = ai_setting.bullet_color
        self.speed_factor= ai_setting.bullet_speed_factor
    
    def update(self):
        #Перемещение пули вверх по экрану
        #Обновление пули в вещественном формате
        self.y -= self.speed_factor
        #Обновление позиции прямоугольника
        self.rect.y = self.y
    
    def draw_bullet(self):
        #Вывод пули на экран
        pygame.draw.rect(self.screen, self.color, self.rect)