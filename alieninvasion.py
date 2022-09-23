import pygame
from bullet import Bullet
import gamefunction as gf

from settings import Setting
from spaceship import Spaceship
from pygame.sprite import Group
from alien import Alien
from gamestats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():

    #Создание окна
    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode((ai_setting.screen_height, ai_setting.screen_width))
    pygame.display.set_caption("Alien Invasion")

    #Create Play-button
    play_button = Button(ai_setting, screen, "Start game")

    #Create ship
    ship = Spaceship(ai_setting,screen)
    bullets = Group()
    aliens = Group()
    stats = GameStats(ai_setting)
    sb = Scoreboard(ai_setting, screen, stats)

    gf.create_fleet(ai_setting, screen, ship, aliens)

    #Запуск основного цикла игры
    while True:
        #Control
        gf.check_events(ai_setting, screen,ship, bullets, stats, play_button, aliens)
        if stats.game_active:
            ship.update()
            gf.bullet_update(ai_setting, stats, screen, sb ,ship, aliens, bullets)
            gf.update_aliens(ai_setting, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_setting, stats, screen, sb ,ship, aliens, bullets, play_button)
run_game()