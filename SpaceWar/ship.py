import pygame 

class Ship:
    """Класс для управления кораблем"""

    def __init__(self, aiGame):
        """Инициализирует корабль и задает его начальную позицию"""
        self.screen = aiGame.screen
        self.screenRect = aiGame.screen.get_rect()
        self.set = aiGame.set

        # Загружает изображение корабля и получает прямоугольник
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Каждый новый корабль появляется у нижнего края экрана
        self.rect.midbottom = self.screenRect.midbottom

        # Сохранение координаты центра корябля
        self.x = float(self.rect.x)

        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screenRect.right: self.x += self.set.shipSpeed
        if self.moving_left and self.rect.left > 0: self.x -= self.set.shipSpeed
        self.rect.x = self.x

    def blitme(self):
        """Рисует корабль"""
        self.screen.blit(self.image, self.rect)