import sys
import pygame

from settings import Setting
from spaceship import Spaceship
import gamefunction as gf

def run_game():

    #Создание окна
    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode((ai_setting.screen_height, ai_setting.screen_width))
    pygame.display.set_caption("Alien Invasion")

    #Create ship
    ship = Spaceship(ai_setting,screen)

    #Запуск основного цикла игры
    while True:
        
        #Control
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_setting, screen, ship)
run_game()