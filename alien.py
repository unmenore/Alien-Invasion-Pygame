import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_setting, screen) -> None:
        super().__init__()
        self.screen = screen
        self.ai_setting = ai_setting


        #Download UFO image
        self.image = pygame.image.load('npc/ufo.png')
        self.rect = self.image.get_rect()

        #UFO position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Save start position UFO
        self.x = float(self.rect.x)


    def blitme(self):
        #Input UFO in position
        self.screen.blit(self.image, self.rect)


    def check_edges(self):
        #Возвращает True, если пришелец находится у края экрана.
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True


    def update(self):
        #Перемещение пришельца влево или вправо
        self.x += (self.ai_setting.alien_speed_factor * self.ai_setting.fleet_direction)
        self.rect.x = self.x
