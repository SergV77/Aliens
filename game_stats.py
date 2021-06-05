import pygame
from pygame.sprite import Sprite

class GameStats:
    """Отслеживание статистики для игры Alien Invasion."""

    def __init__(self, ai_settings):
        """Инициализирует статистику"""
        self.ai_settings = ai_settings
        self.reset_stats()

        #Игра Alien Invasiou запускается в активном состоянии.
        self.game_active = True

    def reset_stats(self):
        """Иницилизирует статистику, изменяющуюся в ходе игры."""
        self.ships_left = self.ai_settings.ship_limit