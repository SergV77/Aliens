import pygame.image

class Ship:
    def __init__(self, ai_settings, screen):
        """Инициализируем корабль и задаем его начальную позицию"""
        self.screen = screen
        self.ai_settings = ai_settings

        #Загрузка изображение корабля и получение прямоугольника
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Каждый новый корабль появляется у нижнего края экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Сохранение вещественной координаты коробля
        self.center = float(self.rect.centerx)

        #Флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновляем позицию корабля с учетом флага."""
        #Обновление атрибута center, не rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        #Обнавление отрибута rect на основании self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Рисуем корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Размещает корабль в центре нижней стороны."""
        self.center = self.screen_rect.centerx