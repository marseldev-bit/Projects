import pygame.font
from pygame.sprite import Sprite
from ship import Ship

class Scoreboard:
    def __init__(self, aiGame):
        self.screen = aiGame.screen
        self.screenRect = self.screen.get_rect()
        self.set = aiGame.set
        self.stats = aiGame.stats
        self.game = aiGame

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep()
    
    def prep_score(self):
        self.score_image = self.font.render(f"Очки: {round(self.stats.score, -1):,}", True, self.text_color, self.set.bg)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screenRect.right - 20
        self.score_rect.top = 20

    def prep_record(self):
        record = round(self.stats.record, -1)
        self.record_image = self.font.render(f"Рекорд: {record:,}", True, self.text_color, self.set.bg)
        self.record_rect = self.record_image.get_rect()
        self.record_rect.centerx = self.screenRect.centerx
        self.record_rect.top = self.score_rect.top

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.record_image, self.record_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
    
    def check_record(self):
        if self.stats.score > self.stats.record:
            self.stats.record = self.stats.score
            self.prep_record()
    
    def prep_level(self):
        self.level_image = self.font.render(f"Уровень: {str(self.stats.level)}", True, self.text_color, self.set.bg)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
    
    def difficulty(self, level):
        if level == 2:
            for i in range(3):
                self.set.increase_speed()
            self.stats.level += 2
            self.prep_level()
        elif level == 3:
            for i in range(5):
                self.set.increase_speed()
            self.stats.level += 4
            self.prep_level()
    
    def prep_ships(self):
        self.ships = pygame.sprite.Group()
        for number in range(self.stats.ships_left):
            ship = Ship(self.game)
            ship.rect.x = 10 + number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
    
    def prep(self):
        self.prep_score()
        self.prep_record()
        self.prep_level()
        self.prep_ships()