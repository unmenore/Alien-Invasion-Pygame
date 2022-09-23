import sys
import pygame

from bullet import Bullet
from alien import Alien
from time import sleep


#Нажатие клавиш
def check_keydown_event(event,ai_setting, screen,ship, bullets, stats, play_button, aliens):
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key== pygame.K_LEFT:
            ship.moving_left = True
        elif event.key == pygame.K_w:
            fire_bullet(ai_setting, screen,ship,bullets)
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_p and not stats.game_active:
            start_game(ai_setting, stats, screen, ship, aliens, bullets)

def check_keyup_event(event,ship):
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
                ship.moving_left = False

def check_events(ai_setting, screen,ship, bullets, stats, play_button, aliens):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_setting, stats, screen, ship, aliens, bullets, play_button, mouse_x, mouse_y)
        
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event,ai_setting, screen,ship, bullets, stats, play_button, aliens)

        elif event.type == pygame.KEYUP:
            check_keyup_event(event,ship)


def check_play_button(ai_setting, stats, screen, ship, aliens, bullets, play_button, mouse_x, mouse_y):

    #Блокировка кнопки Play
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        start_game(ai_setting, stats, screen, ship, aliens, bullets)

def start_game(ai_setting, stats, screen, ship, aliens, bullets):

        ai_setting.initialize_dynamic_setting()
           #Скрытие указателя мыши
        pygame.mouse.set_visible(False)
        #Сброс игровой статистики
        stats.reset_stats()
        stats.game_active = True

        #Очистка списков пришельцев и пуль
        aliens.empty()
        bullets.empty()

        #Создание нового флота и размещение корабля в центре
        create_fleet(ai_setting, screen, ship, aliens)
        ship.center_ship()

#Снижение флота и смена направления
def check_fleet_edges(ai_setting,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_setting,aliens)
            break

def change_fleet_direction(ai_setting, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_setting.fleet_drop_speed
    ai_setting.fleet_direction *= -1



#Создание новой пули и добавление в группу
def fire_bullet(ai_setting, screen,ship,bullets):
    if len(bullets) < ai_setting.bullet_allowed:
        new_bullet = Bullet(ai_setting, screen, ship)
        bullets.add(new_bullet)    

def bullet_update(ai_setting, screen, ship, bullets, aliens):
    bullets.update()
    #Bullet delete
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collision(ai_setting, bullets, screen, ship, aliens)

def check_bullet_alien_collision(ai_setting, bullets, screen, ship, aliens):
    #УДаение пришельцев при колизии
    colision = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        #УНичтожеие существующих пуль и создание нового флота
        bullets.empty()
        ai_setting.increase_speed()
        create_fleet(ai_setting, screen,ship,aliens)

#Заполнение экрана пришельцами
def get_number_aliens_x(ai_setting, alien_width):
    available_space_x = ai_setting.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x 

def get_number_rows(ai_setting, ship_height, alien_height):
    #Определение рядов помещающихся на экран
    available_space_y = (ai_setting.screen_height - (3 * alien_height - ship_height))
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_setting, screen, aliens, alien_number, row_number):
    alien = Alien(ai_setting,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_setting, screen, ship, aliens):
    alien = Alien(ai_setting,screen)
    number_aliens_x = get_number_aliens_x(ai_setting, alien.rect.width)
    number_rows = get_number_rows(ai_setting, ship.rect.height, alien.rect.height)

    #Create fleet UFo
    for row_number in range(number_rows):
    #First row UFO
        for alien_number in range(number_aliens_x):
            create_alien(ai_setting,screen,aliens, alien_number,row_number)


def update_aliens(ai_setting, stats, screen, ship, aliens, bullets):
    #Проверяет, достиг ли флот края экрана, после чего обновляет позиции всех пришельцев во флоте.
    check_fleet_edges(ai_setting, aliens)
    #Проверка пришлеьцев доехавших до конца экрана
    check_alien_bottom(ai_setting, stats, screen, ship, aliens, bullets)
    #Обновляет позиции всех во флоте
    aliens.update()

    #ПРоверка колицизий "Пришелец-кораьбль"
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_setting, stats, screen, ship, aliens, bullets)

def check_alien_bottom(ai_setting, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_setting, stats, screen, ship, aliens, bullets)
            break

#Столковение корабля с пришельцами
def ship_hit(ai_setting, stats, screen, ship, aliens, bullets):
        
    if stats.ships_left > 0:
        stats.ships_left -= 1
        #ОЧеистка пришельцев и пуль
        aliens.empty()
        bullets.empty()
        #Создание нового флота
        create_fleet(ai_setting, screen, ship, aliens)
        ship.center_ship()
        #Пауза
        sleep(0.5)

    else:
        stats.game_active = False

#Обновление экрана
def update_screen(ai_setting, stats, screen, ship, aliens, bullets, play_button):
    #Перерисовка экрана при каждом проходе цикла
    screen.fill(ai_setting.bg_color)
    #Все пули выводятся позади изображение окрабля и пришельцев
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    if not stats.game_active:
        play_button.draw_button()

        #Отображение последнего прорисованного экрана
    pygame.display.flip()



