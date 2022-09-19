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