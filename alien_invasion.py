import sys
import pygame

from settings import Settings
from ship import Ship
from pygame.sprite import Group
import game_functions as gf

def run_game():
    #Инициализируем игру и создаем объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Назначение цвета фона
    bg_color = (ai_settings.bg_color)

    #Создаем корабль, группы для хранения пуль и группы пришельцев
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Создание флота пришельца
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #Запуск основного цикла игры
    while True:
        #Отслеживаем событий клавиатуры и мыши
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
