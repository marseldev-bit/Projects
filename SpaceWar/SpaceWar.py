import sys
from time import sleep
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from gameStats import GameStats

class AlienInvasion:
    """Управление ресурсами и поведением игры"""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.set = Settings()
        self.screen = pygame.display.set_mode((self.set.screenWidth, self.set.screenHeight))
        pygame.display.set_caption("Alien Invasion")
        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.gameActive = True

        self._create_fleet()
    
    def runGame(self):
        """Запускает основной цикл игры"""

        while True:
            self._check_events()
            if self.gameActive:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
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
        self._alien_bullet_collisions()
    
    def _alien_bullet_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _create_fleet(self):
        alien = Alien(self)
        currentTop = alien.y
        while currentTop < (self.set.screenHeight - (alien.rect.height * 3)):
            currentLeft = alien.x
            while currentLeft < (self.set.screenWidth - (alien.rect.width + alien.x)):
                self._create_alien(currentLeft, currentTop)
                currentLeft += 2 * alien.rect.width
            currentTop += alien.rect.height + alien.y

    def _check_fleet_edges(self):
        for alien in self.aliens:
            if alien.check_edges():
                self._change_fleet_directions()
                break
    
    def _change_fleet_directions(self):
        for alien in self.aliens:
            alien.rect.y += self.set.fleet_drop_speed
        self.set.fleet_direction *= -1

    def _create_alien(self, left, top):
        newAlien = Alien(self)
        newAlien.rect.left = left
        newAlien.rect.top = top
        self.aliens.add(newAlien)
    
    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()
    
    def _check_aliens_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.set.screenHeight:
                self._ship_hit()
                break
    
    def _ship_hit(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else: 
            self.gameActive = False

    def _update_screen(self):
        self.screen.fill(self.set.bg)
        for bullet in self.bullets.sprites():
            bullet.showBullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        # Отображение последнего прорисованного экрана
        pygame.display.flip()
         
    

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.runGame()




