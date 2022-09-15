import pygame

class Spaceship():
    
    def __init__(self, ai_setting,screen) -> None:
        #Инициализируем корабль и задаем стартовую позицию
        self.screen = screen
        self.ai_setting = ai_setting

        self.moving_right = False
        self.moving_left = False

        #Download spaceship.png in project
        self.image = pygame.image.load('npc/spaceship2.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Каждый новый корабль появляется у нижнего края экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Сохранение координаты корабля
        self.center = float(self.rect.centerx)

    
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_setting.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.center -= self.ai_setting.ship_speed

        #Обновление атрибута rect на основании self.center
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)