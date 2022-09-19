import sys
from zoneinfo import available_timezones
import pygame

from bullet import Bullet
from alien import Alien

def check_keydown_event(event,ai_setting, screen,ship,bullets):
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key== pygame.K_LEFT:
            ship.moving_left = True
        elif event.key == pygame.K_w:
            fire_bullet(ai_setting, screen,ship,bullets)
        elif event.key == pygame.K_q:
            
            sys.exit()

def check_keyup_event(event,ship):
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
                ship.moving_left = False

def check_events(ai_setting, screen,ship,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event,ai_setting, screen,ship,bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_event(event,ship)

 #Создание новой пули и добавление в группу
def fire_bullet(ai_setting, screen,ship,bullets):
    if len(bullets) < ai_setting.bullet_allowed:
        new_bullet = Bullet(ai_setting, screen, ship)
        bullets.add(new_bullet)    

def bullet_update(bullets):
    bullets.update()
    #Bullet delete
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def get_number_aliens_x(ai_setting, alien_width):
    available_space_x = ai_setting.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x 

def create_alien(ai_setting, screen, aliens, alien_number):
    alien = Alien(ai_setting,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)

def create_fleet(ai_setting, screen, aliens):
    alien = Alien(ai_setting,screen)
    number_aliens_x = get_number_aliens_x(ai_setting, alien.rect.width)

    #First row UFO
    for alien_number in range(number_aliens_x):
        create_alien(ai_setting,screen,aliens, alien_number)

def update_screen(ai_setting, screen, ship, aliens, bullets):
    #Перерисовка экрана при каждом проходе цикла
    screen.fill(ai_setting.bg_color)
    #Все пули выводятся позади изображение окрабля и пришельцев
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

        #Отображение последнего прорисованного экрана
    pygame.display.flip()



