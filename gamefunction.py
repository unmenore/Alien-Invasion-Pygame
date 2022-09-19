import sys
import pygame

from bullet import Bullet

def check_keydown_event(event,ai_setting, screen,ship,bullets):
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key== pygame.K_LEFT:
            ship.moving_left = True
        elif event.key == pygame.K_q:
            fire_bullet(ai_setting, screen,ship,bullets)

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

def update_screen(ai_setting, screen, ship, bullets):
    #Перерисовка экрана при каждом проходе цикла
    screen.fill(ai_setting.bg_color)
    #Все пули выводятся позади изображение окрабля и пришельцев
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

        #Отображение последнего прорисованного экрана
    pygame.display.flip()



