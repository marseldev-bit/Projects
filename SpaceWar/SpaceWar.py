import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Управление ресурсами и поведением игры"""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.set = Settings()
        self.screen = pygame.display.set_mode((self.set.screenWidth, self.set.screenHeight))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
    
    def runGame(self):
        """Запускает основной цикл игры"""

        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        # Отслеживание событий клавиатуры и мыши
        for event in pygame.event.get(): 
                if event.type == pygame.QUIT: sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
                    else: self._check_keydown(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup(event)


    def _check_keydown(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        if len(self.bullets) <= self.set.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        self.screen.fill(self.set.bg)
        for bullet in self.bullets.sprites():
            bullet.showBullet()
        self.ship.blitme()
        # Отображение последнего прорисованного экрана
        pygame.display.flip()
         
    

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.runGame()




