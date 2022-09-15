import pygame

class Spaceship():
    
    def __init__(self, screen) -> None:
        #Инициализируем корабль и задаем стартовую позицию
        self.screen = screen
        self.moving_right = False
        self.moving_left = False

        #Download spaceship.png in project
        self.image = pygame.image.load('npc/spaceship2.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Каждый новый корабль появляется у нижнего края экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
    
    def update(self):
        if self.moving_right:
            self.rect.centerx +=1
        if self.moving_left:
            self.rect.centerx -=1

    def blitme(self):
        self.screen.blit(self.image, self.rect)