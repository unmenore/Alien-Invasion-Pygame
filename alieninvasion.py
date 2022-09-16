from email.headerregistry import Group
import pygame
from bullet import Bullet
import gamefunction as gf

from settings import Setting
from spaceship import Spaceship
from pygame.sprite import Group


def run_game():

    #Создание окна
    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode((ai_setting.screen_height, ai_setting.screen_width))
    pygame.display.set_caption("Alien Invasion")

    #Create ship
    ship = Spaceship(ai_setting,screen)
    bullets = Group()

    #Запуск основного цикла игры
    while True:
        
        #Control
        gf.check_events(ai_setting, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_setting, screen, ship, bullets)
run_game()