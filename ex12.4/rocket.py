import pygame
from rocketModel import Rocket
from bullets import Bullet
from enemy import Enemy
import sys

class RocketGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.screenRect = self.screen.get_rect()
        self.screenTitle = pygame.display.set_caption("Rocket")
        self.bg = (42, 50, 75)
        self.clock = pygame.time.Clock()

        self.enemy = Enemy(self)
        self.model = Rocket(self)
        self.bullets = pygame.sprite.Group()
        self.maxBullets = 2

        self.moveRight = False
        self.moveLeft = False
        self.moveUp = False
        self.moveDown = False
        self.isEnemy = True

    def runGame(self):
        while True:
            self.check_event()
            self.updateBullet()
            self.enemy.run()
            self.model.moveRocket()
            if not self.checkHit(): self.isEnemy = False
            self.updateScreen(self.isEnemy)
            self.clock.tick(60)

    def checkHit(self):
        for bullet in self.bullets:
            if pygame.sprite.collide_rect(bullet, self.enemy):
                return False 
        return True

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q: sys.exit()
                elif event.key == pygame.K_UP:
                    self.moveUp = True
                elif event.key == pygame.K_DOWN:
                    self.moveDown = True
                elif event.key == pygame.K_SPACE:
                    self.goBullets()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.moveUp = False
                elif event.key == pygame.K_DOWN:
                    self.moveDown = False
    
    def goBullets(self):
        if len(self.bullets) <= self.maxBullets:
            newBullet = Bullet(self)
            self.bullets.add(newBullet)
        
    def updateScreen(self, isEnemy):
        self.screen.fill(self.bg)
        if isEnemy: self.enemy.showEnemy()
        for bullet in self.bullets:
            bullet.drawBullet()
        self.model.showModel()
        pygame.display.flip()

    def updateBullet(self):
        for bullet in self.bullets: 
            bullet.shoot()
        for bullet in self.bullets.copy():
            if bullet.rect.right >= self.screenRect.right:
                self.bullets.remove(bullet)

if __name__ == "__main__":
    rock = RocketGame()
    rock.runGame()

