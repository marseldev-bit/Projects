import sys
from pathlib import Path
from time import sleep
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alienBullet import alienBullet
from alien import Alien
from gameStats import GameStats
from button import Button
from scoreboard import Scoreboard

class AlienInvasion:
    """Управление ресурсами и поведением игры"""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.set = Settings()
        self.screen = pygame.display.set_mode((self.set.screenWidth, self.set.screenHeight))
        pygame.display.set_caption("Alien Invasion")
        self.recordFile = Path('record.txt')
        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.alienBullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.gameActive = False
        self.playButton = Button(self, "Play")
        self.difficulty = 1
        self.isSetDifficulty = False
        self.sb = Scoreboard(self)
        self.count = 0

        self._create_fleet()
    
    def runGame(self):
        """Запускает основной цикл игры"""
        while True:
            self._check_events()
            if self.gameActive:
                self.ship.update()
                self._update_aliens()
                self.update_bullets(self.count)
                if not self.alienBullets:
                    self.count += 1
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        # Отслеживание событий клавиатуры и мыши
        for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    self.saveRecord()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if not self.gameActive and not self.isSetDifficulty:
                        self.setDifficulty(event)
                        self.isSetDifficulty = True
                    if not self.gameActive and self.isSetDifficulty:
                        if event.key == pygame.K_p:
                            self._check_play_button()
                    if event.key == pygame.K_q:
                        self.saveRecord()
                        sys.exit()
                    else: self._check_keydown(event)

                elif event.type == pygame.KEYUP:
                    self._check_keyup(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.playButton.rect.collidepoint(pygame.mouse.get_pos()) and not self.gameActive:
                        self._check_play_button()

    def setDifficulty(self, event):
        if event.key == pygame.K_1:
            self.difficulty = 1
        elif event.key == pygame.K_2:
            self.difficulty = 2
        elif event.key == pygame.K_3:
            self.difficulty = 3

    def _check_play_button(self): 
        self.stats.reset_stats()
        self.sb.prep()
        self.gameActive = True
        self.bullets.empty()
        self.aliens.empty()
        pygame.mouse.set_visible(False)
        self.set.init_dynamic_set()
        self.sb.difficulty(self.difficulty)
        self._create_fleet()

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

    def _update_ship_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._alien_bullet_collisions()

    def _update_alien_bullets(self, count):
        self.alienBullets.update()
        for bullet in self.alienBullets.copy():
            if bullet.rect.top >= self.screen.get_rect().bottom:
                self.alienBullets.empty()
                break
        if count == 100:
            for alien in self.aliens.sprites():
                if alien.isShooter:
                    self._create_alienBullet(alien)
            self.count = 0
        
        self._ship_alienBullet_collision()

    def update_bullets(self, count):
        self._update_alien_bullets(count)
        self._update_ship_bullets()
    
    def _alien_bullet_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions: 
            for coll in collisions.values():
                self.stats.score += self.set.alien_points * len(coll)
            self.sb.prep_score()
            self.sb.check_record()
        if not self.aliens:
            self.startNewLevel()
    
    def _ship_alienBullet_collision(self):
        collisions = pygame.sprite.spritecollide(self.ship, self.alienBullets, False)
        if collisions:
            self._ship_hit()

    def _create_fleet(self):
        alien = Alien(self)
        currentTop = 150
        isShooter = False
        while currentTop < (self.set.screenHeight - (alien.rect.height * 10)):
            if currentTop + alien.rect.height + alien.y >= self.set.screenHeight - (alien.rect.height * 10):
                isShooter = True
            currentLeft = alien.x
            while currentLeft < (self.set.screenWidth - (alien.rect.width + alien.x)):
                self._create_alien(currentLeft, currentTop, isShooter)
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

    def _create_alien(self, left, top, isShooter):
        newAlien = Alien(self)
        newAlien.rect.left = left
        newAlien.rect.top = top
        if isShooter: 
            newAlien.isShooter = True
        self.aliens.add(newAlien)

    def _create_alienBullet(self, alien):
        newAlienBullet = alienBullet(self)
        newAlienBullet.setPos(alien.rect.bottom, alien.rect.centerx)
        self.alienBullets.add(newAlienBullet)
    
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
            self.sb.prep_ships()
            self.aliens.empty()
            self.bullets.empty()
            self.alienBullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else: 
            self.isSetDifficulty = False
            self.gameActive = False
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        self.screen.fill(self.set.bg)
        for bullet in self.bullets.sprites():
            bullet.showBullet()
        for bullet in self.alienBullets.sprites():
            bullet.showAlienBullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        self.sb.show_score()
        if not self.gameActive:
            self.playButton.drawButton()
        # Отображение последнего прорисованного экрана
        pygame.display.flip()
    
    def saveRecord(self):
        self.recordFile.write_text(str(self.stats.record))
         
    def getRecord(self):
        return int(self.recordFile.read_text())
    
    def startNewLevel(self):
        self.bullets.empty()
        self._create_fleet()
        self.set.increase_speed()
        self.stats.level += 1
        self.sb.prep_level()

    

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.runGame()




