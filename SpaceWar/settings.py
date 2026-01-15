class Settings:
    """Класс для хранения настроек игры Space War"""

    def __init__(self):
        self.screenWidth = 1200
        self.screenHeight = 800
        self.bg = (142, 184, 229)
        self.ship_limit = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (242, 221, 110)
        self.alienBullet_color = (214, 122, 177)
        self.bullets_allowed = 5
        self.fleet_drop_speed = 10
        self.speedup_scale = 1.3
        self.score_scale = 1.5
        
        self.init_dynamic_set()

    def init_dynamic_set(self):
        self.shipSpeed = 1.5
        self.alien_speed = 1.0
        self.bullet_speed = 3.0
        self.fleet_direction = 1
        self.alien_points = 50
    
    def increase_speed(self):
        self.shipSpeed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
    